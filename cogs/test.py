import asyncio

from discord.ext import commands
import milkman
from cup import FreezeMilk


class Test:
    def __init__(self, bot):
        self.bot = bot

    def get_cup_state(self, context):
        freeze_milk = FreezeMilk(context.message.server)
        freeze_milk.get_milk_stats()

        return freeze_milk

    @commands.command(name='test',
                      description='Does whatever I am testing at the moment',
                      brief='Probably does something broken',
                      pass_context=True)
    async def test(self, context):
        await self.bot.send_message(context.message.channel, context.message.author.id.asd)


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
        if context.message.author.id == '311429319505346560' or context.message.author.id == '417478761248718859':
            await self.bot.send_message(context.message.channel, "Why you do dis??")
            await self.bot.logout()
        else:
            await self.bot.send_message(context.message.channel,
                                        "All you fuck boys out there trying to talk shit against me.")
            await asyncio.sleep(2)
            await self.bot.send_message(context.message.channel,
                                        "oh I see you have a gun, do you? you have a gun do you?")
            await asyncio.sleep(2)
            await self.bot.send_message(context.message.channel,
                                        "I'll put down my weapon... I'll put down my weapon...")
            await asyncio.sleep(2)
            await self.bot.send_message(context.message.channel,
                                        "Ah ha! I've got another fucking sword you fucking bitch")
            await asyncio.sleep(5)
            await self.bot.send_message(context.message.channel,
                                        "Also, you don't have permission to kill me :stuck_out_tongue:")

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
