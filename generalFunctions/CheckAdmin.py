import json

def checkAdmin(ctx):
    admins = []
    adminJson = json.load(open('data/admins/testBotAdmins.json', 'r'))

    for a in adminJson['testBotAdmins']:
        admins.append(a['ID'])

    if ctx.author.id in admins:
        return True
    else:
        return False
