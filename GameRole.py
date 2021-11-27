#!/usr/bin/env python3
import discord
from discord.utils import get
import asyncio

############
# Settings #
############

BotToken = 'Your BOT TOKEN here'
Prefix = "gr!"
PlayingGame = ["Game1", "Game2", "Game3"]
PlayingRole = "Role name"

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
    if any(str(after.activities) in search for search in PlayingGame):
        if any(str(before.activities) in search for search in PlayingGame):
            return
        else:
            print("Adding " + str(role) + " to " + after.name)
            await after.add_roles(role)
    if any(str(before.activities) in search for search in PlayingGame):
        if any(str(after.activities) in search for search in PlayingGame):
            return
        else:
            print("Removing " + str(role) + " from " + after.name)
            await after.remove_roles(role)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(Prefix + 'help'):
        GameList=", ".join(map(str,PlayingGame))
        await message.channel.send('This is a bot written by Ezel#1995 to automagically add and remove people to the "' + PlayingRole + '" role when they start playing ' + GameList + '!')

client.run(BotToken)
