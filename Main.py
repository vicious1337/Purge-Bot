prefix = "!"
token = "TOKEN HERE"

import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import bot
import pyfiglet
from pyfiglet import Figlet

client = commands.Bot(command_prefix=prefix, self_bot=True)

custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('purge bot'))

@client.event
async def on_ready():
    print ("Username: {}#{}".format(client.user.name, client.user.discriminator))
    print ("How to use: !purge [amount]")
    print ("Creator: github.com/vicious1337")

@client.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

client.run(token, bot=False)
