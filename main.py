import logging
from logging import Formatter, FileHandler, StreamHandler
from sys import stdin

from discord import Member, Role
from discord.ext.commands import Bot, Context

from dotenv import load_dotenv
from os import environ

load_dotenv()
DISCORD_TOKEN = environ["DISCORD_TOKEN"]

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
formatter = Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
handler = FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(formatter)
logger.addHandler(handler)
handler = StreamHandler(stream=stdin)
handler.setFormatter(formatter)
logger.addHandler(handler)

bot = Bot(command_prefix="!")


async def find_role(member: Member, role: Role):
    for r in member.roles:
        if r == role:
            return True
    return False


@bot.command(name="ext:add")
async def add_cog(ctx: Context, name: str):
    if ctx.channel.name == "bots-console":
        if await find_role(ctx.author, ctx.guild.get_role(831173962158440508)):
            await bot.load_extension(f"cogs.{name}")
            logger.info(f"added cog {name}")
        else:
            await ctx.send("you don't have permission to menage bots")


@bot.command(name="ext:del")
async def add_cog(ctx: Context, name: str):
    if ctx.channel.name == "bots-console":
        if await find_role(ctx.author, ctx.guild.get_role(831173962158440508)):
            await bot.unload_extension(f"cogs.{name}")
            logger.info(f"added cog {name}")
        else:
            await ctx.send("you don't have permission to menage bots")


@bot.command(name="ext:refresh")
async def add_cog(ctx: Context, name: str):
    if ctx.channel.name == "bots-console":
        if await find_role(ctx.author, ctx.guild.get_role(831173962158440508)):
            await bot.reload_extension(f"cogs.{name}")
            logger.info(f"added cog {name}")
        else:
            await ctx.send("you don't have permission to menage bots")


bot.run(DISCORD_TOKEN)
