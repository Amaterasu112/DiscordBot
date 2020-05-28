import discord
from discord.ext import commands
from generalFunctions import Logging
import numpy as np

import json

class Shitpostingbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="misfortunes")
    async def misfortunes(self, ctx):
        Logging.commandLog("misfortunes", ctx)

        misfortunes = json.load(open('data/misfortunes/misfortunes.json', 'r'))
        misfortune = misfortunes['misfortunes'][np.random.random_integers(0, len(misfortunes['misfortunes']))]['misfortune']
        print(misfortune)

        await ctx.send(misfortune)
