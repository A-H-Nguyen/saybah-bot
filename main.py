import asyncio
import discord
import os
# import youtube_dl # currently youtube_dl has some bugs so use yt_dlp instead
import yt_dlp as youtube_dl

from discord.ext import commands,tasks
from dotenv import load_dotenv

load_dotenv()
__TOKEN__ = os.getenv("token") # Get the API token from the .env file.

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

queue = []

youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
    
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename



# Commands:
@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if (ctx.author.voice): # If the person is in a channel
        channel = ctx.author.voice.channel
        await channel.connect()
    else: #But is (s)he isn't in a voice channel
        await ctx.send("You must be in a voice channel first so I can join it.")

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("I'm not connected to a voice channel.")

@bot.command(name='play', help='To play a youtube link')
async def play(ctx,url):
    server = ctx.message.guild
    voice_channel = server.voice_client
    if not voice_channel or not server:
        ctx.send("The bot is not connected to a voice channel.")
        return

    filename = await YTDLSource.from_url(url, loop=bot.loop)
    global queue
    queue.append(filename)

    async with ctx.typing():    
        if len(queue) != 1:            
            await ctx.send('{} added to queue'.format(filename))
        await play_song(ctx, voice_channel)

async def play_song(ctx, vc):
    global queue
     
    while len(queue) > 0:
        curr_song = queue[0]
        await ctx.send('**Now playing:** {}'.format(curr_song))
        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=curr_song))

        queue.pop(0)

    # for song in queue:
    #     await ctx.send('**Now playing:** {}'.format(song))

    # try :
    #     server = ctx.message.guild
    #     voice_channel = server.voice_client
    #     async with ctx.typing():
    #         filename = await YTDLSource.from_url(url, loop=bot.loop)
    #         voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename))
    #     await ctx.send('**Now playing:** {}'.format(filename))
    # except:
    #     await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    # else:
    #     await ctx.send("The bot was not playing anything before this. Use play command")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    # else:
    #     await ctx.send("The bot is not playing anything at the moment.")

@bot.command()
async def hello(ctx):
    text = "「―――問おう。貴方は私のマスターか」."
    await ctx.send(text)



if __name__ == "__main__" :
    bot.run(__TOKEN__)