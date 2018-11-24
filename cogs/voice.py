from discord.ext import commands


class Voice:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='oneStep',
                      description="Toohey is always one step ahead",
                      brief="One step aheeeeeeaad",
                      pass_context=True)
    async def one_step(self, context):
        if context.message.author.voice_channel:
            if not self.bot.voice_client_in(context.message.author.server):
                voice = await self.bot.join_voice_channel(context.message.author.voice_channel)
            else:
                voice = self.bot.voice_client_in(context.message.author.server)
            player = voice.create_ffmpeg_player('resources/sounds/OneStepAhead.mp3')
            player.start()

        else:
            await  self.bot.send_message(context.message.channel, "You need to join a voice channel first")

    @commands.command(name='cow',
                      description="Go get some fresh milk straight from the source",
                      brief="Milk that cow",
                      pass_context=True)
    async def cow(self, context):
        if context.message.author.voice_channel:
            if not self.bot.voice_client_in(context.message.author.server):
                voice = await self.bot.join_voice_channel(context.message.author.voice_channel)
            else:
                voice = self.bot.voice_client_in(context.message.author.server)
            player = voice.create_ffmpeg_player('resources/sounds/cow.mp3')
            player.start()

        else:
            await self.bot.send_message(context.message.channel, "You need to join a voice channel first")


def setup(bot):
    bot.add_cog(Voice(bot))
