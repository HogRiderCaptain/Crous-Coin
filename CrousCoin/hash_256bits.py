import hashlib

def hash256(message_encode):
    """Fonction pour créer le hashage d'un message encode passé en paramètre. Ici on hash 2 fois pour plus de sécurité.
    L'encodage choisi est le big indian d'ou le big comme 2ème paramètre de int.from_bytes."""
    return int.from_bytes(hashlib.sha256(hashlib.sha256(message_encode).digest()).digest(), 'big')

