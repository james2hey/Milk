from discord.ext import commands


class KeyPeele:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='admission',
                      description="You can just help yourself sir",
                      brief="Excuse me garcon",
                      pass_context=True)
    async def admission(self, context):
        await self.send_voice(context, "resources/sounds/breakfast/admission.mp3")

    @commands.command(name='buckleup',
                      description="Aaaaahh the danish",
                      brief="Where shall we... fly to next?",
                      pass_context=True)
    async def buckle_up(self, context):
        await self.send_voice(context, "resources/sounds/breakfast/buckleup.mp3")

    @commands.command(name='donut',
                      description="The pitt of the donut",
                      brief="The pitt of the donut",
                      pass_context=True)
    async def donut(self, context):
        await self.send_voice(context, "resources/sounds/breakfast/donut.mp3")

    @commands.command(name='grease',
                      description="Hello grease where the yogurt flows like water",
                      brief="Like gogurt but to stay",
                      pass_context=True)
    async def grease(self, context):
        await self.send_voice(context, "resources/sounds/breakfast/grease.mp3")

    @commands.command(name='love',
                      description="I'll have what I'm having",
                      brief="A delight to the senses",
                      pass_context=True)
    async def love(self, context):
        await self.send_voice(context, "resources/sounds/breakfast/love.mp3")

    @commands.command(name='paper',
                      description="La de da",
                      brief="Paper and everything",
                      pass_context=True)
    async def paper(self, context):
        await self.send_voice(context, "resources/sounds/breakfast/paper.mp3")

    @commands.command(name='plum',
                      description="Well aren't you a tiny plum",
                      brief="Well aren't you a tiny plum",
                      pass_context=True)
    async def plum(self, context):
        await self.send_voice(context, "resources/sounds/breakfast/plum.mp3")

    @commands.command(name='theroom',
                      description="Can you believe this?",
                      brief="It all comes with the room",
                      pass_context=True)
    async def the_room(self, context):
        await self.send_voice(context, "resources/sounds/breakfast/theroom.mp3")

    @commands.command(name='fapoon',
                      description="Not a spoon, not a fork",
                      brief="Not a spoon, not a fork",
                      pass_context=True)
    async def whoru(self, context):
        await self.send_voice(context, "resources/sounds/breakfast/whoru.mp3")

    async def send_voice(self, context, mp3):
        if context.message.author.voice_channel:
            if not self.bot.voice_client_in(context.message.author.server):
                voice = await self.bot.join_voice_channel(context.message.author.voice_channel)
            else:
                voice = self.bot.voice_client_in(context.message.author.server)
            player = voice.create_ffmpeg_player(mp3)
            player.start()

        else:
            await  self.bot.send_message(context.message.channel, "You need to join a voice channel first")


def setup(bot):
    bot.add_cog(KeyPeele(bot))
