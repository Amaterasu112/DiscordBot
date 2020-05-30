from testBotCommands.botAdminCommands.getAdmins import getAdmins

import json

async def addBotAdmin(ctx, user):
    admins, adminJson = getAdmins()

    if user.id not in admins:
        adminJson['testBotAdmins'].append({
            'name': user.name,
            'ID': user.id
        })

        json.dump(adminJson, open('data/admins/testBotAdmins.json', 'w'), indent=2)

        await ctx.send("Added {} as an administrator to TestingBot".format(user.name))
    else:
        await ctx.send("{} already an administrator to TestingBot".format(user.name))
