from Point import Point

from FieldElement import FieldElement
import unittest

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
            
if __name__ == '__main__':
    unittest.main()