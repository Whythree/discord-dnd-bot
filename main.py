import discord
import os

#ToDo: Eigene Implementation des Beispiels schreiben.
intents = 
client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


