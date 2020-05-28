import discord


async def checkUserInput(ctx, user: discord.Member = None, message=""):
    if user:
        return True
    else:
        await ctx.send(message)
