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
    
    print(Fore.CYAN + f"User        : {platform.node()}")
    print(Fore.YELLOW + f"OS          : {platform.system()} {platform.release()}")
    print(Fore.MAGENTA + f"CPU         : {platform.processor()}")
    print(Fore.BLUE + f"RAM         : {round(psutil.virtual_memory().total / (1024**3),2)} GB")
    print(Fore.GREEN + f"Python Ver  : {platform.python_version()}")
    print(Fore.RED + f"Time        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(Fore.WHITE + "-" * 55)

if __name__ == "__main__":
    show_banner()