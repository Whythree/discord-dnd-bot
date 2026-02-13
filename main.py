import os
from dotenv import load_dotenv

import discord
from discord.ext import commands


load_dotenv()
api_key = str(os.getenv("API_KEY"))

bot =commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Bot logged on as {bot.user}")

@bot.command()
async def ping(context):
    await context.send("Pong!")


bot.run(api_key)