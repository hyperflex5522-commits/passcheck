#!/usr/bin/env python3

import argparse
import getpass
import sys
from colorama import Fore, Style, init

from passcheck.modules.strength import check_strength
from passcheck.modules.scanner import scan_password_list
from passcheck.modules.cracker import crack_hash

init(autoreset=True)


def banner():

    print(Fore.CYAN + r"""
██████╗  █████╗ ███████╗███████╗ ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██║ ██╔╝
██████╔╝███████║███████╗███████╗██║     █████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║     ██╔═██╗
██║     ██║  ██║███████║███████║╚██████╗██║  ██╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝
""" + Style.RESET_ALL)

    print(Fore.YELLOW + "PASSCHECK - Password Security Tool")
    print(Fore.BLUE + "Version : 1.0")
    print(Fore.BLUE + "Author  : Security CLI Tool\n")


def info(msg):
    print(Fore.CYAN + "[INFO] " + msg)


def success(msg):
    print(Fore.GREEN + "[SUCCESS] " + msg)


def error(msg):
    print(Fore.RED + "[ERROR] " + msg)


def main():

    banner()

    parser = argparse.ArgumentParser(
        description="PassCheck - Password Security Toolkit"
    )

    parser.add_argument(
        "-p",
        "--password",
        nargs="?",
        help="Check password strength"
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Scan password list"
    )

    parser.add_argument(
        "-H",
        "--hash",
        help="Hash to crack"
    )

    parser.add_argument(
        "-w",
        "--wordlist",
        help="Wordlist for cracking"
    )

    args = parser.parse_args()

    # HASH CRACKING MODE
    if args.hash and args.wordlist:
        info("Starting hash cracking...")
        crack_hash(args.hash, args.wordlist)
        return

    # PASSWORD STRENGTH MODE
    if args.password is not None or "-p" in sys.argv:

        if args.password:
            password = args.password
        else:
            password = getpass.getpass("Enter password: ")

        info("Checking password strength...\n")
        check_strength(password)
        return

    # PASSWORD LIST SCAN MODE
    if args.file:
        info("Scanning password list...\n")
        scan_password_list(args.file)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
