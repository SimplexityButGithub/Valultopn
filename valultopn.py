import requests
import random
import string
import time
from colorama import init, Fore, Back

init()

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def check_code(code):
    response = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}")
    if response.status_code == 200:
        return True
    else:
        return False

def print_logo():
    # Here's your fancy rainbow ASCII logo
    print(Fore.RED + Back.GREEN)
    print("  ██╗   ██╗ █████╗ ██╗     ██╗   ██╗██╗  ████████╗ ██████╗ ██████╗ ███╗   ██╗")
    print("  ██║   ██║██╔══██╗██║     ██║   ██║██║  ╚══██╔══╝██╔═══██╗██╔══██╗████╗  ██║")
    print("  ██║   ██║███████║██║     ██║   ██║██║     ██║   ██║   ██║██████╔╝██╔██╗ ██║")
    print("  ╚██╗ ██╔╝██╔══██║██║     ██║   ██║██║     ██║   ██║   ██║██╔═══╝ ██║╚██╗██║")
    print("   ╚████╔╝ ██║  ██║███████╗╚██████╔╝███████╗██║   ╚██████╔╝██║     ██║ ╚████║")
    print("    ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝    ╚═════╝ ╚═╝     ╚═╝  ╚═══╝")
    print(Back.RESET)

print_logo()
print("Generating Discord Nitro codes...\n")

while True:
    code = generate_code()
    if check_code(code):
        print(f"{Fore.GREEN}Valid Nitro Code: {Fore.RESET}discord.gift/{code}")
    else:
        print(f"{Fore.RED}Redeemed Nitro Code: {Fore.RESET}discord.gift/{code}")
    time.sleep(0.1)