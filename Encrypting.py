from discord_webhook import DiscordWebhook, DiscordEmbed
from cryptography.fernet import Fernet
import colorama
import random
import time
import sys
import os

username = os.environ.get("USERNAME")

numb_gen = random.radint(0,2000)

def choice_assist():

    if X1 == 1:
        Profile_Creation()
    elif X1 == 2:
        Profile_Deletion()
    elif X1 == 3:
        Passwords()
    else: 
        print("Uh oh that doesnt seem right, try again i guess? :( ")
        time.sleep(2)
        os.system("cls")
        start()

def start():

    global X1

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
            Choice_assist()
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

def saving_to_file(email, password):

    with open(f"ANX{numb_gen}", "w") as file:
         file.write(f"{email}\n")
         file.write(f"{password}\n")
     
def Profile_Creation():

    X = input("Website email: ")
    time.sleep(2)
    Y = input("Website Password: ")
    time.sleep(2)
    saving_to_file(X,Y)
    print("Successfully saved!")

