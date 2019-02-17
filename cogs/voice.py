from discord.ext import commands
from cogs.images import send_image
from random import randint


class Voice:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='oneStep',
                      description="Toohey is always one step ahead",
                      brief="One step aheeeeeeaad",
                      pass_context=True)
    async def one_step(self, context):
        if context.message.author.voice_channel:
            player = await self.get_player(context, 'resources/sounds/OneStepAhead.mp3')
            player.start()

        else:
            await  self.bot.send_message(context.message.channel, "You need to join a voice channel first")

    @commands.command(name='cow',
                      description="Go get some fresh milk straight from the source",
                      brief="Milk that cow",
                      pass_context=True)
    async def cow(self, context):
        if context.message.author.voice_channel:
            player = await self.get_player(context, 'resources/sounds/cow.mp3')
            player.start()

        else:
            await self.bot.send_message(context.message.channel, "You need to join a voice channel first")

    @commands.command(name='win',
                      description="Steppin' on the beach do do do DOOO",
                      brief="Got a dub did ya?",
                      pass_context=True)
    async def win(self, context):
        if context.message.author.voice_channel:
            await self.bot.send_message(context.message.channel, "Sweet victory bois!")
            await send_image(self, context, 'resources/img/sweetVictory/sv' + str(randint(0, 6)) + '.jpg')
            player = await self.get_player(context, 'resources/sounds/SweetVictory.m4a')
            player.start()

        else:
            await self.bot.send_message(context.message.channel, "You need to join a voice channel first")

    @commands.command(name='loss',
                      description="Steppin' on the beach do do do DOOO",
                      brief="Got a dub did ya?",
                      pass_context=True)
    async def loss(self, context):
        if context.message.author.voice_channel:
            await self.bot.send_message(context.message.channel, "R.I.P. bois!")
            player = await self.get_player(context, 'resources/sounds/SadLoss.m4a')
            player.start()

        else:
            await self.bot.send_message(context.message.channel, "You need to join a voice channel first")

    @commands.command(name='hoopla',
                      description="Steppin' on the beach do do do DOOO",
                      brief="Got a dub did ya?",
                      pass_context=True)
    async def hoopla(self, context):
        if context.message.author.voice_channel:
            player = await self.get_player(context, 'resources/sounds/Hoopla.opus')
            await send_image(self, context, 'resources/img/hoopla.' + ('jpg' if randint(0, 1) == 1 else 'gif'))
            player.start()

        else:
            await self.bot.send_message(context.message.channel, "You need to join a voice channel first")

    @commands.command(name='killin',
                      description="Oh Boy",
                      brief="Thought I wouldn't notice huh Morty?",
                      pass_context=True)
    async def killin_again(self, context):
        if context.message.author.voice_channel:
            player = await self.get_player(context, 'resources/sounds/OhBoy.opus')
            player.start()

        else:
            await self.bot.send_message(context.message.channel, "You need to join a voice channel first")

    async def get_player(self, context, resource):
        if not self.bot.voice_client_in(context.message.author.server):
            voice = await self.bot.join_voice_channel(context.message.author.voice_channel)
        else:
            voice = self.bot.voice_client_in(context.message.author.server)
            await voice.disconnect()
            voice = await self.bot.join_voice_channel(context.message.author.voice_channel)
        player = voice.create_ffmpeg_player(resource)
        player.volume = 0.3
        return player


def setup(bot):
    bot.add_cog(Voice(bot))
