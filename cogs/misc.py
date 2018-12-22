from discord import Embed
from discord.ext import commands
from random import randint

from mintai import get_mintai


class Misc:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='trent',
                      description="lactose intolerance + milk =",
                      brief="What happens when trent drinks milk?",
                      pass_context=True)
    async def trent(self, context):
        await self.bot.add_reaction(context.message, "\U0001F602")
        await self.bot.send_message(context.message.channel, ":boom: KABOOM!")
        if context.message.author.voice_channel:
            if not self.bot.voice_client_in(context.message.author.server):
                voice = await self.bot.join_voice_channel(context.message.author.voice_channel)
            else:
                voice = self.bot.voice_client_in(context.message.author.server)
            fart = randint(1, 7)
            player = voice.create_ffmpeg_player('resources/sounds/farts/fart' + str(fart) + '.mp3')
            player.start()

    @commands.command(name='mint',
                      description="idk",
                      brief="idk",
                      pass_context=True)
    async def mint(self, context):
            post = get_mintai()
            embed = Embed(title=post.title, color=0x111, url=post.url, )

            # embed.set_image(post.url)
            embed.add_field(name=post.permalink, value=post.url)

            await self.bot.send_message(context.message.channel, embed=embed)

    @commands.command(name='james',
                      description="my👏creator👏is👏the👏best😘🤗👏",
                      brief="Who is he?",
                      pass_context=True)
    async def james(self, context):
        await self.bot.send_message(context.message.channel, "2HEY")


def setup(bot):
    bot.add_cog(Misc(bot))
