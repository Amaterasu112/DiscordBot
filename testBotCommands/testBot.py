import discord
from discord.ext import commands
from generalFunctions import Logging
from generalFunctions.CheckUserInput import checkUserInput
from generalFunctions.CheckAdmin import checkAdmin
import numpy as np

import os
import json


class Testbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.admins = []
        self.adminJson = {}

        self.reloadAdmins()

        if os.path.getsize('data/admins/testBotAdmins.json') > 2:
            self.adminJson = json.load(open('data/admins/testBotAdmins.json', 'r'))
        else:
            self.adminJson = {'testBotAdmins': []}

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            Logging.errorLog(error, ctx)
            await ctx.send('I could not find that user')


    @commands.command(name="ping")
    async def ping(self, ctx):
        Logging.commandLog("ping", ctx)
        await ctx.send('pong')

    @commands.command(name="changeprefix")
    async def changePrefix(self, ctx, arg):
        Logging.commandLog("changeprefix", ctx)

        if checkAdmin(ctx):
            self.bot.command_prefix = arg
            await ctx.send("Prefix changed to", arg)
        else:
            await ctx.send("Nice try")

    @commands.command(name="addbotadmin")
    async def addBotAdmin(self, ctx, user: discord.Member):
        Logging.commandLog("addbotadmin", ctx)

        self.reloadAdmins()

        if checkAdmin(ctx):
            if user.id not in self.admins:
                self.adminJson['testBotAdmins'].append({
                    'name': user.name,
                    'ID': user.id
                })

                json.dump(self.adminJson, open('data/admins/testBotAdmins.json', 'w'), indent=2)

                await ctx.send("Added {} as an administrator to TestingBot".format(user.name))
            else:
                await ctx.send("{} already an administrator to TestingBot".format(user.name))

    @commands.command(name="removebotadmin")
    async def removeBotAdmin(self, ctx, user: discord.Member):
        Logging.commandLog("removebotadmin", ctx)

        self.reloadAdmins()

        if checkAdmin(ctx):
            if user.id in self.admins:
                for a in self.adminJson['testBotAdmins']:
                    if a['ID'] == user.id:
                        self.adminJson['testBotAdmins'].remove(a)

                json.dump(self.adminJson, open('data/admins/testBotAdmins.json', 'w'), indent=2)
                self.reloadAdmins()

                await ctx.send("Removed {} as an administrator to TestingBot".format(user.name))
            else:
                await ctx.send("{} is not an administrator to TestingBot".format(user.name))

    @commands.command(name="sendcookies")
    async def sendCookies(self, ctx, user: discord.Member = None):
        Logging.commandLog("sendcookies", ctx)

        if checkUserInput(ctx, user, "Please add a valid User ID or Mention who you want to send this message to"):
            if user.dm_channel is None:
                channel = await user.create_dm()
            else:
                channel = await user.dm_channel

            await channel.send("🍪")

    @commands.command(name="cleardms")
    async def clearDMs(self, ctx, userId):
        Logging.commandLog("cleardms", ctx)

        user = self.bot.get_user(int(userId))
        if checkAdmin(ctx):
            print(user.name)
            if user.dm_channel is None:
                channel = await user.create_dm()
            else:
                channel = await user.dm_channel

            messages = await channel.history().flatten()

            if len(messages) < 1:
                await ctx.send("No Dms found")
            else:
                for message in messages:
                    await message.delete()
                await ctx.send("Deleted all found Dms")

    def reloadAdmins(self):
        self.adminJson = json.load(open('data/admins/testBotAdmins.json', 'r'))

        for a in self.adminJson['testBotAdmins']:
            self.admins.append(a['ID'])
