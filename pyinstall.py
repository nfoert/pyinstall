from colorama import Fore, Style
import platform
import sys
from time import sleep
import os
import subprocess

# Enter the name of your .spec or .py file here:

specfile_windows = "example.py"
specfile_mac = "example.py"

# -------------------------------------

print(f"{Fore.YELLOW}--------------------------------------------------------------------------")
print(f"{Fore.MAGENTA}                _          _____       _           _        _ _            ")
print(f"{Fore.MAGENTA}     /\        | |        |  __ \     (_)         | |      | | |           ")
print(f"{Fore.MAGENTA}    /  \  _   _| |_ ___   | |__) |   _ _ _ __  ___| |_ __ _| | | ___ _ __  ")
print(f"{Fore.MAGENTA}   / /\ \| | | | __/ _ \  |  ___/ | | | | '_ \/ __| __/ _` | | |/ _ \ '__| ")
print(f"{Fore.MAGENTA}  / ____ \ |_| | || (_) | | |   | |_| | | | | \__ \ || (_| | | |  __/ |    ") 
print(f"{Fore.MAGENTA} /_/    \_\__,_|\__\___/  |_|    \__, |_|_| |_|___/\__\__,_|_|_|\___|_|    ")
print(f"{Fore.MAGENTA}                                  __/ |                                    ")
print(f"{Fore.MAGENTA}                                |___/                                      ")
print(f"{Fore.MAGENTA}    Cross-Platform Pretty Pyinstaller by {Fore.RED}nfoert                            ")
print(f"{Fore.YELLOW}--------------------------------------------------------------------------")

if platform.system() == "Windows":
    print(f"{Fore.YELLOW}Selected OS: Windows")

elif platform.system() == "Darwin":
    print(f"{Fore.YELLOW}Selected OS: Mac")

else:
    print(f"{Fore.RED}OS NOT DETECTED OR SUPPORTED")
    print(f"{Fore.YELLOW}--------------------------------------------------------------------------")
    print(Style.RESET_ALL)
    sys.exit()

print(f"{Fore.GREEN}PREPARE FOR PYINSTALLING")
print(f"{Fore.YELLOW}--------------------------------------------------------------------------")
sleep(1)
print(f"{Fore.GREEN}Starting in 3")
sleep(1)
print("\033[A                             \033[A")
print(f"{Fore.GREEN}Starting in 2")
sleep(1)
print("\033[A                             \033[A")
print(f"{Fore.GREEN}Starting in 1")
sleep(1)
print("\033[A                             \033[A")
print(f"{Fore.GREEN}Starting!")
print(f"{Fore.YELLOW}--------------------------------------------------------------------------")

print(Style.RESET_ALL)

if platform.system() == "Darwin":
    cmd = subprocess.call(f"pyinstaller --noconfirm {specfile_mac}", shell=True, stdout=subprocess.PIPE)

else:
    cmd = subprocess.call(f"pyinstaller --noconfirm {specfile_windows}", shell=True, stdout=subprocess.PIPE)

print("\n")
print(f"{Fore.GREEN} Done!")
print(f"{Fore.YELLOW}--------------------------------------------------------------------------")


print(Style.RESET_ALL)