import discord
from discord.ext import commands
import pandas as pd
import random

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("IT'S YA GORL, CRASH")

@client.command()
async def hi(ctx):
    await ctx.send("Hello")

@client.command()
async def ping(ctx):
    await ctx.send("pong!")

@client.command()
async def jokes(ctx):
    jokes_df = pd.read_csv("qa_jokes.csv")
    numb = random.randint(0, len(jokes_df.index))
    question = jokes_df.iloc[numb, 0]
    answer = jokes_df.iloc[numb, 1]
    text = question + "->" + answer
    await ctx.send(text)

@client.command()
async def quotes(ctx):
    quotes_df = pd.read_csv("QUOTE.csv")
    numb = random.randint(0, len(quotes_df.index))
    author = quotes_df.iloc[numb, 0]
    quote = quotes_df.iloc[numb, 1]
    text = author + "->" + quote
    await ctx.send(text)

client.run("ODM1OTI1NjY3OTYzMDc2NjY0.YIWicQ._08kv-ygWkt6h0N6-41TvEB5shk")