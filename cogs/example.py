import discord
import youtube_dl
from discord.ext import commands

class example(commands.Cog):
  def __init__(self, client):
    self.client=client

  @commands.Cog.listener()
  async def on_ready(self):
    print("We have logged in ")



  @commands.command()
  async def join(self, ctx):
    destination = ctx.author.voice.channel
    await destination.connect()
    print("joined the channel")

  @commands.command()
  async def stream(self, ctx, *, url):
    player = await YTDLSource.from_url(url, loop=self.client.loop, stream=True)
    ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    await ctx.send('Now playing: {}'.format(player.title))


  @commands.command()
  async def leave(self,ctx):
    await ctx.voice_client.disconnect()
    print("left the channel")
  @commands.command()
  async def tell(self,ctx,*msg):
   
    await ctx.send(msg, tts=True)
    
  
    


def setup(client):
  client.add_cog(example(client))
