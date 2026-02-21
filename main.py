import os
from urllib import request
from dotenv import load_dotenv
import discord
from discord.ext import commands
import aiohttp
import asyncio

from KeywordHandler import KeywordHandler

load_dotenv()
api_key = str(os.getenv("API_KEY"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# Das werden wir wohl wegwerfen
INTENT_KEYWORDS: list = [
    "spells",
    "alignments",
    "backgrounds",
    "classes",
    "conditions",
    "damage-types",
    "equipment",
    "feats",
    "features",
    "languages",
]


def populate_keywords():
    pass


@bot.event
async def on_ready():
    # Dynamically adding a new session attribute to bot object
    bot.session = aiohttp.ClientSession(base_url="https://www.dnd5eapi.co/api/2014/")
    print(f"Bot logged on as {bot.user}")


@bot.event
async def on_close():
    await bot.session.close()


@bot.command()
async def ping(context):
    await context.send("Pong!")


@bot.command()
async def spell(context, *, spellname):
    print(spellname)
    spellname = str(spellname.lower().strip().replace(" ", "-"))
    print(spellname)
    async with bot.session.get(f"spells/{spellname}") as response:
        print(response.status)
        data = await response.json()
        await context.send(data["desc"][0])


@bot.command()
async def test(context):
    keyword_handler = KeywordHandler(bot.session)
    print(keyword_handler.spells)


bot.run(api_key)
