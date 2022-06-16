import requests

def Webhook_Sender(webhook):
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

    try:
        send = requests.post(webhook, json = payload, verify = False)

    
    except:
        ERROR = '''
+-----------------------------------+
| Incorrect Webhook, or pip SSL FAIL|
+-----------------------------------+
'''
        print(ERROR)
