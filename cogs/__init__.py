from discord.ext.commands.cog import Cog

from main import logger


class MyCog(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        logger.info(self.__class__.__name__+" cog is ready")
        await self.bot.get_channel(831897786202062858).send(self.__class__.__name__+" extraction is ready")
