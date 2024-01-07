import hashlib
import hmac
from Signature import Signature
from S256 import G, N

class PrivateKey:
    
    def __init__(self, secret):
        self.secret = secret
        self.point = secret*G
        
    def hex(self):
        return '{:x}'.format(self.secret).zfill(4)

    def sign(self, z):
        k = self.deterministic_k(z)
        R = k*G
        k_inv = pow(k,N-2,N)
        s = k_inv * (z + self.secret*R.x.num) % N
        if s > N / 2:
            s = N - s
        return Signature(R.x, s)

    def deterministic_k(self, z):
        k = b'\x00' * 32
        v = b'\x01' * 32
        if z > N:
            z -= N
        z_bytes = z.to_bytes(32, 'big')
        secret_bytes = self.secret.to_bytes(32, 'big')
        s256 = hashlib.sha256
        k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        while True:
            v = hmac.new(k, v, s256).digest()
            candidate = int.from_bytes(v, 'big')
            if candidate >= 1 and candidate < N:
                return candidate
            k = hmac.new(k, v + b'\x00', s256).digest()
            v = hmac.new(k, v, s256).digest()
