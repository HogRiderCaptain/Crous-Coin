from FieldElement import FieldElement
from Point import Point
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