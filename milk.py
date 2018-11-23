import discord
from config import Config
from cup import FreezeMilk

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
            await client.send_message(message.channel, "```"
                                                       "Your daily intake of calcium"
                                                       "cup - show your cups current state\n"
                                                       "pour - pour a level of milk in your cup\n"
                                                       "drink - drink that milky goodness\n"
                                                       "```")

        elif args[1] == "trent":
            await client.send_message(message.channel, ":boom: KABOOM!")

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
            if len(args) > 2 and message.mentions:
                current_cup = freeze_milk.stats[message.mentions[0]]
            full_cup = current_cup.drink()
            pre_text = ""
            if full_cup:
                pre_text = "You drunk a full glass of milk. Upgrade time! "

            await client.send_message(message.channel, pre_text + current_cup.draw())

        elif args[1] == "test":
            person = message.mentions[0].name
            await client.send_message(message.channel, person)

        elif args[1] == "one" and args[2] == "step":
            await client.send_message(message.channel, "One Step Aheeeaadd")
            voice = await client.join_voice_channel(message.author.voice_channel)
            player = voice.create_ffmpeg_player('resources/sounds/OneStepAhead.mp3')
            player.start()

        else:
            await client.send_message(message.channel, ":milk: Unrecognised command :milk:")


client.run(Config().token)
