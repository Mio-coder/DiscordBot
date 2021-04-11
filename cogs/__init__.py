from discord.ext.commands import command
from bot_menager import logger
from discord.ext.commands.cog import Cog


class PingPong(Cog):

    @Cog.listener()
    async def on_ready(self):
        logger.info(self.__class__.__name__+" is ready")

    @command(name="o- ping")
    async def pong(self, ctx):
        await ctx.send("pong -o")

