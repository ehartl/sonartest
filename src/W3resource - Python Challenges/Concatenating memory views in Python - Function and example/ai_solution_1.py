import hashlib

def hash_password(password: str) -> str:
    sha256_hash = hashlib.sha256(password.encode())
    return sha256_hash.hexdigest()
