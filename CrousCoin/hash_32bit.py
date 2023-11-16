import hashlib

def hash_32bit(data):
    # Utilisez SHA-256 pour créer un hachage
    sha256_hash = hashlib.sha256(data.encode('utf-8'))
    hash_value = int(sha256_hash.hexdigest(), 16)

    # Tronquer la sortie pour obtenir les 32 bits
    truncated_hash = hash_value & 0xFFFFFFFF  # Masque pour conserver seulement les 32 bits

    return truncated_hash
