import os
import json

def getAdmins():
    admins = []

    if os.path.getsize('data/admins/testBotAdmins.json') > 2:
        adminJson = json.load(open('data/admins/testBotAdmins.json', 'r'))
    else:
        adminJson = {'testBotAdmins': []}

    for a in adminJson['testBotAdmins']:
        admins.append(a['ID'])

    return admins, adminJson