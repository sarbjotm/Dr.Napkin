import discord
import asyncio
import datetime 
import os
import random
from google_trans_new import google_translator  
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '-')
channel = client.get_channel(744817323973804093)

translator = google_translator()  
@client.event
async def on_ready():
    print("Bot is Ready")
    drinkwater.start()
    goodmorning.start()

@tasks.loop(minutes=90)
async def drinkwater():
    timenow = str(datetime.datetime.now().time())
    timenow = timenow.split(':')
    print(int(timenow[0]))
    if ((int(timenow[0]) >= 17) or (int(timenow[0]) <= 8)):
        channel = client.get_channel(744817323973804093)
        await channel.send("Make sure to drink water Dodos!")

@tasks.loop(hours = 2)
async def goodmorning():
    timenow = str(datetime.datetime.now().time())
    timenow = timenow.split(':')
    print(int(timenow[0]))
    if ((int(timenow[0]) == 17)):
        await channel.send("Good Morning Dodos!")
    elif((int(timenow[0]) == 8)):
        await channel.send("Good Night!")


@client.event
async def on_message(message):
    if message.content.startswith('Hello'):
        await message.channel.send(f"{message.author.mention} Hello!")

@client.event
async def on_member_join(member):
    await channel.send(f"Welcome {member.mention}!")

@client.event
async def on_member_leave(member):
    await channel.send(f"Goodbye {member.mention}!")
    


@client.command()
async def translate(ctx,*,sentence):
    translate_text = translator.translate(sentence,lang_tgt='en')  
    await ctx.send(translate_text)


#Blackbox
client.run(os.environ['TOKEN'])