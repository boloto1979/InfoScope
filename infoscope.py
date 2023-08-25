import socket
import whois
from colorama import Fore
import webbrowser
import sys
from termcolor import colored
import os
import random
import logging


logo = (
    "\n"
    "                     ⠀⠀⠀⠀⠀⣀⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣀⠀⠀⠀⠀⠀⠀\n"
    "                     ⠀⠀⠀⣠⡞⠁⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀\n"
    "                     ⠀⠀⣴⡟⠀⠀⠀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⡀⠀⠀⢿⣆⠀⠀⠀\n"
    "                     ⠀⣼⣿⠁⠀⢠⣾⡟⠀⢀⡤⠂⠀⠀⠀⠀⠀⠢⡀⠀⠀⢻⣄⠀⠈⣿⣆⠀⠀\n"
    "                     ⢰⣿⡟⠀⢀⣿⡿⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⢹⣆⠀⠈⣿⡆⠀⢻⣿⡄⠀\n"
    "                     ⣸⣿⡇⠀⢸⣿⡇⠀⣿⡏⠀⠀⣠⣶⣶⣶⡀⠀⠈⣿⡄⠀⢻⣿⠀⢸⣿⡇⠀\n"
    "                     ⢻⣿⡇⠀⢹⣿⡇⠀⣿⣇⠀⠀⢿⣿⣿⣿⡇⠀⢀⣿⠇⠀⣸⣿⠀⢸⣿⡇⠀\n"
    "                     ⢸⣿⣇⠀⠸⣿⣧⠀⠹⣿⠀⠀⠀⢹⣿⠉⠀⠀⣸⡟⠀⠀⣿⡏⠀⣸⣿⠇⠀\n"
    "                     ⠀⢿⣿⡀⠀⠙⣿⣆⠀⠘⠳⠀⠀⢸⣿⠀⠀⠀⠋⠀⠀⣼⠟⠀⢀⣿⡟⠀⠀\n"
    "                     ⠀⠈⢿⣧⠀⠀⠈⠻⣆⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⢀⡼⠋⠀⠀⣼⡿⠁⠀⠀\n"
    "                     ⠀⠀⠈⠻⣧⠀⠀⠀⠈⠑⠀⠀⠀⢸⣿⠀⠀⠀⠀⠁⠀⠀⠀⠞⠁⠀⠀⠀⠀\n"
    "                     ⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠠⠃⠀⠀⠀⠀⠀\n"
    "                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    "                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    "  ██╗███╗░░██╗███████╗░█████╗░░██████╗░█████╗░░█████╗░██████╗░███████╗\n"
    "  ██║████╗░██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝\n"
    "  ██║██╔██╗██║█████╗░░██║░░██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝█████╗░░\n"
    "  ██║██║╚████║██╔══╝░░██║░░██║░╚═══██╗██║░░██╗██║░░██║██╔═══╝░██╔══╝░░\n"
    "  ██║██║░╚███║██║░░░░░╚█████╔╝██████╔╝╚█████╔╝╚█████╔╝██║░░░░░███████╗\n"
    "  ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚══════╝\n"
    "                       "+Fore.LIGHTRED_EX+"["+Fore.LIGHTWHITE_EX+"::"+Fore.LIGHTRED_EX+"] "+Fore.LIGHTWHITE_EX+"Select an Option "+Fore.LIGHTRED_EX+"["+Fore.LIGHTWHITE_EX+"::"+Fore.LIGHTRED_EX+"]\n"
    "\n"
    "                       "+Fore.LIGHTWHITE_EX+" ["+Fore.LIGHTRED_EX+"1"+Fore.LIGHTWHITE_EX+"] Monitor a server.\n"
    "                    "+Fore.LIGHTWHITE_EX+" ["+Fore.LIGHTRED_EX+"2"+Fore.LIGHTWHITE_EX+"] Insert existing domain.\n"
    "\n"
    "          "+Fore.LIGHTWHITE_EX+" ["+Fore.LIGHTRED_EX+"help"+Fore.LIGHTWHITE_EX+"] Help.    ["+Fore.LIGHTRED_EX+"exit"+Fore.LIGHTWHITE_EX+"] Exit.     ["+Fore.LIGHTRED_EX+"clear"+Fore.LIGHTWHITE_EX+"] Clear.\n"
)

logging.basicConfig(filename='infoscope.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w
    except whois.parser.PywhoisError:
        return None

def generate_tracking_link():
    return "http://127.0.0.1:8000/"

def start_tracking_server(ip_address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((ip_address, port))
        server_socket.listen()
        print(f"Trace server on started {ip_address}:{port}")
        
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"connection received from {client_address[0]}:{client_address[1]}")
            client_socket.close()

if __name__ == "__main__":
    print(colored(logo, 'red'))

    while True:
        choice = input("infoscope> ")

        if choice == "1":
            ip_address = input("Enter the IP address of the server: ")
            port = int(input("Enter port to monitor: "))
            
            if port == 0:
                port = random.randint(1024, 49151)
                print(f"Using random port: {port}")
            
            start_tracking_server(ip_address, port)
            logging.info(f"Started tracking server on {ip_address}:{port}")
        
        elif choice == "2":
            domain = input("Enter the domain you want to search for information: ")
            ip_address = get_ip_address(domain)
            if ip_address:
                print(f"Domain IP address {domain}: {ip_address}")
            else:
                print(f"Unable to get IP address for domain {domain}")
            
            whois_info = get_whois_info(domain)
            if whois_info:
                print("WHOIS information:")
                print(whois_info)
            else:
                print(f"Unable to get WHOIS information for the domain {domain}")
        
        elif choice.lower() == "help":
            webbrowser.open("https://github.com/boloto1979/InfoScope")

        elif choice.lower() == "exit":
            print("Exiting InfoScope. Goodbye!")
            logging.info("Exiting InfoScope")
            sys.exit()

        if choice.lower() == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored(logo, 'red'))

        else:
            print("Invalid option. Please choose a valid option.")