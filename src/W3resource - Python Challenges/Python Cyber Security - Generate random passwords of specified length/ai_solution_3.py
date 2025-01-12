import os
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(characters[os.urandom(1)[0] % len(characters)] for _ in range(length))
    return password
