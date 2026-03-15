import re
from colorama import Fore
from passcheck.modules.entropy import calculate_entropy


def check_strength(password):

    entropy = calculate_entropy(password)

    print("\nEntropy:", round(entropy, 2), "bits")

    if entropy < 28:
        print(Fore.RED + "Strength: VERY WEAK")

    elif entropy < 36:
        print(Fore.YELLOW + "Strength: WEAK")

    elif entropy < 60:
        print(Fore.BLUE + "Strength: STRONG")

    else:
        print(Fore.GREEN + "Strength: VERY STRONG")
