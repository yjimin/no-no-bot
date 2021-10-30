import discord

client = discord.Client()
curse_words = ["fuck", "shit", "cunt"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('hoi peasant')

client.run('OTA0MDkwMzE5OTI5Mzc2Nzgw.YX2duQ.lm949QK-q7IDD_ghY7rJ9OiWNTI')