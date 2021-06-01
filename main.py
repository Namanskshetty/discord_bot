import os
import discord
from discord.ext import commands
import typing
import emoji
from replit import db
from keep_alive import keep_alive
import smtplib
import emoji
import requests
import json
import random


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data= json.loads(response.text)
  quote=json_data[0]['q'] + " -" + json_data[0]['a']
    
  return(quote)

#############################################
print(discord.__version__)
#############################################
client = commands.Bot(command_prefix='.')
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_member_join(member):
  print(f'(member) has joined server.')

@client.event
async def on_member_remove(member):
  print(f'(member) has left server.')


@client.command()
async def hi(ctx):
  await ctx.send('Hello :grinning: this is your bot sevenr~ designed for The Den Of Arceus! :smiling_face_with_3_hearts:  ')

@client.command()
async def ping(ctx):
  await ctx.send(f'ping  {round(client.latency*1000)}ms')

@client.command()
async def mail(ctx):

  mail=os.environ['mail']
  passw=os.environ['password']
  nam=os.environ["naman"]
  amit=os.environ["amit"]
  rak=os.environ["rak"]
  man=os.environ['man']
  print(mail,passw)
  words=(amit ,nam ,rak ,man)
  for word in words:
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(mail,passw)
    server.sendmail("sevenrbot@gmail.com",word,"hello  this is your bot please join discord and play GTA")
    server.quit()
  await ctx.send("Mail sent successfully :thumbsup: ")
###################################quotes###########################



@client.command()
async def nam(ctx):
  quote= get_quote()
  await ctx.send(quote)

@client.command()
async def write(ctx,amount):
  i=1
  limit=int(amount)
  while i < limit:
    await ctx.send("Write!!! :face_with_raised_eyebrow: ")
    i=i+1
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)
#######################music-try#########

  
@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('py'):
    client.load_extension(f'cogs.{filename[:-3]}')


keep_alive()

client.run(os.environ['TOKEN'])
