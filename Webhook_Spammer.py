import requests

def Webhook_Spammer(webhook):
    question = '''
+-----------------------+
| Enter your Message:   |
+-----------------------+
    '''
    print(question)
    message = input('>>> ')
    
    payload = {
        "content": message
        }

    
    while True:
        try:
            send = requests.post(webhook, json = payload, verify = False)
            sleep(0.3)
        except:
    
            ERROR = '''
+-----------------------------------+
| Incorrect Webhook, or pip SSL FAIL|
+-----------------------------------+
'''
            pass
