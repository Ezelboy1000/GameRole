#!/bin/env python3
import discord
from discord.utils import get
import asyncio

############
# Settings #
############

BotToken = '<Your BOT TOKEN here>'
PlayingGame = "<Name of game>"
PlayingRole = "<Name of role>"

############

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="this server!"))

@client.event
async def on_member_update(before,after):
    guild = after.guild
    role = get(guild.roles, name=PlayingRole)
    for Bactivity in before.activities:
        for Aactivity in after.activities:
            if PlayingGame in str(Aactivity):
                if PlayingGame in str(Bactivity):
                    return
                else:
                    print("Adding " + str(role) + " to " + after.name)
                    await after.add_roles(role)
            if PlayingGame in str(Bactivity):
                if PlayingGame in str(Aactivity):
                    return
                else:
                    print("Removing " + str(role) + " from " + after.name)
                    await after.remove_roles(role)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('k!help'):
        await message.channel.send('This is a bot written by Ezel#1995 to automagically add and remove people to the "' + PlayingRole + '" role when they start playing ' + PlayingGame + '!')

client.run(BotToken)