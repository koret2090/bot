#B0T Даныло


import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import ffmpeg
import youtube_dl

#discord.opus.load_opus()
# Commands
# Roles and members
def output_roles():
    text = ''
    f = open('RoleName','r')
    for string in f:
        text += string

    f.close()

    return text

def add_list(role,name):
    f = open('RoleName','a')
    f.write(role + '  | ' + name + '\n')
    f.close()
    


#import requests
greeting = 'Darova ipta, kozhaniy meshok'
client = commands.Bot(command_prefix = '!')
client_token = "NjAyODM4OTI3MDEwNjkzMTIx.XTdXNg.Lnk4HW_ArNqSoQypC77TVht_VkY"
invite = "https://discordapp.com/oauth2/authorize?&client_id=602838927010693121&scope=bot&permissions=0"


#discord.opus.load_opus('opus')  #  Bot's voice?

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    discord.opus.load_opus


# Check the authentification
@client.command(pass_context = True)
async def on_message(message):
    if message.author == client.user:
        return

# Gretting
@client.command(pass_context=True)
async def hello(ctx):
    await ctx.send(greeting)

# List of file members
@client.command(pass_context = True)
async def list(ctx):
    await ctx.send(output_roles())

# Add to the members' file
@client.command(pass_context = True)
async def addlist(ctx, role, *, name):
    print(name)
    add_list(role,name)
    text = role + ' ' + name +  ' succesfully added'
    await ctx.send(text)


# Activity
@client.command(pass_context = True)
async def act(ctx,nick : discord.Member):
    print(nick.roles[1], str(nick)[:-5])   
    if nick.activity == None:
        await ctx.send(str(nick.roles[1]) + ' ' + str(nick)[:-5] + ' just chills po kaify')
    else:
        await ctx.send(str(nick.roles[1]) + ' ' + str(nick)[:-5] +"'s activity: {0.activity}")
    
# Join the channel
@client.command(pass_context = True)
async def join(ctx):
    '''Join the channel'''
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)
    '''
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()
    '''
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send('Ama in da hous')

# Leave the channel
@client.command(pass_context = True)
async def leave(ctx):
    '''Leave the voice channel'''
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    await voice.disconnect()
    await ctx.send('bb')

# Voice
@client.command(pass_context = True)
async def play(ctx):
    '''play <name> - play local music'''
    name = ctx.message.content.split()
    name.pop(0)
    name = ' '.join(name)
    channel_name = ctx.message.author.voice.channel


    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel_name)
    else:
            voice = await channel_name.connect()          

    print("NAME = ", name)
    print("channel_name = ", channel_name)

    sourcee = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(executable = '/Users/Danya/Downloads/ffmpeg/bin/ffmpeg',source = name))
    
    ctx.voice_client.play(sourcee)           


@client.command(pass_context = True)
async def playy(ctx, url : str):
    print("da")
    
@client.command(pass_context = True)
async def stop(ctx):
    ctx.voice_client.stop()
    await ctx.send('Music is stopped')




client.run(client_token)



        
