import os
import json

from datetime import datetime


def log(command, ctx):
    if os.path.getsize('logs/commandLogs.json') > 2:
        log = json.load(open('logs/commandLogs.json', 'r'))
    else:
        log = {'commandLog': []}

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
