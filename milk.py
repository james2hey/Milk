import discord
from cup import Cup

client = discord.Client()
milk_stats = dict()

@client.event
async def on_ready():
    print("Milk is flowing")
    await client.change_presence(game=discord.Game(name="Mint"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content:
        get_milk_stats(message)
        await process_message(message)


async def process_message(message):
    args = message.content.split(" ")
    print(args)
    if args[0] == "milk":
        if args[1] == "trent":
            await client.send_message(message.channel, ":boom: KABOOM!")

        if args[1] == "sconz":
            await client.send_message(message.channel, "Laters to your money")

        if args[1] == "james":
            await client.send_message(message.channel, "2hey")

        if args[1] == "upgrade":
            milk_stats[message.author].upgrade_cup()
            await client.send_message(message.channel, "You been upgraded to size " + str(milk_stats[message.author].size))

        if args[1] == "cup":
            await client.send_message(message.channel, milk_stats[message.author].draw())


def get_milk_stats(message):
    print(len(milk_stats))
    if len(milk_stats) == 0:
        for member in message.server.members:
            milk_stats[member] = Cup()
    pass


client.run("NTE0MjYwMzEzMDU5NjIyOTE3.DtT-dw.3McwIX5CvtFYBumxuQuPHTgPkr4")
