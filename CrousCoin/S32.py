from FieldElement import FieldElement
from Point import Point
from zlib import adler32

P=4294956461
N=715826077
A,B = 0,8

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

    def verify(self, message_encode, sig):
        s_inv = pow(sig.s, N-2, N)
        u = message_encode*s_inv % N
        v = sig.r*s_inv % N
        total = u*G + v*self
        return total.x.num == sig.r

G = S32Point(1,3)