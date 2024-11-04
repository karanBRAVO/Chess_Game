from colorama import Fore, Back, Style, init

init()


def print_warn(text: str):
    print(Fore.WHITE + Back.YELLOW + Style.BRIGHT +
          text + Fore.RESET + Back.RESET + Style.RESET_ALL)


def print_info(text: str):
    print(Fore.WHITE + Back.CYAN + Style.BRIGHT +
          text + Fore.RESET + Back.RESET + Style.RESET_ALL)


def print_success(text: str):
    print(Fore.WHITE + Back.GREEN + Style.BRIGHT +
          text + Fore.RESET + Back.RESET + Style.RESET_ALL)


def print_error(text: str):
    print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT +
          text + Fore.RESET + Back.RESET + Style.RESET_ALL)
