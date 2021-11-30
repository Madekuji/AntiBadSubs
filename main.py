# Original code from https://github.com/Ryu1845/delete_otak
# Modified by Madekuji-san

from dotenv import load_dotenv
from datetime import datetime


import os

load_dotenv('.env')

import discord

client = discord.Client()

database = ['OtakMoriTranslationsVTubers', 'UCF4-I8ZQL6Aa-iHfdz-B9KQ', 'UCizN2tVLNcwP67bAHlVRg1Q', 'UC1Ysc66Fb-E-3UH4Jb9padA', 'UC0zZ3QsUhYq6hQ0A-_THfgA', 'UC3hXsep6P_d1Z5opjCDFUqA']	

def utcTime():
  utcTimestr = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
  return utcTimestr

channelEmbed=discord.Embed(title="You posted a bad channel!", description="The channel you sent is known to be a bad clipper who harms talents through their focus on clickbait, bad metadata, mistranslation, or doxxing. Please consider looking for clips elsewhere.", color=0xcc0000)
channelEmbed.set_author(name="AntiBadSubs", icon_url="https://i.vgy.me/wWzvwy.png")
channelEmbed.set_thumbnail(url="https://i.vgy.me/qLhqkK.png")

videoEmbed=discord.Embed(title="You posted a bad sub!", description="The video you sent is from a channel that is known to be a bad clipper who harms talents through their focus on clickbait, bad metadata, mistranslation, or doxxing. Please consider looking for clips elsewhere.", color=0xcc0000)
videoEmbed.set_author(name="AntiBadSubs", icon_url="https://i.vgy.me/wWzvwy.png")
videoEmbed.set_thumbnail(url="https://i.vgy.me/qLhqkK.png")

aboutEmbed=discord.Embed(title="AntiBadSubs Bot", description="This bot will remove messages containing links to videos from known bad subbers and clippers, as well as their channel links.", color=0xcc0000)
aboutEmbed.set_thumbnail(url="https://i.vgy.me/tWyCbF.png")
aboutEmbed.add_field(name=chr(173), value="[The bot is available on GitHub.](https://github.com/Madekuji/AntiBadSubs)", inline=True)

inviteEmbed=discord.Embed(title="Invite this bot to your server!", url="https://discord.com/api/oauth2/authorize?client_id=896309801875812362&permissions=429497117696&scope=bot", color=0xcc0000)
inviteEmbed.set_author(name="AntiBadSubs Bot")
inviteEmbed.set_thumbnail(url="https://i.vgy.me/tWyCbF.png")

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
        await message.channel.send(embed = channelEmbed)
        print(f" [" + utcTime() + "] " + "[Embed Sent - Channel Trigger] " + "[" + dcServer + ": " + dcChannel + "] ")

    embed: discord.Embed
    for embed in message.embeds:

        dcEmbed = embed.author.url
        
        if dcEmbed:
          if any(x in dcEmbed for x in database):
              await message.delete()
              print(f" [" + utcTime() + "] " + "[Message Deleted] " + "[" + dcServer + ": " + dcChannel + "] " + dcMessage)
              await message.channel.send(embed = videoEmbed)
              print(f" [" + utcTime() + "] " + "[Embed Sent - Video Trigger] " + "[" + dcServer + ": " + dcChannel + "] ")
    
    if dcMessage.startswith('abs!about'):
      await message.channel.send(embed = aboutEmbed)
      print(f" [" + utcTime() + "] " + "[abs!about Triggered] " + "[" + dcServer + ": " + dcChannel + "] ")

    if dcMessage.startswith('abs!list'):
      await message.channel.send("<https://docs.google.com/spreadsheets/d/1GF_QC5XpvUgFAYqvUTvLyaf3SwzPHpSiQEJwz6hTo_c/edit?usp=sharing>")
      print(f" [" + utcTime() + "] " + "[abs!list Triggered] " + "[" + dcServer + ": " + dcChannel + "] ")

    if dcMessage.startswith('abs!invite'):
      inviteEmbed.set_footer(text=("Bot server limit: " + str(len(client.guilds)) + "/100"))
      await message.channel.send(embed = inviteEmbed)
      print(f" [" + utcTime() + "] " + "[abs!invite Triggered] " + "[" + dcServer + ": " + dcChannel + "] ")

    if dcMessage.startswith('abs!activity'):
      await client.change_presence(activity=discord.Game(name='abs!help'))
      await message.channel.send("Activity updated.")
      print(f" [" + utcTime() + "] " + "[abs!activity Triggered] " + "[" + dcServer + ": " + dcChannel + "] ")


client.run(os.getenv('TOKEN'))