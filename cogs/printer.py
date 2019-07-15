from discord.ext import commands
from octorest import OctoRest
from config import Config
from log import logGeneric


class Printer:
    def __init__(self, bot):
        self.bot = bot
        try:
            self.op_client = OctoRest(url="http://octopi.local", apikey=Config().octopi_api_key)
        except ConnectionError as ex:
            logGeneric(ex)

    @commands.command(name='print',
                      description="Gets the current printer status",
                      brief="Is that 3D print done yet?",
                      pass_context=True)
    async def print_status(self, context, mention: str = None):
        job_info = self.op_client.job_info()
        if job_info["state"] == "Printing":
            await self.bot.send_message(context.message.channel,
                                        "Printer is printing\n"
                                        "Currently {} is {:.1f}% done"
                                        .format(
                                            job_info["job"]["file"]["name"],
                                            job_info["progress"]["completion"]
                                        ))
        else:
            await self.bot.send_message(context.message.channel, "Printer is {}".format(job_info["state"]))


def setup(bot):
    bot.add_cog(Printer(bot))
