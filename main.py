import discord
from discord.ext import commands
from myserver import server_on

TOKEN = "MTUwMDM4MDY1OTcyNDU4NzAzOA.Gi2SM4.467OQjGAWYO_q-KtfmeDlYGJvFxhmlVK9a_iQ8" # ganti dengan token bot anda

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot {} online'.format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Jangan lupa subscribenya ya :)'.format(ctx.author.name.title()))

server_on()
bot.run(os.getenv("TOKEN"))