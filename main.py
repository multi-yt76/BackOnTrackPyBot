import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix = "$")

@bot.event
async def on_ready():
  print("Ready")

@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")

@bot.command()
async def add(ctx, arg1 : int, arg2 : int):
  await ctx.send(f"The answer is {arg1 + arg2}")

bot.run(os.environ.get("TOKEN"))