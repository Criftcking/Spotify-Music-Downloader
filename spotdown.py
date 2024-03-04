import importlib
import subprocess
import os
import colorama
from colorama import Fore
import spotdl
spotdl
colorama.init()
def check_and_install_library(library_name):
    try:
        importlib.import_module(library_name)
    except ImportError:
        subprocess.check_call(["pip", "install", library_name])


library_name = "spotdl"
check_and_install_library(library_name)

def limpiar():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux/Unix/Mac
            os.system('clear')
            
limpiar()
def menu():
    print(Fore.MAGENTA+"""
            
      ██████  ██▓███   ▒█████  ▄▄▄█████▓ ██▓  █████▒▓██   ██▓    ███▄ ▄███▓ █    ██   ██████  ██▓ ▄████▄  
    ▒██    ▒ ▓██░  ██▒▒██▒  ██▒▓  ██▒ ▓▒▓██▒▓██   ▒  ▒██  ██▒   ▓██▒▀█▀ ██▒ ██  ▓██▒▒██    ▒ ▓██▒▒██▀ ▀█  
    ░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒ ▓██░ ▒░▒██▒▒████ ░   ▒██ ██░   ▓██    ▓██░▓██  ▒██░░ ▓██▄   ▒██▒▒▓█    ▄ 
      ▒   ██▒▒██▄█▓▒ ▒▒██   ██░░ ▓██▓ ░ ░██░░▓█▒  ░   ░ ▐██▓░   ▒██    ▒██ ▓▓█  ░██░  ▒   ██▒░██░▒▓▓▄ ▄██▒
    ▒██████▒▒▒██▒ ░  ░░ ████▓▒░  ▒██▒ ░ ░██░░▒█░      ░ ██▒▓░   ▒██▒   ░██▒▒▒█████▓ ▒██████▒▒░██░▒ ▓███▀ ░
    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░   ▒ ░░   ░▓   ▒ ░       ██▒▒▒    ░ ▒░   ░  ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░▓  ░ ░▒ ▒  ░
    ░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░     ░     ▒ ░ ░       ▓██ ░▒░    ░  ░      ░░░▒░ ░ ░ ░ ░▒  ░ ░ ▒ ░  ░  ▒   
    ░  ░  ░  ░░       ░ ░ ░ ▒    ░       ▒ ░ ░ ░     ▒ ▒ ░░     ░      ░    ░░░ ░ ░ ░  ░  ░   ▒ ░░        
        ░               ░ ░            ░           ░ ░               ░      ░           ░   ░  ░ ░      
                                                    ░ ░                                         ░        
"""+Fore.RESET)
    
def options():
    print(Fore.MAGENTA+"""
    |==Downloader Menu==|

    1- Install Requirements
    2- Spotify Music Download (URL)
    3- Exit
    """+Fore.RESET)    
menu()
options()

option = int(input(Fore.LIGHTMAGENTA_EX+"[Select option]========>"+Fore.RESET))
if option == 1:
    os.system("spotdl --download-ffmpeg")
elif option == 2:
    limpiar()
    menu()
    url = str(input(Fore.LIGHTMAGENTA_EX+"[Paste URL]========>"+Fore.RESET))
    os.system(f'spotdl --output "music" {url}')
    print(Fore.LIGHTMAGENTA_EX+"MUSIC SAVE IN '/music' folder")
else:
    limpiar()
    pass
