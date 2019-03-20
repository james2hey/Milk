from datetime import datetime
import sys
import traceback

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound, CommandOnCooldown
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from log import log

from config import Config

BOT_PREFIX = "milk "

initial_extensions = ['cogs.voice',
                      'cogs.misc',
                      'cogs.drinks',
                      'cogs.images',
                      'cogs.test',
                      'cogs.redditor',
                      'cogs.flat_memes']

bot = commands.Bot(command_prefix=BOT_PREFIX, description='Milk is flowing')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


async def do_the_bins():
    ch = bot.get_channel("548040895996362752")

    for server in bot.private_channels:
        print(server)
        for member in server.recipients:
            print(member)

    out = " @everyone"
    # for server in bot.servers:
    #     for member in server.members:
    #         out += " " + member.mention

    if datetime.now().isocalendar()[1] % 2 == 0:
        out = "Don't forget to put the red bin out! " + out
        await bot.send_message(ch, out)
    else:
        out = "Don't forget to put the yellow bin out! " + out
        await bot.send_message(ch, out)


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(game=discord.Game(name="milk help (on Raspberry Pi)"))
    print('Milk is flowing')

    scheduler = AsyncIOScheduler()
    scheduler.add_job(do_the_bins, 'cron', day_of_week='wed', hour=20)
    # scheduler.add_job(do_the_bins, 'interval', seconds=3)
    scheduler.start()


@bot.event
async def on_command_completion(command, context):
    log(command, context)


@bot.event
async def on_command_error(error, context):
    log(error, context)
    if isinstance(error, CommandOnCooldown):
        out_string = "You milked too hard. `{}` is on cool down. {}".format(
            context.invoked_with,
            str(error).split(".", 1)[1].strip()
        )
        await bot.send_message(context.message.channel, out_string)
    else:
        await bot.send_message(context.message.channel, "ah shit the devs fucked up")
        raise error


bot.run(Config().token, bot=True)
