import discord
from discord.ext import commands
from generalFunctions import Logging
import numpy as np

import json

class Shitpostingbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.misfortunes = json.load(open('data/misfortunes/misfortunes.json', 'r'))


    @commands.command(name="misfortunes")
    async def misfortunes(self, ctx):
        Logging.commandLog("misfortunes", ctx)

        # np.random.random_integers(0, len(self.misfortunes['misfortunes']))

        misfortune = self.misfortunes['misfortunes'][np.random.random_integers(0, len(self.misfortunes['misfortunes']) - 1)][
            'misfortune']

        print(misfortune)

        await ctx.send(misfortune)

    @commands.command(name="addmisfortune")
    async def addMisfortune(self, ctx):
        Logging.commandLog("addmisfortune", ctx)

        misfortune = ctx.message.content[len("!addmisfortune "):]

        self.misfortunes['misfortunes'].append({
            'misfortune': misfortune
        })

        json.dump(self.misfortunes, open('data/misfortunes/misfortunes.json', 'w'), indent=2)
        self.misfortunes = json.load(open('data/misfortunes/misfortunes.json', 'r'))

        await ctx.send("Misfortune added")

