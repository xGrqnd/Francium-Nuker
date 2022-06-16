import requests
import json

def Server_Leaver(token):
    guilds = requests.get('https://discord.com/api/v8/users/@me/guilds', headers = {'Authorization': token}, verify = False)
    guildstext = guilds.text
    status = guilds.status_code
    json = guilds.json()

    x = 0
    for guild in json:
        json2 = json[x]
        
        name = json2['name']
        print(name)
        id1 = json2['id']
        print(id1)
        print('Want to leave? y/n')
        leave = input('>>> ')
        print()
        
        if leave == 'y':
            response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/' + id1, headers={'Authorization': token}, verify = False)

            if response.status_code == 204 or response.status_code == 200:
                print('Left server ' + name)
                
            elif response.status_code == 400:
                response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/' + id1, headers={'Authorization': token}, verify = False)

        x = x + 1

