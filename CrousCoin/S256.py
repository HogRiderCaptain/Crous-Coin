from FieldElement import FieldElement
from Point import Point
P=2**256 - 2**32 - 977

class S256Field(FieldElement):
        
    def __init__(self,num,prime=None):
        super().__init__(num,prime=P)
        
    def __repr__(self):
        return '{:x}'.format(self.num)

A,B = 0,7
class S256Point(Point):
    def __init__(self,x,y,a=None,b=None):
        a,b = S256Field(A),S256Field(B)
        if type(x) == int:
            super().__init__(S256Field(x),S256Field(y),a,b)
        else:
            super().__init__(x,y,a,b)
        
    def __repr__(self):
        return '{:x}'.format(self.num)

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