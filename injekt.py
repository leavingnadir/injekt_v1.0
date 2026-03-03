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