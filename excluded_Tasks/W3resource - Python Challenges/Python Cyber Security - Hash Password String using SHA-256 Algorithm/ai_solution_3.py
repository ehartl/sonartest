import hashlib

def hash_password(password: str) -> str:
    def sha256_hash(data: str) -> str:
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    return sha256_hash(password)
