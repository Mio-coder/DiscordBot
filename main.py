import logging
from logging import Formatter, FileHandler, StreamHandler
from os import environ
from sys import stdout

from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = environ["DISCORD_TOKEN"]

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
# noinspection SpellCheckingInspection
formatter = Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
handler = FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(formatter)
logger.addHandler(handler)
handler = StreamHandler(stream=stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)

bot = Bot(command_prefix="!")


@bot.event
async def on_ready():
    logger.info(f"bot is ready ----------")
    await bot.load_extension("cogs.Manager")


bot.run(DISCORD_TOKEN)
