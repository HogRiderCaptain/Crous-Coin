from FieldElement import FieldElement
from Point import Point
P=2**256 - 2**32 - 977
N=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

class S256Field(FieldElement):
        
    def __init__(self,num,prime=None):
        super().__init__(num,prime=P)
        
    def __repr__(self):
        return '{:x}'.format(self.num).zfill(64)

A,B = 0,7
class S256Point(Point):
    def __init__(self, x,y ,a=None, b=None):
        a,b = S256Field(A),S256Field(B)
        if type(x) == int:
            super().__init__(S256Field(x),S256Field(y),a,b)
        else:
            super().__init__(x,y,a,b)
            
    def __repr__(self):
        if self.x is None:
            return '256Point(infinity)'
        return '256Point({},{})_{}_{}'.format(self.x, self.y, A, B)

    def __rmul__(self, coefficient):
        coef = coefficient%N  #avec NG = 0
        return super().__rmul__(coef)

G = S256Point(
 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)

print(N*G) #--> infinity exemple1

#P=eG  P->Public key e->Private key
z = 0xbc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
px = 0x04519fac3d910ca7e7138f7013706f619fa8f033e6ec6e09370ea38cee6a7574
py = 0x82b51eab8c27c66e26c858a079bcdf4f1ada34cec420cafc7eac1a42216fb6c4
point = S256Point(px, py)
s_inv = pow(s, N-2, N)

u = z * s_inv % N
v = r * s_inv % N

print((u*G + v*point).x.num == r)


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
print(n*G)"""