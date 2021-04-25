from discord.ext.commands import Bot, command, Context

from cogs import MyCog
from cogs.ideas.client import IdeasClient


class Ideas(MyCog):

    def __init__(self, bot: Bot):
        super(Ideas, self).__init__(bot)
        self.client = IdeasClient()
        self.channel_name = "bots-console"

    @command("idea:list")
    async def list(self, ctx: Context):
        if ctx.channel.name == self.channel_name:
            data = await self.client.get()
            string = "ideas:\n"
            for idea, (author, votes) in data:
                string += f"{idea} - author: {author}, votes: {votes}" + "\n"
            if string.strip() == "ideas:":
                string = "nothing :("
            await ctx.send(string)

    @command("idea:add")
    async def add(self, ctx: Context, idea: str, anonymous: bool = False):
        if ctx.channel.name == self.channel_name:
            data = await self.client.get()
            if idea in data.keys():
                await ctx.send(f"\"{idea}\" already exist")
            else:
                if anonymous:
                    await self.client.add(idea)
                else:
                    await self.client.add(idea, ctx.author.display_name)

    @command("idea:delete")
    async def delete(self, ctx: Context, idea: str):
        if ctx.channel.name == self.channel_name:
            data = await self.client.get()
            if idea in data.keys():
                await self.client.delete(idea, ctx.author.display_name)
            else:
                await ctx.send(f"\"{idea}\" not found")

    @command("idea:search")
    async def search(self, ctx: Context, idea: str):
        if ctx.channel.name == self.channel_name:
            data = await self.client.get()
            if idea in data.keys():
                await ctx.send(f"\"{idea}\" found")
            else:
                await ctx.send(f"\"{idea}\" not found")
