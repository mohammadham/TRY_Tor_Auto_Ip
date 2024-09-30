import time
import os
import subprocess
import sys






try:

    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

os.system("clear")
port1="9050"
port2="9050"
lin = 0
x = 600
auto = False
if len(sys.argv)>1:
    auto = True
    if sys.argv[1] == '-u':
        port2 = port1
    elif sys.argv[1] == '-p':
        if len(sys.argv)==4:
            port1 = int(sys.argv[2])
            port2 = int(sys.argv[3])
        if len(sys.argv)==3:
            port1 = int(sys.argv[2])
            port2 = port1
    else:
        print(f"service cant start !! use -h for help")
        exit(1)

    if len(sys.argv)>2 and sys.argv[1] == '-u' and sys.argv[2] == '-t':
        x = int(sys.argv[3])
        if len(sys.argv)>4 and sys.argv[4] == '-f':
            line = int(sys.argv[5])
    elif len(sys.argv)>2 and sys.argv[1] == '-u' and sys.argv[2] == '-f':
        lin = int(sys.argv[3])
        if len(sys.argv)>4 and sys.argv[4] == '-t':
            x = int(sys.argv[5])
    elif len(sys.argv)>3 and sys.argv[1] == '-p':
        if len(sys.argv)>4 and sys.argv[4] == '-t':
            x = int(sys.argv[5])
            if len(sys.argv)>5 and sys.argv[6] == '-f':
                lin = int(sys.argv[7])
        elif len(sys.argv)>3 and sys.argv[3] == '-t':
            x = int(sys.argv[4])
            if len(sys.argv)>4 and sys.argv[5] == '-f':
                lin = int(sys.argv[6])
        elif len(sys.argv)>3 and sys.argv[3] == '-f':
            lin = int(sys.argv[4])
            if len(sys.argv)>4 and sys.argv[5] == '-t':
                x = int(sys.argv[6])
    


def ma_ip():
    url='http://checkip.amazonaws.com'
    get_ip= requests.get(url,proxies=dict(http=f"socks5://127.0.0.1:{port1}",https=f"socks5://127.0.0.1:{port2}"))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('[+] Your IP has been Changed to : '+str(ma_ip()))

print('''\033[1;32;40m \n
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 0.1
from mrFD
''')

os.system("service tor start")




time.sleep(3)
print(f"\033[1;32;40m change your  SOCKES to 127.0.0.1:{port1} \n")
os.system("service tor start")
if auto == False:
    x = input("[+] time to change Ip in Sec [type=60] >> ")
    lin = input("[+] How many times do you want to change your IP? enter to infinite IP change] >> ") or "0"
try:
    lin = int(lin)

    if lin == 0:
        print("Starting infinite IP change. Press Ctrl+C to stop.")
        while True:
            try:
                time.sleep(int(x))  # Assuming 'x' is defined earlier in your code
                change()  # Assuming 'change()' is defined elsewhere
            except KeyboardInterrupt:
                print('\nAuto IP changer is closed.')
                break
    else:
        for _ in range(lin):
            time.sleep(int(x))  # Assuming 'x' is defined earlier in your code
            change()  # Assuming 'change()' is defined elsewhere

except ValueError:
    print("Invalid input. Please enter a valid number.")
