import sys
import traceback

import discord
from discord.ext import commands

from config import Config

BOT_PREFIX = "milk "

initial_extensions = ['cogs.voice',
                      'cogs.misc',
                      'cogs.drinks',
                      'cogs.images',
                      'cogs.test']

bot = commands.Bot(command_prefix=BOT_PREFIX, description='Milk is flowing')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(game=discord.Game(name="milk help (on scones' pc)"))
    print('Milk is flowing')

bot.run(Config().token, bot=True)
