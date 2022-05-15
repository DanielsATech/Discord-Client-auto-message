import discord
from discord.ext import tasks, commands

client = discord.Client()



@tasks.loop(hours=7)
async def sendmessage():

    channel = client.get_channel(ID_HERE)
    
    await channel.send("Message")

    
    
    

@client.event
async def on_ready():
    
    sendmessage.start()

client.run('TOKEN', bot=False)