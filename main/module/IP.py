from module.color import color
import os, sys
path_conf = r'./config/ip.conf'

def checkconffile():
    try:
        print(f'{color.fr_green}[!] The ./config/ip.conf exist{color.reset}')
    except FileNotFoundError:
        print(f"{color.fr_red}[!] The file ./config/ip.conf doesn't exist. The file will be create.")
        with open(path_conf, 'w') as createconf:
            createconf.write('')
        sys.exit() 

def lst_ip():
    checkconffile()
    with open(path_conf, 'r') as readfile:
        nmb_line = sum(1 for _ in readfile)
        print(f'{color.fr_yellow}[!] Listing all ip saved in config/ip.conf. The .conf file contain {nmb_line} lines. {color.fr_orange}')
    print(readfile.read())
