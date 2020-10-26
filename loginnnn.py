# Created by Falcn8 on GitHub

import os
from colorama import Fore, Back, Style, init

clear = lambda: os.system('cls')
clear()

username = input(Fore.LIGHTCYAN_EX + "Login: >> " + Fore.YELLOW)

users = ["test", "Falcn8"]
pas = ["test", "Falcn8"]

if username in users:
    print(Fore.WHITE + f"Welcome back, {username}.")
    password = input(Fore.LIGHTCYAN_EX + "Password: >> " + Fore.YELLOW)
    pos = users.index(username)
    if password == pas[pos]:
        print(Fore.WHITE + f"Successfully logged in. Thank you {username}!" + Fore.RESET)
    else:
        print(Fore.BLUE + f"Wrong password." + Fore.RESET)
else:
    print(Fore.BLUE + f'No user called "{username}".' + Fore.RESET)
