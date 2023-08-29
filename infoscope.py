import socket
import whois
from colorama import Fore
import webbrowser
import sys
from termcolor import colored
import os
import random
import logging
import psutil
from datetime import datetime


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
    "                             "+Fore.LIGHTRED_EX   +"Version : 1.0 "+Fore.LIGHTCYAN_EX   +"\n"
    "\n"
    "                      "+Fore.LIGHTWHITE_EX+" ["+Fore.LIGHTRED_EX+"1"+Fore.LIGHTWHITE_EX+"] Monitor a server.\n"
    "                      "+Fore.LIGHTWHITE_EX+" ["+Fore.LIGHTRED_EX+"2"+Fore.LIGHTWHITE_EX+"] Insert existing domain.\n"
    "                      "+Fore.LIGHTWHITE_EX+" ["+Fore.LIGHTRED_EX+"3"+Fore.LIGHTWHITE_EX+"] Info Network.\n"
    "                      "+Fore.LIGHTWHITE_EX+" ["+Fore.LIGHTRED_EX+"4"+Fore.LIGHTWHITE_EX+"] Block IP Address.\n"
    "                      "+Fore.LIGHTWHITE_EX+" ["+Fore.LIGHTRED_EX+"5"+Fore.LIGHTWHITE_EX+"] Unblock IP address.\n"
    "\n"
    "          "+Fore.LIGHTWHITE_EX+" ["+Fore.LIGHTRED_EX+"help"+Fore.LIGHTWHITE_EX+"] Help.    ["+Fore.LIGHTRED_EX+"exit"+Fore.LIGHTWHITE_EX+"] Exit.     ["+Fore.LIGHTRED_EX+"clear"+Fore.LIGHTWHITE_EX+"] Clear.\n"
)

logging.basicConfig(filename='infoscope.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

blocked_ips = set()

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

def start_tracking_server(ip_address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.bind((ip_address, port))
            server_socket.listen()
            print(f"Trace server started on {ip_address}:{port}")
            logging.info(f"Trace server started on {ip_address}:{port}")

            while True:
                client_socket, client_address = server_socket.accept()
                if client_address[0] in blocked_ips:
                    print(f"Blocked connection from {client_address[0]}")
                    client_socket.close()
                    continue

                print(f"Connection received from {client_address[0]}:{client_address[1]} at {datetime.now()}")
                logging.info(f"Connection received from {client_address[0]}:{client_address[1]} at {datetime.now()}")
                client_socket.close()

        except OSError as e:
            print(f"Error: {e}")
            logging.error(f"Error: {e}")

if __name__ == "__main__":
    print(colored(logo, 'red'))

    while True:
        choice = input("infoscope> ")

        if choice == "1":
            try:
                ip_address = input("Enter the IP address of the server: ")
                port = int(input("Enter port to monitor: "))
                
                if port == 0:
                    port = random.randint(1024, 49151)
                    print(f"Using random port: {port}")
                
                start_tracking_server(ip_address, port)
                logging.info(f"Started tracking server on {ip_address}:{port}")
            except ValueError:
                print("Invalid input. Please enter a valid port number.")

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

        elif choice.lower() == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored(logo, 'red'))

        elif choice == "3":
            network_info = psutil.net_if_addrs()
            for interface, addresses in network_info.items():
                print(f"Interface: {interface}")
                for addr in addresses:
                    print(f"  {addr.family.name} Address: {addr.address}")
            print("\nNote: Some interfaces might not have an IP address.")
        
        elif choice == "4":
            blocked_ip = input("Enter the IP address to block: ")
            blocked_ips.add(blocked_ip)
            print(f"Blocked IP: {blocked_ip}")

        elif choice == "5":
            blocked_ip = input("Enter the IP address to unblock: ")
            if blocked_ip in blocked_ips:
                blocked_ips.remove(blocked_ip)
                print(f"Unblocked IP: {blocked_ip}")
            else:
                print(f"IP address {blocked_ip} not found in blocked list.")

        else:
            print("Invalid option. Please choose a valid option.")