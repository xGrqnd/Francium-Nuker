import requests
import json

def Friend_Remover(token):
    guilds = requests.get('https://discord.com/api/v8/users/@me/relationships', headers = {'Authorization': token}, verify = False)
    json = guilds.json()


    x = 0
    for friends in json:
        print(friends)
        print()
        json2 = json[x]
        id1 = json2['id']

        try:
            requests.delete('https://discord.com/api/v8/users/@me/relationships/' + id1, headers = {'Authorization': token}, verify = False)

        except:
            print('Failed to Remove friend #' + str(x))
        x = x + 1
    

