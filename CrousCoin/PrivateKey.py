import hashlib
import hmac
from random import randint
from Signature import Signature 
from S32 import G,N

class PrivateKey:
    
    def __init__(self, secret):
        self.secret = secret
        self.point = secret*G
        
    def hex(self):
        return '{:x}'.format(self.secret).zfill(4)

    def sign(self, z):
        k = randint(0,N)
        R = k*G
        k_inv = pow(k,N-2,N)
        s = k_inv * (z + self.secret*R.x.num) % N
        return Signature(R.x, s)
