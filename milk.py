import discord
from config import Config
from cup import FreezeMilk
from random import randint
from milkman import create_milkman
from mintai import get_mintai

client = discord.Client()

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')


@client.event
async def on_ready():
    print("Milk is flowing")
    await client.change_presence(game=discord.Game(name="milk help"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content:
        freeze_milk = FreezeMilk(message.server)
        freeze_milk.get_milk_stats()

        await process_message(message, freeze_milk)

        freeze_milk.save_milk_stats()


async def process_message(message, freeze_milk):
    args = message.content.split(" ")
    if args[0] == "milk" and len(args) > 1:
        current_cup = freeze_milk.stats[message.author]
        if args[1] == "help":
            embed = discord.Embed(title="Milk Help", description="Your daily intake of calcium", color=0x111)
            embed.add_field(name="Drinks", value="cup - show your cups current state\n"
                                                 "pour - pour a level of milk in your cup\n"
                                                 "drink - drink that milky goodness\n", inline=False)
            embed.add_field(name="Voice Chat", value="one step - \n"
                                                     "cow - moo\n", inline=False)
            embed.add_field(name="Images", value="udder - where does milk come from?\n", inline=False)
            embed.add_field(name="Misc", value="trent - lactose intolerance + milk = \n", inline=False)
            await client.send_message(message.channel, embed=embed)

        elif args[1] == "trent":
            await client.add_reaction(message, "\U0001F602")
            await client.send_message(message.channel, ":boom: KABOOM!")

        elif args[1] == "udder":
            await client.send_file(message.channel, "resources/img/udder.jpg")

        elif args[1] == "cup":
            if len(args) > 2 and message.mentions:
                current_cup = freeze_milk.stats[message.mentions[0]]

            await client.send_message(message.channel, current_cup.draw())

        elif args[1] == "pour":
            if len(args) > 2 and message.mentions:
                current_cup = freeze_milk.stats[message.mentions[0]]
            filled_level = current_cup.pour()
            if not filled_level:
                pre_text = "Wtf dude you spilt the milk? You're getting a downgrade lol"
            else:
                pre_text = "milk level: " + str(filled_level) + " "

            await client.send_message(message.channel, pre_text + current_cup.draw())

        elif args[1] == "drink":
            chance = randint(0, 100)

            if len(args) > 2 and message.mentions:
                if chance < 2:
                    current_cup.spill()
                    pre_text = "God damn, you knocked your glass off the table. Downgrade for you"
                else:
                    current_cup = freeze_milk.stats[message.mentions[0]]

            if chance < 2:
                current_cup.spill()
                pre_text = "God damn, you knocked your glass off the table. Downgrade for you"
            else:
                full_cup = current_cup.drink()
                pre_text = ""
                if full_cup:
                    pre_text = "You drunk a full glass of milk. Upgrade time! "
                else:
                    pre_text = "Aww jeez, your cup wasn't full. No upgrade for you"

            await client.send_message(message.channel, pre_text + current_cup.draw())

        elif args[1] == "one" and args[2] == "step":
            # await client.send_message(message.channel, "One Step Aheeeaadd")
            if message.author.voice_channel:
                if not client.voice_client_in(message.author.server):
                    voice = await client.join_voice_channel(message.author.voice_channel)
                else:
                    voice = client.voice_client_in(message.author.server)
                player = voice.create_ffmpeg_player('resources/sounds/OneStepAhead.mp3')
                player.start()

            else:
                await  client.send_message(message.channel, "You need to join a voice channel first")

        elif args[1] == 'cow':
            if message.author.voice_channel:
                if not client.voice_client_in(message.author.server):
                    voice = await client.join_voice_channel(message.author.voice_channel)
                else:
                    voice = client.voice_client_in(message.author.server)
                player = voice.create_ffmpeg_player('resources/sounds/cow.mp3')
                player.start()

            else:
                await client.send_message(message.channel, "You need to join a voice channel first")

        elif args[1] == "test":
            # create_milkman(message.author.avatar_url)
            # await client.send_message(message.channel, message.author.avatar_url)
            await client.send_file(message.channel, create_milkman(message.author.avatar_url))

        elif args[1] == "mint":
            post = get_mintai()
            embed = discord.Embed(title=post.title, color=0x111, url=post.url, )

            # embed.set_image(post.url)
            embed.add_field(name=post.permalink, value=post.url)

            await client.send_message(message.channel, embed=embed)

        elif args[1] == "james":
            await client.send_message(message.channel, "2HEY")
        elif args[1] == 'leave':
            if client.voice_client_in(message.author.server):
                voice = client.voice_client_in(message.author.server)
                await voice.disconnect()

        else:
            await client.send_message(message.channel, ":milk: Unrecognised command :milk:")


client.run(Config().token)
