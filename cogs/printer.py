from discord.ext import commands
from discord import Embed
from octorest import OctoRest
from config import Config
from log import logGeneric
import math
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
    async def print_status(self, context, mention: str = None):
        job_info = self.op_client.job_info()
        if job_info["state"] == "Printing":

            floor_percent = math.floor(job_info["progress"]["completion"] / 10) * 10
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

        else:
            await self.bot.send_message(context.message.channel, "Printer is {}".format(job_info["state"]))

    @staticmethod
    def add_secs(tm, secs):
        fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
        fulldate = fulldate + datetime.timedelta(seconds=secs)
        return fulldate.time()

def setup(bot):
    bot.add_cog(Printer(bot))
