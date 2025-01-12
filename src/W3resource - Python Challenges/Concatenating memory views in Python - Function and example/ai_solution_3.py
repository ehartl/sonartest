import hashlib

def hash_password(password: str) -> str:
    salt = b'some_predefined_salt'
    sha256_hash = hashlib.sha256(salt + password.encode())
    return sha256_hash.hexdigest()
