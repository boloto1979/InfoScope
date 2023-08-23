import socket
import whois
import random
from termcolor import colored

logo = (
    "                     ⠀⠀⠀⠀⠀                       ⠀⠀⠀⠀⠀\n"
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
)

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
        print("Choose an option:")
        print("1. Monitor a server")
        print("2. Insert existing domain")
        
        choice = input("Option: ")

        if choice == "1":
            ip_address = input("Enter the IP address of the server: ")
            port = int(input("Enter port to monitor: "))
            
            start_tracking_server(ip_address, port)
        
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
        
        else:
            print("Invalid option. Please choose a valid option.")