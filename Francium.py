from Bot_Info import Bot_Info
from Webhook_Sender import Webhook_Sender
from Webhook_Spammer import Webhook_Spammer
from Info_Grabber import Info_Grabber
from Super_Annoy import Super_Annoy
from Webhook_Deleter import Webhook_Deleter
from Webhook_Nuker import Webhook_Nuker
from QR_Grabber import QR_Grabber
from Server_Leaver import Server_Leaver
from Friend_Remover import Friend_Remover

from time import sleep
from colorama import init, Fore, Back, Style
init(convert =  True)

banner = f''' {Fore.RED}

 ██▓███   ██▀███   ▒█████   ▄▄▄██▀▀▀▓█████  ▄████▄  ▄▄▄█████▓         
▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒   ▒██   ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒         
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒   ░██   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░         
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░▓██▄██▓  ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░          
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░ ▓███▒   ░▒████▒▒ ▓███▀ ░  ▒██▒ ░          
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░  ▒▓▒▒░   ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░            
░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░  ▒ ░▒░    ░ ░  ░  ░  ▒       ░             
░░         ░░   ░ ░ ░ ░ ▒   ░ ░ ░      ░   ░          ░               
            ░         ░ ░   ░   ░      ░  ░░ ░                        
                                           ░                          
  █████▒██▀███   ▄▄▄       ███▄    █  ▄████▄   ██▓ █    ██  ███▄ ▄███▓
▓██   ▒▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▒██▀ ▀█  ▓██▒ ██  ▓██▒▓██▒▀█▀ ██▒
▒████ ░▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄ ▒██▒▓██  ▒██░▓██    ▓██░
░▓█▒  ░▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒░██░▓▓█  ░██░▒██    ▒██ 
░▒█░   ░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░░██░▒▒█████▓ ▒██▒   ░██▒
 ▒ ░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░▓  ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░ 
 ░       ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒    ▒ ░░░▒░ ░ ░ ░  ░      ░
 ░ ░     ░░   ░   ░   ▒      ░   ░ ░ ░         ▒ ░ ░░░ ░ ░ ░      ░   
          ░           ░  ░         ░ ░ ░       ░     ░            ░   
                                     ░                                
{Fore.RESET}
{Fore.YELLOW}
> By xGrqnd
> Discord:
> discord.com/SERVERLINKNOTHEREYET

> Credit to Hazard Nuker for an idea - I wanted to add more webhook
and discord bot functions - but the code is fully mine but QR Grabber
which is credited in the module

> https://github.com/Rdimo/Hazard-Nuker
> No SKID though :)
'''

table = Fore.RESET + '''
+----------------------------+----------------------+---------------------+
|       Bot Functions        |  Webhook Functions   | User Functions      |
+----------------------------+----------------------+---------------------+
| [1] Bot Info               | [8] Webhook Sender   | [12] Get Info       |
| [2] Invite to all servers  | [9] Webhook Spammer  | [13] Super Annoy    |
| [3] Server Spammer         | [10] Webhook Nuker   | [14] QR Grabber     |  
| [4] Server Channel Maker   | [11] Webhook Deleter | [15] Server Leaver  |
| [5] Server Channel Deleter |                      | [16] Friend Remover |
| [6] Give Admin             |                      |                     |
| [7] User DM Spam           |                      |                     |
+----------------------------+----------------------+---------------------+

+------------------------------------+
| Enter the option you want to use:  |
+------------------------------------+
'''
def main():

    x = 0
    while x < 60:
        print()
        x = x + 1

    while True:
        

        print(banner)
        sleep(2)
        print(table)
        sleep(0.5)
        mode = input('>>> ')
        print()
        
        if mode == '1':
            question = '''
+-----------------------+
| Enter your Bot Token: |
+-----------------------+
        '''
            print(question)
            token = input('>>> ')
            print()
            Bot_Info(token)
            pass

        if mode == '8':
            question = '''
+-----------------------+
| Enter your Webhook  : |
+-----------------------+
'''
            print(question)
            webhook = input('>>> ')
            print()
            Webhook_Sender(webhook)
            pass
        
        if mode == '9':
            question = '''
+-----------------------+
| Enter your Webhook  : |
+-----------------------+
'''
            print(question)
            webhook = input('>>> ')
            print()
            Webhook_Spammer(webhook)
            pass

        if mode == '10':
           question = '''
+-----------------------+
| Enter your Webhook  : |
+-----------------------+
'''
           print(question)
           webhook = input('>>> ')
           print()
           Webhook_Nuker(webhook)
           pass

        if mode == '11':
            question = '''
+-----------------------+
| Enter your Webhook  : |
+-----------------------+
'''
            print(question)
            webhook = input('>>> ')
            print()
            Webhook_Deleter(webhook)
            pass

        if mode == '12':
            question = '''
+-----------------------+
| Enter the TOKEN:      |
+-----------------------+
'''
            print(question)
            token = input('>>> ')
            print()
            Info_Grabber(token)
            pass

        if mode == '13':
            question = '''
+-----------------------+
| Enter the Token:      |
+-----------------------+
'''
            print(question)
            token = input('>>> ')
            print()
            Super_Annoy(token)
            pass

        if mode == '14':
            QR_Grabber()

        if mode == '15':
            question = '''
+-----------------------+
| Enter the Token:      |
+-----------------------+
'''
            print(question)
            token = input('>>> ')
            print()
            Server_Leaver(token)
            pass
            
        if mode == '16':
            question = '''
+-----------------------+
| Enter the Token:      |
+-----------------------+
'''
            print(question)
            token = input('>>> ')
            print()
            Friend_Remover(token)
            pass

        else:
            ERROR = '''
+-------------------------+
| ERROR: UNKNOWN FUNCTION |
+-------------------------+
'''
            print(ERROR)

        sleep(1.5)
        x = 0

        while x < 60:
            print()
            x = x + 1
        
    






if __name__ == '__main__':
    main()
    








