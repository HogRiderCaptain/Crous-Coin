#import matplotlib.pyplot as plt
from FieldElement import FieldElement

class Point:
 
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return 
        if (self.y)**2 != (self.x)**3 + self.a * x + self.b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))
  
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b
        
    def __ne__(self, other):
        return not(self.__eq__(other))
    
    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format(self, other))

        if self.x is None:
            return other
        
        if other.x is None:
            return self
        
        if self.x == other.x and self.y != other.y:
            return Point(None, None, self.a, self.b)

        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s**2 - self.x - other.x
            y = s * (self.x - x) - self.y
            return Point(x, y, self.a, self.b)

        if self == other and self.y == 0 * self.x:
            return Point(None, None, self.a, self.b)

        if self == other:
            s = (3 * self.x**2 + self.a) / (2 * self.y)
            x = s**2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return Point(x, y, self.a, self.b)

    def __rmul__(self, coefficient):
        coef = coefficient
        current = self
        result = Point(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1
        return result
        
    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return 'Point({},{})_{}_{} FieldElement({})'.format(
                self.x.num, self.y.num, self.a.num, self.b.num, self.x.prime)
        else:
            return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)
        
"""
#Exo 4       
point1 = Point(2,5,5,7)
point2 = Point(-1,-1,5,7)
point3 = point1 + point2
print(point3)

#Exo 6
point4 = point2.__add__(point2)
print(point4.__repr__())

#Exo 7
point5 = Point(1,0,0,-1)
point5 = point5.__add__(point5)
print(point5.__repr__())

#Test en deuspi
print("\nTest None + None")
point6 = Point(None,None,5,7)
print(point6.__add__(point6))
print("\nTest Point1 + None")
print(point1 + point6)
print("\nTest None + Point1")
print(point6 + point1)"""