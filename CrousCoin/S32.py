from FieldElement import FieldElement
from Point import Point
import hashlib
import hmac
from random import randint
import unittest
from zlib import adler32

P=4294956461
N=715826077

class S32Field(FieldElement):
        
    def __init__(self,num,prime=None):
        super().__init__(num,prime=P)
        
    def __repr__(self):
        return '{:x}'.format(self.num).zfill(8)


class S32Point(Point):
    def __init__(self, x, y, a=None, b=None):
        a, b = S32Field(A), S32Field(B)
        if type(x) == int:
            super().__init__(x=S32Field(x), y=S32Field(y), a=a, b=b)
        else:
            super().__init__(x=x, y=y, a=a, b=b)
            
    def __repr__(self):
        if self.x is None:
            return '32Point(infinity)'
        return '32Point({},{})_{}_{}'.format(self.x, self.y, A, B)

    def __rmul__(self, coefficient):
        coef = coefficient%N  #avec NG = 0
        return super().__rmul__(coef)

    def verify(self, z, sig):
        s_inv = pow(sig.s, N-2, N)
        u = z*s_inv % N
        v = sig.r*s_inv % N
        total = u*G+v*self
        return total.x.num == sig.r



A,B = 0,8
G = S32Point(1,3)
#print(N*G)

class Signature:
    def __init__(self, r, s):
        self.r = r
        self.s = s
        
    def __repr__(self):
        return 'Signature({:x}, {:x})'.format(self.r, self.s)



e = adler32(b'my secret')
z = adler32(b'my message')

k = 10
r = (k*G).x.num
k_inv = pow(k, N - 2, N)
s = (z + r * e) * k_inv % N
point = e * G
print(point)
print(hex(z))
print(hex(r))
print(hex(s))
#P=eG  P->Public key e->Private key

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