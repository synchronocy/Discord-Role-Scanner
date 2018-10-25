#!usr/bin/env python3
# Date: 10-13-18, Oct ~ 13th 2018 | Synchronocy
# Project: Discord Role Scanner
# IDLE Python 3.6 64-bit

import discord
import os
import asyncio
import random 
import datetime

now = datetime.datetime.now()
YOUR_TOKEN = "tokenhere"
lists = []
client = discord.Client()

@client.event
async def on_ready():
    counter = -1
    print('Logged in as')
    print('User: '+str(client.user.name))
    print('UserID: '+str(client.user.id))
    print('Email: '+str(client.email))
    print('Member of: ')
    for x in client.servers:
        counter += 1
        print(str(counter)+'. ( '+str(x.id)+' ) '+str(x)+'\n')
        lists.append(x.id)
    print('Date: '+str(now.day)+'-'+str(now.month)+'-'+str(now.year))
    print('------------')
    a = int(input('Select your server you wish to Scan.\n:'))
    SERVER = lists[int(a)]
    await main(SERVER)

async def main(SERVER):
    for role in client.get_server(SERVER).roles:
        print('( '+str(role.id)+' ) '+str(role)+'\n')
        
        
client.run(YOUR_TOKEN, bot=False)
