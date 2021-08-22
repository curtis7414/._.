import discord
from discord.ext import commands

bot=commands.Bot(command_prefix= 'pog!')

@bot.event
async def on_ready():
    print (">> Bot is online<<")

bot.run("ODc4OTIzODYzMjQzNzcxOTA0.YSIPog.wos0_ry65oRgSTWuc-2S4FrKFEM")