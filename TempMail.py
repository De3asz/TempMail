













from mailtm import Email
import os
import time
from colorama import Fore, Back, Style, init
from pystyle import Colors, Colorate

time.sleep(3)
print(Colorate.Horizontal(Colors.blue_to_cyan,"""

██████╗ ███████╗██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔════╝╚════██╗██╔══██╗██╔════╝╚══███╔╝
██║  ██║█████╗   █████╔╝███████║███████╗  ███╔╝
██║  ██║██╔══╝   ╚═══██╗██╔══██║╚════██║ ███╔╝
██████╔╝███████╗██████╔╝██║  ██║███████║███████╗███████╗
╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝


""",1))
print("YT: De3asz_ and De3asz_ 2")
init(autoreset=True)

time.sleep(2)
print("Usuwanie PanSage za wlama 12%/100%")
time.sleep(0.9)
print("Usuwanie banów z discorda u davinciego 30%/100%")
time.sleep(4)
print("Laduje silniki aternosa 100%/100%")
time.sleep(5)
os.system('cls')

print(Colorate.Horizontal(Colors.blue_to_cyan,"""

██████╗ ███████╗██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔════╝╚════██╗██╔══██╗██╔════╝╚══███╔╝
██║  ██║█████╗   █████╔╝███████║███████╗  ███╔╝
██║  ██║██╔══╝   ╚═══██╗██╔══██║╚════██║ ███╔╝
██████╔╝███████╗██████╔╝██║  ██║███████║███████╗███████╗
╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝


""",1))
print(f"Siema {os.getlogin()} , Gotowy na maila?")
print("")
def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])

# Get Domains
test = Email()
print("\nDomena: " + test.domain)

# Make new email address
test.register()
print("\nAdres: " + str(test.address))

# Start listening
test.start(listener)
print("\nCzekanie na maila...")