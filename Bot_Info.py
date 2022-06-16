import discord
import asyncio

def Bot_Info(token):
    client = discord.Client()
    bot_token = token
    
    @client.event
    async def on_ready():
        print('Bot Name')
        print(client.user.name)
        print('Bot ID: ' + str(client.user.id))
        for client in client.guilds:
            print('Connected to server: {}'.format(guild))

    try:
        client.run(bot_token)
    except:
        ERROR = '''
+-------------------+
| INVALID BOT TOKEN |
+-------------------+
'''
        print(ERROR)
        print()


