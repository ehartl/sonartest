import hashlib
import os

def hash_password(password: str) -> str:
    salt = os.urandom(16)
    sha256_hash = hashlib.sha256(salt + password.encode())
    return sha256_hash.hexdigest()
