from dotenv import load_dotenv
from os import environ
from discord import Client

load_dotenv()
DISCORD_TOKEN = environ["DISCORD_TOKEN"]


# noinspection PyMethodMayBeStatic
class MainBot(Client):

    async def on_ready(self):
        print("bot is ready")

    


MainBot().run(DISCORD_TOKEN)
