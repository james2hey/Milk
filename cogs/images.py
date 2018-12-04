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


async def send_image(self, context, resource):
        await self.bot.send_file(context.message.channel, resource)

def setup(bot):
    bot.add_cog(Images(bot))
