import socket
import os

def check_domain_availability(domain):
    if ".com" not in domain:
        return False

    server = "whois.verisign-grs.com"
    port = 43
    query = domain + "\r\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, port))
    sock.send(query.encode())

    response = ""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data.decode()
    sock.close()

    if "No match for" in response:
        # First, check if the domain is already in domainNames.txt
        if os.path.exists("domainNames.txt"):
            with open("domainNames.txt", "r") as file:
                existing_domains = file.read().splitlines()
                if domain in existing_domains:
                    return False
        return True

    return False