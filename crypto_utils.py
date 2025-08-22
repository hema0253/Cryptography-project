import hashlib

def hash_identity(identity: str, secret: str) -> str:
    combined = f"{identity}:{secret}"
    return hashlib.sha256(combined.encode()).hexdigest()

def verify_identity(identity: str, secret: str, received_hash: str) -> bool:
    expected_hash = hash_identity(identity, secret)
    return expected_hash == received_hash
