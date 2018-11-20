import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Milk is flowing")
    await client.change_presence(game=discord.Game(name="Mint"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content:
        await process_message(message)


async def process_message(message):
    args = message.content.split(" ")
    print(args)
    if args[0] == "milk":
        if args[1] == "trent":
            await client.send_message(message.channel, ":boom: KABOOM!")
        else:
            await client.send_message(message.channel, "Unrecognised milky command")


client.run("NTE0MjYwMzEzMDU5NjIyOTE3.DtT-dw.3McwIX5CvtFYBumxuQuPHTgPkr4")
