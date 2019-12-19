from discord.ext import commands
import os
import traceback
import discord
from discord.ext import tasks
from datetime import datetime 

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 645902454860283904


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
async def on_ready():
    print('ready')


        
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
