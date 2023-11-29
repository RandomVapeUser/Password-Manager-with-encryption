from discord_webhook import DiscordWebhook, DiscordEmbed
from cryptography.fernet import Fernet
import colorama
import time
import sys
import os

username = os.environ.get("USERNAME")

while True:

    print(f"""

        Welcome to my password manager {username} :)
          
        [1] - Add Profile
        [2] - Delete Profile
        [3] - See Passwords
        [4] - Help
        
        """)
    
    try:
        X = int(input(" "))
        break
    except SyntaxError:
        print("You need to enter a numbers not a letter you dummy")
        time.sleep(2)
        os.system("cls")
        continue

def encrypting():

    os.system("cls")

    key = Fernet.generate_key()

    print("""                                   ~
                                                    
                                                    WARNING:        
          
                        Do not use this password manager, it is highly exploitable and editable.
                                        Made by: salomao31(my discord)
          
          """)



def Profile_Creation():

    print("Loading...")
    time.sleep(2)
    os.system("cls")


















def choice():

    if X == 1:
        encrypting()
    elif X == 2:
        decrypting()
    elif X == 3:
        help0()