from tqdm import tqdm
from colorama import Fore

def scan_password_list(file):

    print("\nScanning password list...\n")

    with open(file, "r", errors="ignore") as f:
        passwords = f.readlines()

    weak_count = 0

    for password in tqdm(passwords):

        password = password.strip()

        if len(password) < 8:
            print("Weak password:", password)
            weak_count += 1

    print("\nScan completed")
    print("Total passwords:", len(passwords))
    print("Weak passwords:", weak_count)
