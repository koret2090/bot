#B0T Даныло



#############################
import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import ffmpeg
import youtube_dl
import os

# Commands
# Roles and members
def output(f = 'RoleName'):
    f = open(f,'r')
    text = ''
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
client = commands.Bot(command_prefix = '?')
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

#Into the chat
@client.command(pass_context = True)
async def vchat(ctx):
    await ctx.send('!vchat_<num>\n 1) Гусь \n 2) Гусь-гидра \n 3) Тукан \n 4) Дядя Богдан')

@client.command(pass_context = True)
async def vchat_1(ctx):
    await ctx.send(output('gus'))

@client.command(pass_context = True)
async def vchat_2(ctx):
    await ctx.send(output('gus_hidra'))

@client.command(pass_context = True)
async def vchat_3(ctx):
    await ctx.send(output('tukan'))

@client.command(pass_context = True)
async def vchat_4(ctx):
    await ctx.send(output('uncle_bogdan'))

# List of file members
@client.command(pass_context = True)
async def list(ctx):
    await ctx.send(output())

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
    
    if nick.activity == None:
        await ctx.send(str(nick)[:-5] + ' just chills po kaify')
    else:
        await ctx.send(str(nick)[:-5] +"'s activity: " +  str(nick.activity.type)[13:] + ' ' +str(nick.activity.name))
    
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
async def play(ctx, *, name):
    '''play <name> - play local music'''
   
    channel_name = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    # Повтор из-за бага
    '''
    if voice and voice.is_connected():
        await voice.move_to(channel_name)
    else:
        voice = await channel_name.connect()

    await voice.disconnect()
    '''

    if voice and voice.is_connected():
        await voice.move_to(channel_name)
    else:
            voice = await channel_name.connect()          

    sourcee = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(
        executable = '/Users/Danya/Downloads/ffmpeg/bin/ffmpeg',
        source = name))
    ctx.voice_client.play(sourcee)
    '''
    if ctx.voice_client.is_playing():
        await ctx.send(name + ' added in the queue')
        client.wait_for(ctx.voice_client.play(sourcee)) 
        
                
    else:
        client.wait_for(ctx.voice_client.play(sourcee))          
    '''

@client.command(pass_context = True)
async def playy(ctx, url : str):

    channel_name = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)


    if voice and voice.is_connected():
        await voice.move_to(channel_name)
    else:
        voice = await channel_name.connect()

    await voice.disconnect()
    
    if voice and voice.is_connected():
        await voice.move_to(channel_name)
    else:
            voice = await channel_name.connect() 

    song_there = os.path.isfile("song.webm")


    try:
        if song_there:
            os.remove("song.webm")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            print("Downloading audio now\n")
            ydl.download([url])
        except:
            pass
    
    print('DIO')

    for file in os.listdir("./"):
        if file.endswith(".webm"):
            name = file
            print("Renamed File: ", file, '\n')
            os.rename(file, "song.webm")

    sourcee = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(
        executable = '/Users/Danya/Downloads/ffmpeg/bin/ffmpeg',
        source = 'song.webm'))
    ctx.voice_client.play(sourcee)


@client.command(pass_context = True)
async def stop(ctx):
    ctx.voice_client.stop()
    await ctx.send('Music is stopped')




client.run(client_token)



        
