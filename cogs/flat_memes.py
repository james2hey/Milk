from discord.ext import commands


class FlatMemes:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='admission',
                      description="You can just help yourself sir",
                      brief="Excuse me garcon",
                      pass_context=True)
    async def admission(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/admission.mp3")

    @commands.command(name='buckleup',
                      description="Aaaaahh the danish",
                      brief="Where shall we... fly to next?",
                      pass_context=True)
    async def buckle_up(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/buckleup.mp3")

    @commands.command(name='donut',
                      description="The pitt of the donut",
                      brief="The pitt of the donut",
                      pass_context=True)
    async def donut(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/donut.mp3")

    @commands.command(name='grease',
                      description="Hello grease where the yogurt flows like water",
                      brief="Like gogurt but to stay",
                      pass_context=True)
    async def grease(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/grease.mp3")

    @commands.command(name='love',
                      description="I'll have what I'm having",
                      brief="A delight to the senses",
                      pass_context=True)
    async def love(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/love.mp3")

    @commands.command(name='paper',
                      description="La de da",
                      brief="Paper and everything",
                      pass_context=True)
    async def paper(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/paper.mp3")

    @commands.command(name='plum',
                      description="Well aren't you a tiny plum",
                      brief="Well aren't you a tiny plum",
                      pass_context=True)
    async def plum(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/plum.mp3")

    @commands.command(name='theroom',
                      description="Can you believe this?",
                      brief="It all comes with the room",
                      pass_context=True)
    async def the_room(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/theroom.mp3")

    @commands.command(name='spork',
                      description="Not a spoon, not a fork",
                      brief="Not a spoon, not a fork",
                      pass_context=True)
    async def who_r_u(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/whoru.mp3")

    @commands.command(name='wrongchoice',
                      description="Wrrrrong  choice",
                      brief="Wrrrrong  choice",
                      pass_context=True)
    async def wrong_choice(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/wrong_choice.mp3")

    @commands.command(name='how',
                      description="How? Did I miss?",
                      brief="How? Did I miss?",
                      pass_context=True)
    async def how_did_i_miss(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/how_did_i_miss.mp3")

    @commands.command(name='what',
                      description="WHAT",
                      brief="WHAT",
                      pass_context=True)
    async def flat_meme(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/what.mp3")

    @commands.command(name='gulp',
                      description="Take a sippy sip",
                      brief="Take a sippy sip",
                      pass_context=True)
    async def gulpy_drink(self, context):
        await self.send_voice(context, "resources/sounds/drink.mp3")

    @commands.command(name='thursty',
                      description="star wars",
                      brief="star wars",
                      pass_context=True)
    async def thursty(self, context):
        await self.send_voice(context, "resources/sounds/flat_meme/jthursty_starwars.mp3")

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
    bot.add_cog(FlatMemes(bot))
