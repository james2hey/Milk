from discord.ext import commands


class Images:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='udder',
                      description="where does milk come from?",
                      brief="where does milk come from?",
                      pass_context=True)
    async def udder(self, context):
        await self.bot.send_file(context.message.channel, "resources/img/udder.jpg")


def setup(bot):
    bot.add_cog(Images(bot))
