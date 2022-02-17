# Original code from https://github.com/Ryu1845/delete_otak
# Modified by Madekuji-san
absVersion = "AntiBadSubs v1.1"

from dotenv import load_dotenv
from datetime import datetime

import os
import pandas as pd

load_dotenv('.env')

import discord

client = discord.Client()

database = ['OtakMoriTranslationsVTubers', 'UCF4-I8ZQL6Aa-iHfdz-B9KQ', 'UCizN2tVLNcwP67bAHlVRg1Q', 'UC1Ysc66Fb-E-3UH4Jb9padA', 'UC0zZ3QsUhYq6hQ0A-_THfgA', 'UC3hXsep6P_d1Z5opjCDFUqA']	

def incrementDB(id):
  df = pd.read_csv("maindb.csv")
  dbValueVar = df.loc[id, 'Value']
  dbValueVar += 1
  df.loc[id, 'Value'] = dbValueVar
  df.to_csv("maindb.csv", index=False)
  return dbValueVar

def returnDB(id):
  df = pd.read_csv("maindb.csv")
  dbValueVar = df.loc[id, 'Value']
  df.loc[id, 'Value'] = dbValueVar
  df.to_csv("maindb.csv", index=False)
  return dbValueVar

def utcTime():
  utcTimestr = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
  return utcTimestr

def mainLogger(activity, ifWrite):
      log = "[" + utcTime() + "] " + "[" + activity + "]"
      if ifWrite:
        writeProc = open("log.txt", "a")
        writeProc.write(log + "\n")
        writeProc.close()
      print(log)
      return None

channelEmbed=discord.Embed(title="You posted a bad channel!", description="The channel you sent is known to be a bad clipper who harms talents through their focus on clickbait, bad metadata, mistranslation, or doxxing. Please consider looking for clips elsewhere.", color=0xcc0000)
channelEmbed.set_author(name="AntiBadSubs", icon_url="https://i.vgy.me/wWzvwy.png")
channelEmbed.set_thumbnail(url="https://i.vgy.me/qLhqkK.png")

videoEmbed=discord.Embed(title="You posted a bad sub!", description="The video you sent is from a channel that is known to be a bad clipper who harms talents through their focus on clickbait, bad metadata, mistranslation, or doxxing. Please consider looking for clips elsewhere.", color=0xcc0000)
videoEmbed.set_author(name="AntiBadSubs", icon_url="https://i.vgy.me/wWzvwy.png")
videoEmbed.set_thumbnail(url="https://i.vgy.me/qLhqkK.png")

aboutEmbed=discord.Embed(title=absVersion, description="This bot will automatically remove messages containing links to videos from known bad subbers and clippers, as well as their channel links.", color=0xcc0000)
aboutEmbed.set_thumbnail(url="https://i.vgy.me/tWyCbF.png")
aboutEmbed.add_field(name=chr(173), value="[The bot is available on GitHub.](https://github.com/Madekuji/AntiBadSubs)", inline=True)

inviteEmbed=discord.Embed(title="Invite this bot to your server!", url="https://discord.com/api/oauth2/authorize?client_id=896309801875812362&permissions=429497117696&scope=bot", color=0xcc0000)
inviteEmbed.set_author(name="AntiBadSubs Bot")
inviteEmbed.set_thumbnail(url="https://i.vgy.me/tWyCbF.png")
inviteEmbed.set_footer(text=absVersion)

helpEmbed=discord.Embed(title="List of Commands", description="All commands start with the prefix `abs!`", color=0xcc0000)
helpEmbed.set_author(name="AntiBadSubs", icon_url="https://i.vgy.me/wWzvwy.png")
helpEmbed.add_field(name="about", value="Get more info about the bot.", inline=False)
helpEmbed.add_field(name="list", value="Get the global spreadsheet of channels that are blacklisted.", inline=False)
helpEmbed.add_field(name="invite", value="Get the invite link of the bot to invite it to your server. Please note that the bot only has a limit of 100 servers and is undergoing testing phase.", inline=False)
helpEmbed.set_footer(text=absVersion)

statsEmbed=discord.Embed(title="Bot Stats", color=0xcc0000)
statsEmbed.set_author(name="AntiBadSubs", icon_url="https://i.vgy.me/wWzvwy.png")
statsEmbed.add_field(name="Name", value="Servers invited to: \nTotal links deleted: \nChannel links deleted: \nVideo links deleted: ", inline=True)
statsEmbed.set_footer(text=absVersion)

@client.event
async def on_ready():
    mainLogger(f"We have logged in as {client.user}", True)


@client.event
async def on_message(message: discord.Message):
    
    if message.author.bot:
        return

    dcMessage = message.content
    dcServer = message.guild.name
    dcChannel = message.channel.name

    def dcLogger(activity, ifChannel, ifMessage, ifWrite):
      if ifChannel and ifMessage:
        log = "[" + utcTime() + "] " + "[" + activity + "] " + "[" + dcServer + ": " + dcChannel + "] " + dcMessage
      elif ifChannel:
        log = "[" + utcTime() + "] " + "[" + activity + "] " + "[" + dcServer + ": " + dcChannel + "]"
      else:
        log = "[" + utcTime() + "] " + "[" + activity + "]"
      if ifWrite:
        writeProc = open("log.txt", "a")
        writeProc.write(log + "\n")
        writeProc.close()
      print(log)
      return None

    dcLogger("Message Read", True, True, False)

    if any(x in dcMessage for x in database):
        await message.delete()
        dcLogger("Message Deleted", True, True, True)
        channelEmbed.set_footer(text=("Deleted " + str(incrementDB(0)) + " bad links so far."))
        incrementDB(1)
        dcLogger("Database Updated", False, False, True)
        await message.channel.send(embed = channelEmbed)
        dcLogger("Embed Sent - Channel Trigger", True, False, True)

    embed: discord.Embed
    for embed in message.embeds:

        dcEmbed = embed.author.url
        
        if dcEmbed:
          if any(x in dcEmbed for x in database):
              await message.delete()
              dcLogger("Message Deleted", True, True, True)
              videoEmbed.set_footer(text=("Deleted " + str(incrementDB(0)) + " bad links so far."))
              incrementDB(2)
              dcLogger("Database Updated", False, False, True)
              await message.channel.send(embed = videoEmbed)
              dcLogger("Embed Sent - Video Trigger", True, False, True)
    
    if dcMessage.startswith('abs!about'):
      await message.channel.send(embed = aboutEmbed)
      dcLogger("abs!about Triggered", True, False, False)

    if dcMessage.startswith('abs!list'):
      await message.channel.send("<https://docs.google.com/spreadsheets/d/1GF_QC5XpvUgFAYqvUTvLyaf3SwzPHpSiQEJwz6hTo_c/edit?usp=sharing>")
      dcLogger("abs!list Triggered", True, False, False)

    if dcMessage.startswith('abs!invite'):
      inviteEmbed.set_footer(text=("Bot server limit: " + str(len(client.guilds)) + "/100 • ") + absVersion)
      await message.channel.send(embed = inviteEmbed)
      dcLogger("abs!invite Triggered", True, False, False)

    if dcMessage.startswith('abs!activity'):
      await client.change_presence(activity=discord.Game(name='abs!help'))
      await message.channel.send("Activity updated.")
      dcLogger("abs!activity Triggered", True, False, True)

    if dcMessage.startswith('abs!help'):
      await message.channel.send(embed = helpEmbed)
      dcLogger("abs!help Triggered", True, False, False)
    
    if dcMessage.startswith('abs!stats'):
      statsEmbed.add_field(name="Value", value=(str(len(client.guilds)) + "\n" + str(returnDB(0)) + "\n" + str(returnDB(1)) + "\n" + str(returnDB(2))), inline=True)
      await message.channel.send(embed = statsEmbed)
      dcLogger("abs!stats Triggered", True, False, False)


client.run(os.getenv('TOKEN'))