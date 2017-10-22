token = ""
# Your token is required for this bot to work.

import discord
import logging
import asyncio
# Required imports for this bot to work.

client = discord.Client()
# Defines the discord client.

name = "EmbedBot"
prefix = "-"
# Some definitions for this bots own usage.

logging.basicConfig(level=logging.INFO)
# Sets the logging level.

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=prefix + "e"))
    print("-------------")
    print(name + ". Running as " + client.user.name + " with the ID " + client.user.id + ".")
    print("-------------")
# Shows message on boot and sets game.

async def ez(message):
    try:
        await client.delete_message(message)
    except:
        pass
    InitMsg = await client.send_message(message.channel, "What would you like the title of the embed to be? If you do not want one, type X.")
    title = await client.wait_for_message(author=message.author, timeout=60)
    try:
        await client.delete_message(title)
    except:
        pass
    await client.edit_message(InitMsg, "What do you want the description to be? If you do not want one, type X.")
    desc = await client.wait_for_message(author=message.author, timeout=60)
    try:
        await client.delete_message(desc)
    except:
        pass
    await client.edit_message(InitMsg, "What do you want the colour of the embed to be? Type white, blue, orange or red. If you want black, type X.")
    colour = await client.wait_for_message(author=message.author, timeout=60)
    try:
        await client.delete_message(colour)
    except:
        pass
    await client.edit_message(InitMsg, "What do you want the thumbnail picture to be? If you do not want one, press X. If you do want one, type the URL.")
    url = await client.wait_for_message(author=message.author, timeout=60)
    try:
        await client.delete_message(url)
    except:
        pass
    title = title.content
    desc = desc.content
    colour = colour.content.lower()
    url = url.content
    if title.lower() == "x":
        title = None
    if desc.lower() == "x":
        desc = None
    if colour == "x":
        colour = None
    if url.lower() == "x":
        url = None
    if colour == None:
        clr = 0x000000
    elif colour == "white":
        clr = 0xFFFFFF
    elif colour == "blue":
        clr = 0x0000FF
    elif colour == "red":
        clr = 0xFF0000
    elif colour == "orange":
        clr = 0xFFA500
    else:
        clr = 0x000000
    if url == None:
        e = discord.Embed(title=title, description=desc, colour=clr)
    else:
        e = discord.Embed(title=title, description=desc, colour=clr).set_thumbnail(url=url)
    await client.send_message(message.channel, embed=e)
    try:
        await client.delete_message(InitMsg)
    except:
        pass

@client.event
async def on_message(message):
    if message.content.startswith(prefix):

        cmd = message.content.lstrip(prefix).split(' ')[0]
        if cmd == "e":
            print(message.author.name + " (" + message.author.id + "): \n" + message.content)
            try:
                await ez(message)
            except Exception as err:
                try:
                    await client.send_message(message.channel, message.author.mention + "```" + str(err) + "```")
                except:
                    pass
        # Chooses where your message goes.

client.run(token)
# Starts the bot.
