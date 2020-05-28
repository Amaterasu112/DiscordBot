import os
import json

from datetime import datetime


def commandLog(command, ctx):
    log = getJsonLog('commandLog')

    now = datetime.now().strftime("%H:%M:%S, %d/%m/%Y")

    log['commandLog'].append({
        'commandName': command,
        'time': now,
        'command': ctx.message.content,
        'server': ctx.guild.name,
        'serverID': ctx.guild.id,
        'channel': ctx.message.channel.name,
        'channelID': ctx.message.channel.id,
        'author': ctx.author.name,
        'authorID': ctx.author.id
    })
    json.dump(log, open('logs/commandLogs.json', 'w'), indent=2)
    print(command, " command logged at", now)


def errorLog(error, ctx):
    log = getJsonLog('errorLog')

    now = datetime.now().strftime("%H:%M:%S, %d/%m/%Y")

    log['errorLog'].append({
        'command': ctx.message.content,
        'time': now,
        'error': str(error)
    })
    json.dump(log, open('logs/errorLogs.json', 'w'), indent=2)
    print(error, " error logged at", now)


def getJsonLog(command):
    log = {command: []}
    if os.path.exists('logs/' + command + 's.json'):
        if os.path.getsize('logs/' + command + 's.json') > 2:
            log = json.load(open('logs/' + command + 's.json', 'r'))
    else:
        log = {command: []}

    return log
