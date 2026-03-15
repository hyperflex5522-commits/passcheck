import hashlib
from tqdm import tqdm
from colorama import Fore

def crack_hash(hash_value, wordlist):

    try:
        with open(wordlist, "r", errors="ignore") as f:
            passwords = f.readlines()

        for password in tqdm(passwords):

            password = password.strip()

            hashed = hashlib.md5(password.encode()).hexdigest()

            if hashed == hash_value:
                print("\nPassword found:", password)
                return

        print("\nPassword not found in wordlist")

    except FileNotFoundError:
        print("Wordlist file not found.")
