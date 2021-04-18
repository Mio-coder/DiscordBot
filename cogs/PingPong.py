from discord.ext.commands import command
from . import MyCog


class PingPong(MyCog):

    @command(name="o- ping", )
    async def pong(self, ctx):
        await ctx.send("pong -o")

