#!/bin/python3

import socket, sys

# General vars
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 23

try:
    print("[!] Waiting for connection ...")
    s.bind(("127.0.0.1", port))
    s.listen(1024)
    while True:
        LHOST = s.getsockname()
        client_sock, addr = s.accept()
        print(f"Connection established !")
        client_sock.send(bytes(f"[!] You are connected to {LHOST}:{port}", 'utf-8'))
        VHOST = client_sock.recv(1024)
        client_sock.send(bytes(VHOST))
        break
        
except KeyboardInterrupt:
    sys.exit(0)