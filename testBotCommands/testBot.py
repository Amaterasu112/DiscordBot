import discord
from discord.ext import commands
from generalFunctions import logging

import os
import json

adminsJson = {}

if os.path.getsize('data/admins/testBotAdmins.json') > 2:
    adminJson = json.load(open('data/admins/testBotAdmins.json', 'r'))
else:
    adminJson = {'testBotAdmins': []}




class Testbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.admins = []

        self.reloadAdmins()

    @commands.command(name="ping")
    async def ping(self, ctx):
        logging.log("ping", ctx)
        await ctx.send('pong')

    @commands.command(name="changeprefix")
    async def changePrefix(self, ctx, arg):
        logging.log("changeprefix", ctx)

        if ctx.author.id in self.admins:
            self.bot.command_prefix = arg
            await ctx.send("Prefix changed to", arg)
        else:
            await ctx.send("Nice try")

    @commands.command(name="addbotadmin")
    async def addBotAdmin(self, ctx, member: discord.Member):
        logging.log("addbotadmin", ctx)

        self.reloadAdmins()

        if ctx.author.id in self.admins:
            if member.id not in self.admins:
                adminJson['testBotAdmins'].append({
                    'name': member.name,
                    'ID': member.id
                })

                json.dump(adminJson, open('data/admins/testBotAdmins.json', 'w'), indent=2)

                await ctx.send("Added {} as an administrator to TestingBot".format(member.name))
            else:
                await ctx.send("{} already an administrator to TestingBot".format(member.name))

    def reloadAdmins(self):
        for a in adminJson['testBotAdmins']:
            self.admins.append(a['ID'])
