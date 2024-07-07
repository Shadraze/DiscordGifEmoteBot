import discord
from requests import post
from discord.ext import commands
from discord.file import File
from discord.message import Attachment
from io import BytesIO
from base64 import b64encode

with open('token.txt', 'r') as token_file:
    token = token_file.readline()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='hue', intents=intents)

@bot.command(name="hue")
async def hue(ctx: commands.Context, *msg):
    filename = ""
    for msgstr in msg:
        print(msgstr)
        filename = msgstr
        break
    
    response = post("http://api_v1:8000/gifEmote/" + filename)
    
    if response.status_code == 200:
        emoteBytesIO = BytesIO(response.content)
        emoteFile = File(emoteBytesIO, filename+".gif")
        await ctx.send(file=emoteFile) 
    else:        
        await ctx.send(response.text)

@bot.command(name="take")
async def take(ctx: commands.Context, *msg):
    counter = 0
    for attachment in ctx.message.attachments:
        if attachment.content_type == 'image/gif':
            filename = attachment.filename.removesuffix(".gif")
            print(filename)
            response = post(
                "http://api_v1:8000/gifEmoteTake/", 
                json = {
                    "filename" : filename,
                    "data" : str(b64encode((await(attachment.read()))),"utf-8")
                })
            
            if response.status_code == 200:
                counter += 1

    await ctx.send("I successfully tooketh " + str(counter) + " gifs! :> You can now recall them with 'huehue [gifname]'!")


bot.run(token)  