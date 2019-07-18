from discord.ext import commands
from discord import Embed
from octorest import OctoRest
from config import Config
from log import logGeneric
import requests
import datetime


class Printer:
    def __init__(self, bot):
        self.bot = bot
        try:
            self.op_client = OctoRest(url="http://192.168.1.158/", apikey=Config().octopi_api_key)
        except ConnectionError as ex:
            logGeneric(ex)

    @commands.command(name='print',
                      description="Gets the current printer status",
                      brief="Is that 3D print done yet?",
                      pass_context=True)
    async def print_status(self, context, rest: str = None):
        job_info = self.op_client.job_info()
        if rest is None:
            if job_info["state"] == "Printing":

                floor_percent = int((job_info["progress"]["completion"] // 5) * 5)
                time_elapsed_nice = str(datetime.timedelta(seconds=job_info["progress"]["printTime"]))
                if job_info["progress"]["printTimeLeft"] is None:
                    time_left_nice = "Calculating..."
                    time_completion = "Waiting for estimate..."
                else:
                    time_left_nice = str(datetime.timedelta(seconds=job_info["progress"]["printTimeLeft"]))
                    time_completion = self.add_secs(datetime.datetime.now().time(), job_info["progress"]["printTimeLeft"]).strftime("%I:%M %p")

                embed = Embed(title="Athol's 3D Printer", description="Printer is currently: Printing", color=0x0080ff)

                embed.add_field(
                    name="Progress",
                    value="[{}{}](https://github.com/james2hey/Milk) ({:.1f}%)".format(
                        "■" * (floor_percent // 5),
                        "□" * ((100 - floor_percent) // 5),
                        job_info["progress"]["completion"]
                    ),
                    inline=True)

                embed.add_field(name="File", value=job_info["job"]["file"]["name"].replace(".gcode", ""), inline=False)
                embed.add_field(name="Time Elapsed", value=time_elapsed_nice, inline=True)
                embed.add_field(name="Estimated Time Left", value=time_left_nice, inline=True)
                embed.add_field(name="Estimated Completion Time", value=time_completion, inline=True)
                await self.bot.send_message(context.message.channel, embed=embed)
                self.getImage()
                await self.bot.send_file(context.message.channel, 'temp/snapshot.jpg')
            else:
                embed = Embed(
                    title="Athol's 3D Printer",
                    description="Printer is currently: {}".format(job_info["state"]),
                    color=0x0080ff)
                embed.add_field(
                    name="State",
                    value="{}".format(job_info["state"])
                )
                await self.bot.send_message(context.message.channel, embed=embed)
        else:
            if rest.lower() == "pause":
                if context.message.author.id == '311429319505346560':
                    err_message = None
                    try:
                        paused = self.op_client.pause()
                    except RuntimeError as e:
                        err_message = "{}".format(e).split("OK:")[1].split(",")[0].strip()

                    if err_message:
                        await self.bot.send_message(context.message.channel, "Error: {}".format(err_message))
                    else:
                        await self.bot.send_message(context.message.channel, "Printer paused")
                else:
                    scones = await self.bot.get_user_info('311429319505346560')
                    await self.bot.send_message(context.message.channel, "Only {} can do that, sorry".format(scones.mention))

    @staticmethod
    def add_secs(tm, secs):
        fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
        fulldate = fulldate + datetime.timedelta(seconds=secs)
        return fulldate.time()

    @staticmethod
    def getImage():
        img_data = requests.get("http://192.168.1.158/webcam/?action=snapshot").content
        with open('temp/snapshot.jpg', 'wb') as handler:
            handler.write(img_data)

def setup(bot):
    bot.add_cog(Printer(bot))
