from discord.ext import commands
import milkman


class Test:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test',
                      description='Does whatever I am testing at the moment',
                      brief='Probably does something broken',
                      pass_context=True)
    async def test(self, context):
        # await self.bot.send_message(context.message.channel, "Testing reload")
        await self.bot.send_file(context.message.channel, milkman.create_spillman(context.message.author.avatar_url))

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

    @commands.command(name='unload', hidden=True, pass_context=True)
    async def cog_unload(self, context, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await self.bot.send_message(context.message.channel, f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await self.bot.send_message(context.message.channel, '**`SUCCESS`**')

    @commands.command(name='reload', hidden=True, pass_context=True)
    async def cog_reload(self, context, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await self.bot.send_message(context.message.channel, f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await self.bot.send_message(context.message.channel, '**`SUCCESS`**')



def setup(bot):
    bot.add_cog(Test(bot))
