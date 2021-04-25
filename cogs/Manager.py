from discord import Member, Role
from discord.ext.commands import Bot, command, Context, Cog
from discord.utils import get as get_role

from main import logger


class Manager(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot
        self.channel_name = "bots-console"
        self.role = "bot-manager"

    @staticmethod
    async def find_role(member: Member, role: Role):
        for r in member.roles:
            if r == role:
                return True
        return False

    @command(name="ext:add")
    async def add_cog(self, ctx: Context, name: str):
        if ctx.channel.name == self.channel_name:
            if await self.find_role(ctx.author, get_role(ctx.guild.roles, name=self.role)):
                await self.bot.load_extension(f"cogs.{name}")
                logger.info(f"added cog {name}")
            else:
                await ctx.send("you don't have permission to menage bots")

    @command(name="ext:del")
    async def add_cog(self, ctx: Context, name: str):
        if ctx.channel.name == self.channel_name:
            if await self.find_role(ctx.author, get_role(ctx.guild.roles, name=self.role)):
                await self.bot.unload_extension(f"cogs.{name}")
                logger.info(f"added cog {name}")
            else:
                await ctx.send("you don't have permission to menage bots")

    @command(name="ext:refresh")
    async def add_cog(self, ctx: Context, name: str):
        if ctx.channel.name == self.channel_name:
            if await self.find_role(ctx.author, get_role(ctx.guild.roles, name=self.role)):
                await self.bot.reload_extension(f"cogs.{name}")
                logger.info(f"added cog {name}")
            else:
                await ctx.send("you don't have permission to menage bots")
