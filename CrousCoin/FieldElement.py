class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    """def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime,self.num)"""
    
    def __eq__(self,other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __ne__(self,other):
        return not(self.__eq__(other))
    
    def __add__(self,other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in differents Fields')
        num = (self.num + other.num)%self.prime
        return FieldElement(num, self.prime)
    
    def __sub__(self,other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in differents Fields')
        num = (self.num - other.num)%self.prime
        return FieldElement(num, self.prime)
    
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return FieldElement(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return FieldElement(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in differents Fields')
        num = (self.num * other.num**(self.prime-2) % self.prime)
        return FieldElement(num, self.prime)
    
    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime
        return FieldElement(num, self.prime)
    
    def __repr__(self):
        return '{}'.format(self.num)

"""
#Test __eq__
a = FieldElement(7,13)
b = FieldElement(6,13)
print(a.__eq__(b))
print(a.__eq__(a))

#Exercice 4:
a = FieldElement(95,97)
b = FieldElement(45,97)
c = FieldElement(31,97)

print((a.__sub__(b)).__add__(c).__repr__())

a = FieldElement(12,97)
b = FieldElement(77,97)
d = FieldElement(0,97)
e = FieldElement(0,97)
for i in range(7):
    d = d.__add__(a)
for i in range(49):
    e = e.__add__(b)

print((a.__sub__(b)).__add__(c).__repr__())


def add(i,k):
    d=0
    for j in range(k):
        d = d.__add__(i)
    return d%19

print("k = 1 : ",[add(i,1) for i in range(19)])
print("k = 3 : ",[add(i,3) for i in range(19)])
print("k = 7 : ",[add(i,7) for i in range(19)])
print("k = 13 : ",[add(i,13) for i in range(19)])
print("k = 18 : ",[add(i,18) for i in range(19)])"""