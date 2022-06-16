import requests

def Webhook_Deleter(webhook):
    print('Deleting Webhook ... ')
    print()
    requests.delete(webhook, verify = False)
    print()
    print('Deleted')
    
