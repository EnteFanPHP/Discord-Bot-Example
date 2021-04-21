import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.command()

async def Help(ctx):

    embed = discord.Embed(title="Cosmos Help")

    embed.add_field(name="Bot Prefix:", value="?")

    embed.set_footer(text="Help for @"f"{ctx.author}")

    await ctx.send(embed=embed)

@bot.event

async def on_ready():

    print('Bot is Running')

bot.run("TOKEN")
