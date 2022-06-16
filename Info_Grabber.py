import requests
import json

def Info_Grabber(token):
    token = token
    r = requests.get('https://discord.com/api/v9/users/@me', headers = {"Authorization": token}, verify = False)

    userName = r.json()['username'] + '#' + r.json()['discriminator']
    userID = r.json()['id']
    phone = r.json()['phone']
    email = r.json()['email']
    language = r.json()['locale']
    mfa = r.json()['mfa_enabled']
    avatar_id = r.json()['avatar']

    print()
    print()
    print('User: ' + userName)
    print('User ID: ' + userID)
    try:
        print('Phone: ' + phone)
    except:
        pass
    try:
        print('email: ' + email)
    except:
        pass
    print('Language: ' + language)
    print('MFA: ' + str(mfa))
    print('Avatar ID: ' + avatar_id)
    print()
    input('Continue?')



