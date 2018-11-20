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
    if args[0] == "milk":
        if len(args) < 2:
            await client.send_message(message.channel, "milk what?")
        if args[1] == "trent":
            await client.send_message(message.channel, ":boom: KABOOM!")

        if args[1] == "sconz":
            await client.send_message(message.channel, "Laters to your money")

        if args[1] == "james":
            await client.send_message(message.channel, "2hey")

        if args[1] == "upgrade":
            freeze_milk.stats[message.author].upgrade_cup()
            await client.send_message(message.channel, "You been upgraded to size " + str(freeze_milk.stats[message.author].size))

        if args[1] == "cup":
            await client.send_message(message.channel, freeze_milk.stats[message.author].draw())


client.run(Config().token)
