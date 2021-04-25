from json import dump, load
from typing import Dict, Optional

from discord.ext.commands import Bot
from discord.ext.commands.cog import Cog
from discord.utils import get

from cogs.errors import GuildNotFound
from main import logger


def get_guild_data(guild_id: Optional[int] = None):
    with open("bot-data/guild-ideas-data.json") as file:
        data: Dict[int, Dict] = load(file)
    if guild_id is not None:
        if guild_id in data.keys():
            return data[guild_id]
        raise GuildNotFound(guild_id)
    return data


def save_guild_data(data, append: bool = False):
    if append:
        _data = get_guild_data()
        _data.update(data)
        data = _data
    with open("bot-data/guild-ideas-data.json", "w") as file:
        dump(data, file)


def add_guild2guild_data(guild_data):
    save_guild_data(guild_data, True)


class MyCog(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        logger.info(self.__class__.__name__ + " cog is ready")
        for guild in self.bot.guilds:
            channel = get(guild.channals, name='bots-console')
            await channel.send(self.__class__.__name__ + " extraction is ready")
