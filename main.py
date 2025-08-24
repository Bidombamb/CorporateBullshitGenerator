import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import requests

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
url = "https://corporatebs-generator.sameerkumar.website/"

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():

    try:
        await bot.tree.sync()
    except Exception as e:
        print(e)

    print("Initializing bullshit")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    

    await bot.process_commands(message)

@bot.tree.command(name="generatebullshit", description="Generate som corporate bullshit!")
async def generatebullshit(interaction):
    response = requests.get(url)

    if response.ok:
        phrase = response.json()["phrase"]

        await interaction.response.send_message(phrase)
    else:
        await interaction.response.send_message(f"Couldn't generate bullshit :( {response.status_code}")












bot.run(token, log_handler=handler, log_level=logging.DEBUG)