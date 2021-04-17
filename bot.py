import discord
import os 
import asyncio
import requests

# Configure the bot
bot = discord.Client()

async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="-help | NAME OF BOT"))

async def on_message(message):
    if message.author == bot.user:
        return
      
    if message.content.startswith("-help"):
        emb = discord.Embed(title='NAME OF BOT Commands')
        emb.add_field(title='-ping', value='Mesaure your ping', inline=False)
        emb.add_field(title='-poll e.g Is pineapple good on pizza ?', value='Mesaure your ping', inline=False)
        
    if message.content.startswith('-ping'):
        emb = discord.Embed(title='Pong!  ', description=f'{round(bot.latency * 1000)}ms')
        await message.channel.send(embed=emb)
        
    if message.content.startswith("-poll"):
        msg = message.content
        emb = discord.Embed(title='POLL', description=msg.replace('-poll',''))
        emb.add_field(name='Initiator', value=f'Initiated by {message.author}')
        poll = await message.channel.send(embed=emb)
        await poll.add_reaction('👍')
        await poll.add_reaction('👎')

bot.run('TOKEN HERE')
