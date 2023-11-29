from discord_webhook import DiscordWebhook, DiscordEmbed
from cryptography.fernet import Fernet
import colorama
import random
import time
import sys
import os

username = os.environ.get("USERNAME")

numbgen = 

while True:

    print(f"""

        Welcome to my password manager {username} :)
          
        [1] - Add Profile
        [2] - Delete Profile
        [3] - See Passwords
        [4] - Help
        
        """)
    
    try:
        X1 = int(input(" "))
        break
    except SyntaxError:
        print("You need to enter a numbers not a letter you dummy")
        time.sleep(2)
        os.system("cls")
        continue


os.system("cls")

print("""                                   
                                                    
                                                    WARNING:        
          
                        Do not use this password manager, it is highly exploitable and editable.
                                        Made by: salomao31(my discord)
          
    """)


time.sleep(5)
print("Loading...")
time.sleep(2)
os.system("cls")

def saving_to_file():

     
def Profile_Creation():

    while True:

            X = input("Website email: ")
            time.sleep(2)
            Y = input("Website Password: ")
            time.sleep(2)

            try 




















def choice():

    if X == 1:
        encrypting()
    elif X == 2:
        decrypting()
    elif X == 3:
        help0()