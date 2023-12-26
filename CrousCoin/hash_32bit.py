import hashlib

def hash256(z):
    return hashlib.sha256(hashlib.sha256(z).digest()).digest()

def hash32(z):
    return int.from_bytes(hash256(z)[:4], 'big')