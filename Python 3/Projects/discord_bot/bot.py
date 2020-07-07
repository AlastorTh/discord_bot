import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_member_join(member):
    print(f"{member} has joined the server.")


@client.event
async def on_member_remove(member):
    print(f"{member} has left the server.")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!{round(client.latency * 1000)} ms')


@client.command()
async def roll20(ctx):
    die_values = []
    die_values.extend(range(1, 21))
    await ctx.send(f"{random.choice(die_values)}")


client.run("Njg4NzYwNDk5OTU3MTM3NDE0.XwRxdA.S6B6tHGlQhZ0bp0AR5oKmzaX3Vw")
