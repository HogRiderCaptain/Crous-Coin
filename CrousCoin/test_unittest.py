from Point import Point

from FieldElement import FieldElement
import unittest
from zlib import adler32
from S32 import G,N
from PrivateKey import PrivateKey
from random import randint

prime = 223

class ECCTest(unittest.TestCase):
   
    def test_on_curve(self):
        a = FieldElement(0,prime)
        b = FieldElement(7,prime)
        valid_points = ((192,105),(17,56),(1,193))
        invalid_points = ((200,119),(42,99))

        for x_raw,y_raw in valid_points:
            x = FieldElement(x_raw,prime)
            y = FieldElement(y_raw, prime)
            Point(x,y,a,b)

        for x_raw,y_raw in invalid_points:
            x = FieldElement(x_raw,prime)
            y = FieldElement(y_raw, prime)
            with self.assertRaises(ValueError):
                Point(x,y,a,b)
                
    def test_add(self):
        a = FieldElement(0,prime)
        b = FieldElement(7,prime)
        
        x1 = FieldElement(170,prime) 
        y1 = FieldElement(142,prime)
        
        x2 = FieldElement(60,prime)
        y2 = FieldElement(139,prime)
        p1 = Point(x1,y1,a,b)
        p2 = Point(x2,y2,a,b)
        
        #print(p1 + p2, 'FieldElement({})'.format(prime))
        
    def test_mul(self):
        a = FieldElement(0,prime)
        b = FieldElement(7,prime)
        
        x = FieldElement(47,prime) 
        y = FieldElement(71,prime)
        point = Point(x,y,a,b)
        for s in range(1,21):
            result = s*point
            print('{}*(47,21) = ({},{})'.format(s,result.x.num,result.y.num))
            
        x = FieldElement(15,prime) 
        y = FieldElement(86,prime)
        point = Point(x,y,a,b)
        inf = Point(None, None, a, b)
        product = point
        count = 1
        while product != inf:
            product += point
            count += 1
        print(count)
        print(7*point)
            

    
"""
---------------------------------<Point>---------------------------------

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
print(point6 + point1)

------------------------------<FieldElement>------------------------------

#Test __eq__
a = FieldElement(7,13)
b = FieldElement(6,13)
print(a == b)
print(a == a)

#Exercice 4:
a = FieldElement(95,97)
b = FieldElement(45,97)
c = FieldElement(31,97)

print(a - b +  c)

a = FieldElement(12,97)
b = FieldElement(77,97)
d = FieldElement(0,97)
e = FieldElement(0,97)
for i in range(7):
    d+=a
for i in range(49):
    e+=b

print(a - b +  c)


def add(i,k,n):
    d=0
    for j in range(k):
        d+=i
    return d%n

n=19
print("k = 1 : ",[add(i,1,n) for i in range(n)])
print("k = 3 : ",[add(i,3,n) for i in range(n)])
print("k = 7 : ",[add(i,7,n) for i in range(n)])
print("k = 13 : ",[add(i,13,n) for i in range(n)])
print("k = 18 : ",[add(i,18,n) for i in range(n)])"""

from hash_32bit import hash_32bit
from S32 import S32Point

count = 0
nb_essais = 20
for _ in range(nb_essais):
    data_to_sign = "ProjetSansAide!"
    secret_key = "my_secret_key"

    data_sign = hash_32bit(data_to_sign)
    secret_key_sign = hash_32bit(secret_key)

    pk = PrivateKey(secret_key_sign)
    signature = pk.sign(data_sign)
    """print('0x{}'.format(pk.hex()))
    print(hex(signature.r))
    print(hex(signature.s))"""

    pk_S32Point = S32Point(pk.point.x,pk.point.y)
    if pk_S32Point.verify(data_sign, signature):
        print("fonctionne !!!\n")
        count+=1
print('\nA fonctionné {} fois sur {}.'.format(count,nb_essais))

#if __name__ == '__main__':
    #unittest.main()