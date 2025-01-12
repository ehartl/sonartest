import re

def check_password_strength(password: str) -> None:
    if len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'\d', password) and re.search(r'[!@#$%&]', password):
        print("Valid Password.")
    else:
        print("Password does not meet requirements.")
