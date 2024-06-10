import discord
from discord.ext import commands

TOKEN = 'BOT_TOKEN'

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='BOT_PREFIX', intents=intents)

bot.run(TOKEN)