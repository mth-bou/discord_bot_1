import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()
clientID = 901015340983660546
permissions_integer = 8
url = f"https://discordapp.com/oauth2/authorize?client_id={clientID}&scope=bot&permissions={permissions_integer}"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


if __name__ == '__main__':
    client.run(os.getenv('BOT_TOKEN'))

