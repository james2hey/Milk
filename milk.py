import discord
from config import Config
from cup import FreezeMilk

client = discord.Client()


@client.event
async def on_ready():
    print("Milk is flowing")
    await client.change_presence(game=discord.Game(name="Butt Cracker"))


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

        if args[1] == "trent":
            await client.send_message(message.channel, ":boom: KABOOM!")

        elif args[1] == "sconz":
            await client.send_message(message.channel, "Laters to your money")

        elif args[1] == "james":
            await client.send_message(message.channel, "2hey")

        elif args[1] == "cup":
            await client.send_message(message.channel, current_cup.draw())

        elif args[1] == "pour":
            filled_level = current_cup.pour()
            if not filled_level:
                pre_text = "Wtf dude you spilt your milk? You're getting a downgrade lol"
            else:
                pre_text = str(message.author) + "'s milk level: " + str(filled_level) + " "

            await client.send_message(message.channel, pre_text + current_cup.draw())

        elif args[1] == "drink":
            full_cup = current_cup.drink()
            pre_text = ""
            if full_cup:
                pre_text = "You drunk a full glass of milk. Upgrade time! "

            await client.send_message(message.channel, pre_text + current_cup.draw())

        else:
            await client.send_message(message.channel, ":milk: Unrecognised command :milk:")


client.run(Config().token)
