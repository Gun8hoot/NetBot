import sys, os

def getHelp():
    print('\x1b[38;5;1m\x1b[1mRemote controle malware replication:\n\x1b[0m   \x1b[38;5;7m-h : Show this help message\n   -c : The command to send\n   -l : List ip saved in the program\n   -i : Add an IP in the .ip.conf file (you need to specify the port too)\x1b[0m')
    sys.exit()
getHelp()