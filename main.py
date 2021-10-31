import discord
from csv import reader

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    global swearList
    swearList = []
    with open('swearWords.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
                swearList = swearList + row
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_message = message.content

    for i in swearList:
        num_of_cursed_words = 0
        if i.casefold() in user_message.casefold():
            num_of_cursed_words += 1
            if num_of_cursed_words >= 3:
                await message.author.kick("Too many bad words for you. Say goodbye :)")
            else:
                await message.channel.send('Thats a bad word. Dont do that. Or else >:(')
        break

client.run('OTA0MDkwMzE5OTI5Mzc2Nzgw.YX2duQ.lm949QK-q7IDD_ghY7rJ9OiWNTI')