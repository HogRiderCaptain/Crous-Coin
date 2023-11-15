from Signature import Signature 
from S32 import G,N

class PrivateKey:
    def __init__(self, secret):
        self.secret = secret
        self.point = secret*G
        
    def hex(self):
        return '{:x}'.format(self.secret).zfill(64)

    def sign(self, z):
        k = self.deterministic_k(z)
        r = (k*G).x.num
        k_inv = pow(k, N-2,N)
        s = (z+r*self.secret)*k_inv%N
        if s > N/2:
            s = N-s
        return Signature(r, s)

    def deterministic_k(self, z):
        k = b'\x00' * 32
        v = b'\x01' * 32
        if z > N:
            z -= N
        z_bytes = z.to_bytes(32, 'big')
        secret_bytes = self.secret.to_bytes(32, 'big')
        s32 = hashlib.sha32
        k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s32).digest()
        v = hmac.new(k, v, s32).digest()
        k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s32).digest()
        v = hmac.new(k, v, s32).digest()
        while True:
            v = hmac.new(k, v, s32).digest()
            candidate = int.from_bytes(v, 'big')
            if candidate >= 1 and candidate < N:
                return candidate
            k = hmac.new(k, v + b'\x00', s32).digest()
            v = hmac.new(k, v, s32).digest()