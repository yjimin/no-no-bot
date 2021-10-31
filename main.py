import discord
from csv import reader

client = discord.Client()

member_list = {}


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
async def on_member_join(member):
    member_list[member.id] = 0
    await member.send('Welcome ' + str(member.user.username) + "!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_message = message.content

    for i in swearList:
        if i.casefold() in user_message.casefold():
            member_list[message.author.username] += 1
            if member_list[message.author].username >= 3:
                await message.author.kick("Too many bad words for you. Say goodbye :)")
            else:
                await message.channel.send('Thats a bad word. Dont do that. Or else >:(')
        

client.run('OTA0MDkwMzE5OTI5Mzc2Nzgw.YX2duQ.lm949QK-q7IDD_ghY7rJ9OiWNTI')