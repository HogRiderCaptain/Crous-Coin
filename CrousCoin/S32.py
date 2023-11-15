from FieldElement import FieldElement
from Point import Point
import hashlib
import hmac
from random import randint
import unittest

P=4294967291

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



A,B = 0,1
G = S32Point(2,3)

N=5
#print(N*G)

class Signature:
    def __init__(self, r, s):
        self.r = r
        self.s = s
    def __repr__(self):
        return 'Signature({:x}, {:x})'.format(self.r, self.s)


"""    pb hash256 
a_string = 'my secret'
e = int(sha256(a_string.encode('utf-8')).hexdigest(), 16)
e = e.from_bytes(e, 'big')
a_string = 'my message'
z = int(sha256(a_string.encode('utf-8')).hexdigest(),16)
z = z.from_bytes(z, 'big')
k = 1234567890
r = (k*G).x.num
k_inv = pow(k, N - 2, N)
s = (z + r * e) * k_inv % N
point = e * G
print(point)
print(hex(z))
print(hex(r))
print(hex(s))
#P=eG  P->Public key e->Private key"""

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

"""gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
p = 2**256 - 2**32 - 977
print(gy**2 % p == (gx**3 + 7) % p)

from FieldElement import FieldElement
from Point import Point

gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
p = 2**256 - 2**32 - 977
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
x = FieldElement(gx, p)
y = FieldElement(gy, p)
seven = FieldElement(7, p)
zero = FieldElement(0, p)
G = Point(x, y, zero, seven)
print(n*G)

class S256Test(unittest.TestCase):

    def test_order(self):
        point = N * G
        self.assertIsNone(point.x)

    def test_pubpoint(self):
        # write a test that tests the public point for the following
        points = (
            # secret, x, y
            (7, 0xcac4f9bc, 0x087264da),
            (1485, 0x5398afda, 0x50901f55),
            (2**128, 0x9ec4c0da, 0x501fff82),
            (2**240 + 2**31, 0x17945116, 0x5e66d053),
        )

        # iterate over points
        for secret, x, y in points:
            # initialize the secp32k1 point (S32Point)
            point = S32Point(x, y)
            # check that the secret*G is the same as the point
            self.assertEqual(secret * G, point)

    def test_verify(self):
        point = S32Point(
            0x8744d06c,
            0x29a0ae34)
        z = 0x003c0f60
        r = 0x10d3a395
        s = 0x1cb423c4
        self.assertTrue(point.verify(z, Signature(r, s)))
        z = 0x7a838a3d
        r = 0xe0529a2c
        s = 0xce6feab6
        self.assertTrue(point.verify(z, Signature(r, s)))

class PrivateKeyTest(unittest.TestCase):

    def test_sign(self):
        pk = PrivateKey(randint(0, N))
        z = randint(0, 2**32)
        sig = pk.sign(z)
        self.assertTrue(pk.point.verify(z, sig))
        
if __name__ == '__main__':
    unittest.main()"""