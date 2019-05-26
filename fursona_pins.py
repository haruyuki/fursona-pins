import os
from os.path import isfile, join
import sys
import traceback

import discord
from discord.ext import commands

from constants import Constants

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(Constants.prefix),
    description='A Fursona Pins Discord bot!',
    case_insensitive=True)
bot.remove_command('help')

if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in os.listdir(Constants.cogs_directory) if isfile(join(Constants.cogs_directory, f))]:
        try:
            bot.load_extension(f'{Constants.cogs_directory}.{extension}')
        except (discord.ClientException, ModuleNotFoundError):
            if extension == '.DS_Store':
                pass
            else:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('--------')
    print(f'Discord.py Version: {discord.__version__}')
    print('--------')
    print(f'Use this link to invite {bot.user.name}: https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=511040')
    print('--------')
    print(f'You are running {bot.user.name} v{Constants.version}')
    print('Created by Haru#5616')
    await bot.change_presence(activity=discord.Game(Constants.playing_text), status=discord.Status.online)


@bot.event
async def on_command_error(_, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

bot.run(Constants.discord_token, bot=True)
