import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

load_dotenv()

token = os.getenv('token')

intents = discord.Intents.all()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
enlaceCurso = 'https://github.com/mouredev/Hello-Python?tab=readme-ov-file'


@bot.command()
async def info(ctx):
    await ctx.send("Soy un BOT desarrollado por Alex.py!")

@bot.command()
async def pene(ctx):
    await ctx.send(f"que te gusta que??")

@bot.command()
async def curso(ctx):
    await ctx.send(f"¡Hola! Aquí tienes el enlace del curso de Python:\n{enlaceCurso}")

@bot.command()
async def dado(ctx):
    await ctx.send(f"tiraste un dado y tu numero es '{random.randint(1,6)}'")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'hola' in message.content.lower():
        await message.channel.send(f"Hola {message.author.name}, como estas?")
    
        
    await bot.process_commands(message)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="k2spBOT",
    url="http://www.twitch.tv/sykoaalex"))
    print(f'{bot.user} ha iniciado sesión')

bot.run(token)