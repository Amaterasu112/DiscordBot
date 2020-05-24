import discord
import json

client = discord.Client()


@client.event
async def on_ready():
    print("logged on as {0}".format(client))


@client.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(json.load(open('token/token.json'))['token'])
