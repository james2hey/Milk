from discord.ext import commands

from milkman import create_milkman


class Test:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test',
                      description='Does whatever I am testing at the moment',
                      brief='Probably does something broken',
                      pass_context=True)
    async def test(self, context):
        await self.bot.send_file(context.message.channel, create_milkman(context.message.author.avatar_url))

    @commands.command(name='leave',
                      description='Makes the bot leave your voice channel',
                      brief='Kick me from voice channels',
                      pass_context=True)
    async def leave(self, context):
        if self.bot.voice_client_in(context.message.author.server):
            voice = self.bot.voice_client_in(context.message.author.server)
            await voice.disconnect()

    @commands.command(name='die',
                      description='Kills the python script running the bot',
                      brief='Kill me :(',
                      pass_context=True)
    async def die(self, context):
        await self.bot.send_message(context.message.channel, "Why you do dis??")
        await self.bot.logout()

    @commands.command(name='echo',
                      description='Repeats whatever you say',
                      brief='Repeats ya',
                      pass_context=True)
    async def echo(self, context, *, all_args: str = None):
        print(all_args)
        if all_args:
            await self.bot.send_message(context.message.channel, all_args)



def setup(bot):
    bot.add_cog(Test(bot))
