from discord.ext import commands
from random import randint
import urbandictionary as ud


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
            fart = randint(1, 21)
            player = voice.create_ffmpeg_player('resources/sounds/farts/fart' + str(fart) + '.mp3')
            player.start()

    @commands.command(name='forkknife',
                      description="prank the boys when you die early",
                      brief="Get them when you're spectating",
                      pass_context=True)
    async def forkknife(self, context):
        if context.message.author.voice_channel:
            if not self.bot.voice_client_in(context.message.author.server):
                voice = await self.bot.join_voice_channel(context.message.author.voice_channel)
            else:
                voice = self.bot.voice_client_in(context.message.author.server)
            fart = randint(0, 2)
            player = voice.create_ffmpeg_player('resources/sounds/fortnite/' + str(fart) + '.mp3')
            player.start()

    @commands.command(name='james',
                      description="my👏creator👏is👏the👏best😘🤗👏",
                      brief="Who is he?",
                      pass_context=True)
    async def james(self, context):
        await self.bot.send_message(context.message.channel, "2HEY is a dumb chicken")
        await self.bot.send_file(context.message.channel, "resources/img/dumbChicken.gif")

    @commands.command(name='dan',
                      description="DPD",
                      brief="Acronym",
                      pass_context=True)
    async def dan(self, context):
        await self.bot.send_message(context.message.channel, "PUMP")
        await self.bot.send_message(context.message.channel, "PUMP")
        if context.message.author.voice_channel:
            if not self.bot.voice_client_in(context.message.author.server):
                voice = await self.bot.join_voice_channel(context.message.author.voice_channel)
            else:
                voice = self.bot.voice_client_in(context.message.author.server)
            player = voice.create_ffmpeg_player('resources/sounds/dan.mp3')
            player.start()

    @commands.command(name='ud',
                      description="Urban dictionary test",
                      brief="Will it work",
                      pass_context=True)
    async def urbanBoi(self, context, rest: str = None):
        if rest:
            word = ud.define(rest)[0]
            await self.bot.send_message(context.message.channel, word.word + " " + word.definition)
        else:
            rando = ud.random()[0]
            await self.bot.send_message(context.message.channel, rando.word + " " + rando.definition)


def setup(bot):
    bot.add_cog(Misc(bot))
