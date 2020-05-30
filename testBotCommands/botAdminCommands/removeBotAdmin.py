from testBotCommands.botAdminCommands.getAdmins import getAdmins

import json


async def removeBotAdmin(ctx, user):
    admins, adminJson = getAdmins()

    if user.id in admins:
        for a in adminJson['testBotAdmins']:
            if a['ID'] == user.id:
                adminJson['testBotAdmins'].remove(a)

        json.dump(adminJson, open('data/admins/testBotAdmins.json', 'w'), indent=2)

        await ctx.send("Removed {} as an administrator to TestingBot".format(user.name))
    else:
        await ctx.send("{} is not an administrator to TestingBot".format(user.name))
