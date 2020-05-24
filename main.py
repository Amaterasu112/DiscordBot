# import discord
from discord.ext import commands
from testBotCommands.testBot import Testbot

import json

botName = "TestingBot"
token = ""
for t in json.load(open('tokens/token.json'))['tokens']:
    if botName in t['botName']:
        token = t['token']

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("logged on as {0}".format(bot.user))

    if botName == "TestingBot":
        bot.add_cog(Testbot(bot))
        print("Running", botName)

bot.run(token)
