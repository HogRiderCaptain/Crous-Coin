<<<<<<< HEAD
import hashlib

def hash256(z):
    return int.from_bytes(hashlib.sha256(hashlib.sha256(z).digest()).digest(), 'big')
=======
import hashlib

def hash256(z):
    return int.from_bytes(hashlib.sha256(hashlib.sha256(z).digest()).digest(), 'big')



>>>>>>> c43a8e61742a36c5474e07e7851ba98b2d8ed839
