import platform
import os
import time
import cpuinfo
from colorama import Fore, Style, init


init()

class Colors:
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    PINK = Fore.MAGENTA  
    RED = Fore.RED

def get_cpu_info():
    cpu_info_raw = cpuinfo.get_cpu_info()
    manufacturer = cpu_info_raw['brand_raw']
    
    if "AMD" in manufacturer:
        return f"{Colors.RED}CPU: {manufacturer}{Style.RESET_ALL}"
    elif "Intel" in manufacturer:
        return f"{Colors.BLUE}CPU: {manufacturer}{Style.RESET_ALL}"
    else:
        return f"{Colors.GREEN}CPU: {manufacturer}{Style.RESET_ALL}"

def get_gpu_info():
    try:
        import GPUtil
        gpu_list = GPUtil.getGPUs()
        if gpu_list:
            gpu_info = f"{Colors.GREEN}GPU: {gpu_list[0].name}, Memory: {gpu_list[0].memoryFree:.2f} MB Free / {gpu_list[0].memoryTotal:.2f} MB Total{Style.RESET_ALL}"

            if "Intel" in gpu_list[0].name:
                gpu_info += f" ({Colors.BLUE}Integrated{Style.RESET_ALL})"
            else:
                gpu_info += f" ({Colors.GREEN}Dedicated{Style.RESET_ALL})"
        else:
            gpu_info = f"{Colors.YELLOW}GPU: Not Found{Style.RESET_ALL}"
    except ImportError:
        gpu_info = f"{Colors.YELLOW}GPU: Module not installed{Style.RESET_ALL}"

    return gpu_info

def get_memory_info():
    import psutil
    memory_info = psutil.virtual_memory()
    return f"{Colors.GREEN}Memory: {memory_info.available / 1024 / 1024:.2f} MB Free / {memory_info.total / 1024 / 1024:.2f} MB Total{Style.RESET_ALL}"


def catinfo():
    system_info = f"{Colors.GREEN}OS: {platform.system()}{Style.RESET_ALL}"
    machine_info = f"{Colors.GREEN}Machine: {platform.machine()}{Style.RESET_ALL}"
    user_info = f"{Colors.GREEN}User: {os.getlogin()}{Style.RESET_ALL}"
    release_info = f"{Colors.GREEN}Release: {platform.release()}{Style.RESET_ALL}"
    version_info = f"{Colors.GREEN}Version: {platform.version()}{Style.RESET_ALL}"

    cpu_info = get_cpu_info()

    gpu_info = get_gpu_info()

    memory_info = get_memory_info()

    print(f"{Colors.CYAN}CATerminal Custom Info for Windows{Style.RESET_ALL}")
    print(system_info)
    print(release_info)
    print(version_info)
    print(machine_info)
    print(user_info)
    print(cpu_info)
    print(gpu_info)
    print(memory_info)

def show_help():
    print(f"{Colors.CYAN}CATerminal Commands:{Style.RESET_ALL}")
    print(f"{Colors.RED}RED{Style.RESET_ALL} = Important, {Colors.MAGENTA}Pink{Style.RESET_ALL} = funny, {Colors.CYAN}CYAN{Style.RESET_ALL} = ok?")
    print(f"{Colors.MAGENTA}cat{Style.RESET_ALL} - Who had the idea to make this??!!")
    print(f"{Colors.RED}catinfo{Style.RESET_ALL} - Display system information.")
    print(f"{Colors.RED}clear{Style.RESET_ALL} - Clear the terminal screen.")
    print(f"{Colors.RED}cmd{Style.RESET_ALL} - {Colors.RED}haha very funny, you cannot use cmd here...{Style.RESET_ALL}")
    print(f"{Colors.CYAN}winget{Style.RESET_ALL} - Run the Windows Package Manager (winget).")
    print(f"{Colors.CYAN}exit{Style.RESET_ALL} - Exit CATerminal.")
    print(f"{Colors.CYAN}help{Style.RESET_ALL} - Show this help message.")
    print(f"{Colors.MAGENTA}rizz{Style.RESET_ALL} - a rizz line??")
    print(f"{Colors.YELLOW}dance{Style.RESET_ALL} - catdance is real!!11!")
    print(f"{Colors.GREEN}sing{Style.RESET_ALL} - meow")
    print(f"{Colors.BLUE}whoami{Style.RESET_ALL} - CATerminal introduction")
    print(f"{Colors.MAGENTA}uwu{Style.RESET_ALL} - Don't do this...")
    print(f"{Colors.CYAN}vim, nano, emacs, notepad{Style.RESET_ALL} - There's no file editors here.")

warnings = 0
uwu_mode = False
rickroll_code = "CRAZYTERMINAL"

while True:
    if uwu_mode:
        command = "uwu"
    else:
        current_directory = os.getcwd()
        command = input(f"{Colors.CYAN}{os.getlogin()}@{platform.node()}${Style.RESET_ALL} ")

    if command.lower() == "cat":
        print(f"{Colors.PINK}meow{Style.RESET_ALL}")
    elif command.lower() == "catinfo":
        catinfo()
    elif command.lower() == "clear":
        os.system("cls" if os.name == "nt" else "clear")
    elif command.lower() in ["exit", "quit"]:
        print(f"{Colors.RED}Exiting CATerminal. Goodbye!{Style.RESET_ALL}")
        break
    elif command.lower() == "help":
        show_help()
    elif command.lower() in ["vim", "nano", "emacs", "notepad"]:
        print(f"{Colors.MAGENTA}This is not an actual serious terminal, so... there's no file editors.{Style.RESET_ALL}")
    elif command.lower() == "cmd":
        if warnings == 0:
            print(f"{Colors.RED}dude i said you cannot use CMD inside CATerminal{Style.RESET_ALL}")
        elif warnings == 1:
            print(f"{Colors.RED}if you do that, i might as well just close myself and open your serious cmd thingy!!{Style.RESET_ALL}")
        elif warnings == 2:
            print(f"{Colors.RED}I'm serious, this is the last warning!!{Style.RESET_ALL}")
        elif warnings == 3:
            print(f"{Colors.RED}Closing CATerminal and opening CMD... Goodbye!{Style.RESET_ALL}")
            time.sleep(2)  
            os.system("start cmd")
            break
        warnings += 1
    elif command.lower() == "winget":
        os.system("winget")
    elif command.lower() == "rizz":
        print(f"{Colors.MAGENTA}are you a cat? cause you're cool{Style.RESET_ALL}")
    elif command.lower() == "dance":
        print(f"{Colors.YELLOW}Lets groove to and i wonder if you know how it feels{Style.RESET_ALL}")
    elif command.lower() == "sing":
        print(f"{Colors.GREEN}Meow?? (cats dont know how to sing){Style.RESET_ALL}")
    elif command.lower() == "whoami":
        print(f"{Colors.BLUE}Meow meow CATerminal, meow meow meow meow!!{Style.RESET_ALL}")
        print(f"Made by {Colors.RED}XRCafe{Style.RESET_ALL}")
    elif command.lower() == "uwu":
        if not uwu_mode:
            print(f"{Colors.MAGENTA}Uwuifying the terminal... (Restart to revert){Style.RESET_ALL}")
            uwu_mode = True
        else:
            print("Uwu")
    elif command.upper() == rickroll_code:
        print(f"{Colors.RED}You've been rickrolled!!{Style.RESET_ALL}")
    else:
        # You can add more custom commands here
        print(f"{Colors.MAGENTA}Unknown command: {command}.{Style.RESET_ALL}")
