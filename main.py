# Original code from https://github.com/Ryu1845/delete_otak
# Modified by Madekuji-san

from dotenv import load_dotenv
from datetime import datetime


import os

load_dotenv('.env')

import discord

client = discord.Client()

database = ['OtakMoriTranslationsVTubers', 'UCF4-I8ZQL6Aa-iHfdz-B9KQ', 'UCizN2tVLNcwP67bAHlVRg1Q']

def utcTime():
  utcTimestr = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
  return utcTimestr

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    
    if message.author.bot:
        return

    dcMessage = message.content
    dcServer = message.guild.name
    dcChannel = message.channel.name

    print(f" [" + utcTime() + "] " + "[Message Read] " + "[" + dcServer + ": " + dcChannel + "] " + dcMessage)

    if any(x in dcMessage for x in database):
        await message.delete()
        print(f" [" + utcTime() + "] " + "[Message Deleted] " + "[" + dcServer + ": " + dcChannel + "] " + dcMessage)
        await message.channel.send('https://i.vgy.me/qLhqkK.png')
        print(f" [" + utcTime() + "] " + "[Embed Sent - Channel Trigger] " + "[" + dcServer + ": " + dcChannel + "] ")

    embed: discord.Embed
    for embed in message.embeds:

        dcEmbed = embed.author.url
        
        if dcEmbed:
          if any(x in dcEmbed for x in database):
              await message.delete()
              print(f" [" + utcTime() + "] " + "[Message Deleted] " + "[" + dcServer + ": " + dcChannel + "] " + dcMessage)
              await message.channel.send('https://i.vgy.me/qLhqkK.png')
              print(f" [" + utcTime() + "] " + "[Embed Sent - Video Trigger] " + "[" + dcServer + ": " + dcChannel + "] ")
    
    if dcMessage.startswith('abs!about'):
      embedVar = discord.Embed(title = "AntiBadSubs Bot", description = "Remove all known bad subbers.")
      await message.channel.send(embed = embedVar)
      print(f" [" + utcTime() + "] " + "[abs!about Triggered] " + "[" + dcServer + ": " + dcChannel + "] ")

    if dcMessage.startswith('abs!list'):
      await message.channel.send("<https://docs.google.com/spreadsheets/d/1GF_QC5XpvUgFAYqvUTvLyaf3SwzPHpSiQEJwz6hTo_c/edit?usp=sharing>")
      print(f" [" + utcTime() + "] " + "[abs!list Triggered] " + "[" + dcServer + ": " + dcChannel + "] ")

    if dcMessage.startswith('abs!invite'):
      await message.channel.send("<https://discord.com/api/oauth2/authorize?client_id=896309801875812362&permissions=532576462912&scope=bot>")
      print(f" [" + utcTime() + "] " + "[abs!invite Triggered] " + "[" + dcServer + ": " + dcChannel + "] ")


client.run(os.getenv('TOKEN'))