import discord
import os
from discord.ext import commands
from typing import Union

bot = commands.Bot(command_prefix = "$")

# Episode 1 ->

@bot.event
async def on_ready():
  print("Ready")

@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")

@bot.command()
async def add(ctx, arg1 : int, arg2 : int):
  await ctx.send(f"The answer is {arg1 + arg2}")

# .. <-

# Episode 2 ->

@bot.command()
async def msg(ctx, arg : Union[discord.TextChannel, discord.Member], *, msg):
  if type(arg) == discord.Member:
    await arg.send(f"Sending Message To User: {msg}")

  elif type(arg) == discord.TextChannel:
    await arg.send(f"Sending Message To Channel: {msg}")

bot.run(os.environ.get("TOKEN"))