import socket, sys
from color import color

def connect(IP):
    socket = socket.socket(AF_INET)
    print(socket)
    try:
        pass
    except KeyboardInterrupt:
        print(f"\n{color.fr_red}[!] Abording ...{color.reset}")
        sys.exit()
