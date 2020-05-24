import discord
from discord.ext import commands
from generalFunctions import logging

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
                self.adminJson['testBotAdmins'].append({
                    'name': member.name,
                    'ID': member.id
                })

                json.dump(self.adminJson, open('data/admins/testBotAdmins.json', 'w'), indent=2)

                await ctx.send("Added {} as an administrator to TestingBot".format(member.name))
            else:
                await ctx.send("{} already an administrator to TestingBot".format(member.name))

    @commands.command(name="removebotadmin")
    async def removeBotAdmin(self, ctx, member: discord.Member):
        logging.log("removebotadmin", ctx)

        self.reloadAdmins()

        if ctx.author.id in self.admins:
            if member.id in self.admins:
                for a in self.adminJson['testBotAdmins']:
                    if a['ID'] == member.id:
                        self.adminJson['testBotAdmins'].remove(a)

                json.dump(self.adminJson, open('data/admins/testBotAdmins.json', 'w'), indent=2)
                self.reloadAdmins()

                await ctx.send("Removed {} as an administrator to TestingBot".format(member.name))
            else:
                await ctx.send("{} is not an administrator to TestingBot".format(member.name))

    def reloadAdmins(self):
        self.adminJson = json.load(open('data/admins/testBotAdmins.json', 'r'))

        for a in self.adminJson['testBotAdmins']:
            self.admins.append(a['ID'])
