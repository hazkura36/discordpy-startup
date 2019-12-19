from discord.ext import commands
import os
import traceback
import discord
from discord.ext import tasks
from datetime import datetime 

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 645902454860283904

client = discord.Client()
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
async def on_ready():
    print('ready')

@client.event
async def on_ready():
    while True:
        if time.strftime('%H:%M:%S',time.localtime())=='10:12:00':
            channel = client.get_channel('CHANNEL_ID')
            await client.send_message(channel, '勝手に喋るよ')
            sleep(5)
        
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

client.run(token)
bot.run(token)
