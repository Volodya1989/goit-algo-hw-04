import sys
from pathlib import Path
from colorama import init, Fore, Style


def print_directory_structure(directory, indent=""):
    try:
        for entry in directory.iterdir():  # Use pathlib's iterdir() to iterate over directory contents
            if entry.is_dir():
                print(
                    f"{indent}{Fore.BLUE}[DIR] {entry.name}{Style.RESET_ALL}")
                print_directory_structure(entry, indent + "  ")
            else:
                print(f"{indent}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[ACCESS DENIED]{Style.RESET_ALL}")


def main():
    init(autoreset=True)  # Initialize colorama

    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python script.py <directory_path>{Style.RESET_ALL}")
        sys.exit(1)

    directory = Path(sys.argv[1])

    if not directory.exists() or not directory.is_dir():
        print(f"{Fore.RED}Error: The specified path does not exist or is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.YELLOW}Directory Structure of: {directory}{Style.RESET_ALL}")
    print_directory_structure(directory)


if __name__ == "__main__":
    main()
