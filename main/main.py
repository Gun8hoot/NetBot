import os, sys, socket, time, subprocess, threading
from module.color import color

#   ARGUMENTS
validargv = '-c', '-l', '-i', ''

class argv():
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[3]
        arg3 = sys.argv[5]
        arg4 = sys.argv[7]
        arg5 = sys.argv[9]
    except IndexError:
        pass
# Fonction
def main():
    from module.IP import lst_ip
    lst_ip()
    sys.exit()
    try:
        try:
            if argv.arg1 == validargv[0] or argv.arg2 != validargv[0] or argv.arg3 != validargv[0]:
                print('aaa')
        except AttributeError:
            from module.getHelp import getHelp
            getHelp()

    
    except KeyboardInterrupt:
        print ("\033[A\033[A")
        print(f'{color.fr_red}{color.bold_on}[!] Keyboard intrupt keys press !{color.reset}')

if __name__ == '__main__':
    main()