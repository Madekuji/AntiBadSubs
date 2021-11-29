# Original code from https://github.com/Ryu1845/delete_otak
# Modified by Madekuji-san

from keep_alive import keep_alive

import os

import discord

client = discord.Client()

database = ['OtakMoriTranslationsVTubers', 'UCF4-I8ZQL6Aa-iHfdz-B9KQ', 'UCizN2tVLNcwP67bAHlVRg1Q']	


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    
    if message.author.bot:
        return

    dcMessage = message.content

    if any(x in dcMessage for x in database):
        await message.delete()
        await message.channel.send('https://i.vgy.me/qLhqkK.png')

    embed: discord.Embed
    for embed in message.embeds:

        dcEmbed = embed.author.url

        if any(x in dcEmbed for x in database):
            await message.delete()
            await message.channel.send('https://i.vgy.me/qLhqkK.png')
    
    if dcMessage.startswith('abs!about'):
      embedVar = discord.Embed(title = "AntiBadSubs Bot", description = "Remove all known bad subbers.")
      await message.channel.send(embed = embedVar)

    if dcMessage.startswith('abs!list'):
      await message.channel.send("<https://docs.google.com/spreadsheets/d/1GF_QC5XpvUgFAYqvUTvLyaf3SwzPHpSiQEJwz6hTo_c/edit?usp=sharing>")

    if dcMessage.startswith('abs!invite'):
      await message.channel.send("<https://discord.com/api/oauth2/authorize?client_id=896309801875812362&permissions=532576462912&scope=bot>")


keep_alive()
client.run(os.environ['TOKEN'])