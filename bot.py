import discord
from discord.ext import commands
import random
import requests



# Define the intents your bot requires
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.voice_states = True

# Create an instance of the bot with the intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Greet
@bot.command()
async def greet(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

@bot.command()
async def join(ctx):
    # Check if the user is in a voice channel
    if ctx.author.voice is None:
        await ctx.send('You are not connected to a voice channel.')
        return

    # Get the voice channel the user is connected to
    channel = ctx.author.voice.channel

    # Join the voice channel
    voice_client = await channel.connect()

    await ctx.send(f'Joined {channel.name}.')

@bot.command()
async def leave(ctx):
    # Check if the bot is connected to a voice channel
    if ctx.voice_client is None:
        await ctx.send('I am not connected to a voice channel.')
        return

    # Disconnect from the voice channel
    await ctx.voice_client.disconnect()

    await ctx.send('Left the voice channel.')
@bot.command()
async def play(ctx, url):
    voice_client = ctx.voice_client
    if not voice_client:
        await ctx.send('I am not connected to a voice channel. Use `join` command first.')
        return

    try:
        voice_channel = voice_client.channel
        voice_client.stop()
        player = discord.FFmpegPCMAudio(url)
        voice_client.play(player)
        await ctx.send(f'Now playing: {url} in {voice_channel}')
    except Exception as e:
        await ctx.send(f'Error: {e}')



@bot.command()
async def joke(ctx):
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    joke = response.json()
    setup = joke['setup']
    punchline = joke['punchline']
    await ctx.send(f"**Joke:** {setup}\n**Punchline:** {punchline}")

# Run the bot
bot.run('MTExMTUyNDE1MjkxOTIwMzg5MQ.GVcFlA.4GZUXoPkyE-QY54OBeqjnhfUFbZ7B7tWC8SrU4')
