import os , sys

try:
  import psutil
except ImportError:
  print("Install required module: psutil\n")
  os.system('python -m pip install psutil')
try:
  from pyinjector import inject
except ImportError:
  print("Install required module: pyinjector\n")
  os.system('python -m pip install pyinjector')
try:
  import rgbprint 
except ImportError:
  print("Install required module: rgbprint\n")
  os.system('python -m pip install rgbprint')
try:
  import time
except ImportError:
  print("Install required module: time\n")
  os.system('python -m pip install time')


def FindCombatMater():
    processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_info = proc.info
            if process_info['name'] == "CombatMaster.exe":
                processes.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes


def clear():
  os.system('cls' if os.name == 'nt' else 'clear')


def titleui():
    rgbprint.gradient_print(
  """
+===============================================================================================================+
|  ██████╗ ██████╗ ███╗   ███╗██████╗  █████╗ ████████╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗  |
| ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗ |
| ██║     ██║   ██║██╔████╔██║██████╔╝███████║   ██║       ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝ |
| ██║     ██║   ██║██║╚██╔╝██║██╔══██╗██╔══██║   ██║       ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗ |
| ╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║  ██║   ██║       ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║ |
|  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ |
|                                                                                                               |
|                                     ██╗  ██╗ █████╗  ██████╗██╗  ██╗                                          |
|                                     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝                                          |
|                                     ███████║███████║██║     █████╔╝                                           |
|                                     ██╔══██║██╔══██║██║     ██╔═██╗                                           |
|                                     ██║  ██║██║  ██║╚██████╗██║  ██╗                                          |
|                                     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                                          |
+===============================================================================================================+
""",
    start_color=0x4BBEE3, 
    end_color=rgbprint.Color.medium_violet_red    
)
    rgbprint.gradient_print(
        "                                              Made By luxz#8403",
        start_color=0x4BBEE3, 
        end_color=rgbprint.Color.medium_violet_red    
    )
    rgbprint.gradient_print(
        "\n                                [+] 1 : Vesion 1 | [+] 2 : Vesion 2 (Menu shows when in game)",
        start_color=0x4BBEE3, 
        end_color=rgbprint.Color.medium_violet_red    
    )


def Injectdll(type):
    process = FindCombatMater()
    if not process:
        rgbprint.rgbprint("[!] Combat Master is Not open", color="red")
        time.sleep(1)
        sys.exit()
    else:
        rgbprint.rgbprint(f"[+] Found Combat Master (PID: {process[0]['pid']})", color="lime_green")
        if type == "1":
            rgbprint.rgbprint(f"[+] Start Inject DLL", color="yellow")
            time.sleep(1)
            inject(int(process[0]['pid']), "kappa.dll")
            rgbprint.rgbprint(f"[+] Injecting kappa.dll into process {process[0]['pid']}", color="yellow")
            time.sleep(1)
            rgbprint.rgbprint("[+] Successfully Injected DLL", color="lime_green")
            rgbprint.rgbprint("[+] Press Insert to open menu and Press again to close", color="yellow")
        elif type == "2":
            rgbprint.rgbprint(f"[+] Start Inject DLL", color="yellow")
            time.sleep(1)
            inject(int(process[0]['pid']), "cheat.dll")
            rgbprint.rgbprint(f"[+] Injecting cheat.dll into process {process[0]['pid']}", color="yellow")
            time.sleep(1)
            rgbprint.rgbprint("[+] Successfully Injected DLL", color="yellow")
            rgbprint.rgbprint("[+] Menu will shows automatically when in game", color="lime_green")
            rgbprint.rgbprint("[+] Press Insert to open menu and Press again to close", color="yellow")
   


def Main():
    while True:
        titleui()
        print(f"\n\33[33mENTER 1-2 -> \x1b[0m", end='')
        select = input()
        if select == "1":
            break
        elif select == "2":
            break
        else:
            print("\33[91mInvalid input. Please enter 1 or 2. \x1b[0m") 
            time.sleep(1)
            clear()
            continue
    Injectdll(select)


Main()

