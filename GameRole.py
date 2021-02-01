#!/usr/bin/env python3
import discord
from discord.utils import get
import asyncio

############
# Settings #
############

BotToken = '<Your BOT TOKEN here>'
Prefix = "gr!"
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
    if PlayingGame in str(after.activities):
        if PlayingGame in str(before.activities):
            return
        else:
            print("Adding " + str(role) + " to " + after.name)
            await after.add_roles(role)
    if PlayingGame in str(before.activities):
        if PlayingGame in str(after.activities):
            return
        else:
            print("Removing " + str(role) + " from " + after.name)
            await after.remove_roles(role)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(Prefix + 'help'):
        await message.channel.send('This is a bot written by Ezel#1995 to automagically add and remove people to the "' + PlayingRole + '" role when they start playing ' + PlayingGame + '!')

client.run(BotToken)
