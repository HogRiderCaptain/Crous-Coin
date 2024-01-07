import hashlib

def hash256(z):
    return int.from_bytes(hashlib.sha256(hashlib.sha256(z).digest()).digest(), 'big')

