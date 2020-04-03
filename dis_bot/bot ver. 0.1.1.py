#B0T Даныло


import discord
import asyncio

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
client = discord.Client()
bot_token = "NjAyODM4OTI3MDEwNjkzMTIx.XTdXNg.Lnk4HW_ArNqSoQypC77TVht_VkY"
invite = "https://discordapp.com/oauth2/authorize?&client_id=602838927010693121&scope=bot&permissions=0"


#discord.opus.load_opus('opus')  #  Bot's voice?



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await client.send_message(message.channel, greeting)

    if message.content.startswith('!list'):
        await client.send_message(message.channel, output_roles())

    if message.content.startswith('!addlist'):
        role_name = message.content.split()
        role = role_name[1]
        name = role_name[2]
        add_list(role,name)
        text = role + ' ' + name +  ' succesfully added'
        await client.send_message(message.channel, text)

    if message.content.startswith('!play'):
       # discord.opus.load_opus()
        name = message.content.split()
        name.pop(0)
        name = ' '.join(name)
        channel_name = message.author.voice.voice_channel
        print("NAME = ", name)

        vc = await client.join_voice_channel(channel_name)
        #source = await discord.FFmpegOpusAudio.from_probe(name)
        #vc.play(source)

        vc.play(discord.FFmpegPCMAudio(name), after=lambda e: print('done', e))

        #except:
            #await client.send_message(message.channel, 'Join the voice channel')            

    if message.content.startswith('!stop'):
        try:
            vc.stop()
            await client.leave_voice_channel(channel_name)
            await client.send_message(message.channel, 'Music is stopped')

        except:
            await client.send_message(message.channel, 'There is no music')
            
           

    





client.run(bot_token)



        
