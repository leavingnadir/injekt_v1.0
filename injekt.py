import shutil

if not shutil.which("nmap"):
    print("Nmap is not installed. Please install it first.")
    sys.exit()

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Auto install colorama
try:
    from colorama import Fore, Style, init
except ImportError:
    print("Installing colorama...")
    install("colorama")
    from colorama import Fore, Style, init

# Auto install psutil
try:
    import psutil
except ImportError:
    print("Installing psutil...")
    install("psutil")
    import psutil

# Auto install python-nmap
try:
    import nmap
except ImportError:
    print("Installing python-nmap...")
    install("python-nmap")
    import nmap

import platform
from datetime import datetime

init(autoreset=True)

def show_banner():
    print(r"""
               \
                \\
                 \%,     ,'     , ,.
                  \%\,';/J,";";";;,,.
     ~.------------\%;((`);)));`;;,.,-----------,~
    ~~:           ,`;@)((;`,`((;(;;);;,`         :~~
   ~~ :           ;`(@```))`~ ``; );(;));;,      : ~~
  ~~  :            `X `(( `),    (;;);;;;`       :  ~~
 ~~~~ :            / `) `` /;~   `;;;;;;;);,     :  ~~~~
~~~~  :           / , ` ,/` /     (`;;(;;;;,     : ~~~~
  ~~~ :          (o  /]_/` /     ,);;;`;;;;;`,,  : ~~~
   ~~ :           `~` `~`  `      ``;,  ``;" ';, : ~~
    ~~:                             `'   `'  `'  :~~
     ~`-----------------------------------------`~
       _____       _      _    _          __   ___  
      |_   _|     (_)    | |  | |        /_ | / _ \ 
        | |  _ __  _  ___| | _| |_  __   _| || | | |
        | | | '_ \| |/ _ \ |/ / __| \ \ / / || | | |
       _| |_| | | | |  __/   <| |_   \ V /| || |_| |
      |_____|_| |_| |\___|_|\_\\__|   \_/ |_(_)___/ 
                 _/ |                               
                |__/                                
    """)
print("\n" + "-" * 55)

print(Fore.CYAN + f"Project      : Injekt -  Network & Vulnerability Scanner")
print(Fore.YELLOW +f"Version      : v1.0.0")
print(Fore.MAGENTA + f"Created      : 2026")
print(Fore.BLUE + f"Languages    : Python")
print(Fore.GREEN + f"Author       : leaving Nadir -Hirusha Ranaweera")
print(Fore.RED + f"Repo         : https://github.com/leavingnadir/injekt_v1.0.git")
print(Fore.WHITE + f"Dependencies : nmap, colorama, psutil")
print("-" * 55)

if __name__ == "__main__":
    show_banner()


import socket
import requests
import nmap
from datetime import datetime

def port_scan(target, start_port, end_port):
    print(f"Scanning target: {target} for open ports from {start_port} to {end_port}...")
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)

        sock.close()
    return open_ports

def banner_grab(target, port):
    print(f"Grabbing banner for {target}:{port}")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        sock.settimeout(2)
        banner = sock.recv(1024).decode('utf-8', errors='ignore')
        sock.close()
        return banner.strip()

    except:
        return None

def vulnerability_scan(target):
    print(f"Scanning target {target} for vulnerabilities...")
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=target, arguments='-O -sV --script=vuln')
        return nm[target]
    except Exception as e:
        print(f"Error during vulnerability scan: {e}")
        return None

def network_scan(target, start_port, end_port):
    print(f"Starting network scan for target: {target}...")
    start_time = datetime.now()

    open_ports = port_scan(target, start_port, end_port)
    if open_ports:
        print(f"Open ports found: {open_ports}")
    else:
        print("No open ports found.")

    for port in open_ports:
        banner = banner_grab(target, port)
        if banner:
            print(f"Banner for {target}:{port} - {banner}")
        else:
            print(f"No banner found for {target}:{port}")
    
    vuln_info = vulnerability_scan(target)
    if vuln_info:
        if 'hostname' in vuln_info:
            print(f"Hostname: {vuln_info['hostname']}")
        if 'osmatch' in vuln_info:
            print(f"Operating System: {vuln_info['osmatch']}")
        if 'vulns' in vuln_info:
            print(f"Vulnerabilities: {vuln_info['vulns']}")
        
    else:
        print(f"No vulnerabilities detected or unable to detect.")

    
    end_time = datetime.now()
    print(f"Scan completed in: {end_time - start_time}")
            

if __name__ == "__main__":
    target_ip = input("Enter the target IP address or hostname: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    network_scan(target_ip, start_port, end_port)
