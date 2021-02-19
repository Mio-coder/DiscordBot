import discord
from discord.ext import commands

client = commands.Bot(command_prefix="o- ")



@client.event
async def on_ready():
    print("Bot is ready.")


@client.command()
async def ping(ctx):
    await ctx.send("pong -o")


@client.command()
async def table(ctx, rows=10):
    text = str("#" + "-" * (rows - 2) + "#" + "\n" + "").join(["".join([("#" * 10) + "\n" for _ in range(rows // 2)])]*2)
    ctx.send(text)

client.run("ODEwNDU1ODY4NTY3MDYwNTEx.YCj52A.fNwBUO010EqskAC1ZI2JWwShLvM")
