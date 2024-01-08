#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#////////////////////////////////////////////// Imports des Class //////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
from blockChain import *
from FieldElement import *
from hash_256bits import *
from Mineurs import *
from Personne import *
from Point import *
from PrivateKey import *
from S256 import *
from Signature import *
from transaction import *
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////// Personne ////////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
Brand = Personne("Brand", 100, "brand123")
Sergio = Personne("Sergio", 100, "laroja34")
Youss = Personne("Mugsy99", 100, "andorrayehaw")
Ali = Personne("Goat", 100, "goatultime.")
personne = Personne("Goat", 100, "goatultime.")
"""print(Brand)
print(Sergio)
print(Youss)
print(Ali)
print(personne)"""
print("----------------------------<EQ Personne>---------------------------------")
try:
    assert Brand != Ali
except AssertionError:
    print("Test Class Personne: KO")
else:
    print("Test Class Personne: OK")
try:
    assert Sergio != Youss
except AssertionError:
    print("Test Class Personne: KO")
else:
    print("Test Class Personne: OK")
try:
    assert Ali == personne
except AssertionError:
    print("Test Class Personne: KO")
else:
    print("Test Class Personne: OK")
try:
    assert personne == personne
except AssertionError:
    print("Test Class Personne: KO")
else:
    print("Test Class Personne: OK")
try:
    assert Youss != Youss
except AssertionError:
    print("Test Class Personne: OK")
else:
    print("Test Class Personne: KO")
print("------------------------<modifyMC Personne>-------------------------------")    
for _ in range(1,3):
    try:
        personne.wallet = 100
        personne.modifyMC(-10*_)
        assert personne.wallet == 100-(10*_)
    except AssertionError:
        print("Test ModifyMC Personne: KO")
    else:
        print("Test ModifyMC Personne: OK")
for _ in range(3,6):
    try:
        personne.wallet = 100
        personne.modifyMC(-10*_)
        assert personne.wallet == 1000
    except AssertionError:
        print("Test ModifyMC Personne: OK")
    else:
        print("Test ModifyMC Personne: KO")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////// FieldElement /////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
print("--------------------------<Init FieldElement>-----------------------------")
prime = 223
for _ in range(2):
    try:
        f = FieldElement(_,10)
    except ValueError:
        print("Test FieldElement Valides: KO")
    else:
        print("Test FieldElement Valides: OK")  
for _ in range(3):
    try:
        f = FieldElement(77,_)
    except ValueError:
        print("Test FieldElement Invalides: OK")
    else:
        print("Test FieldElement Invalides: KO")
print("---------------------------<ADD FieldElement>-----------------------------")
for _ in range(1,3):
    try:
        a = FieldElement(170,prime) 
        b = FieldElement(142,prime+_)
        c = a + b     
    except TypeError:
        print("Test ADD FieldElement Invalides: OK")
    else:
        print("Test ADD FieldElement Invalides: KO")  
for _ in range(1,4):
    try:
        a = FieldElement(170,prime+5*_) 
        b = FieldElement(142,prime+5*_)
        c = a + b  
    except TypeError:
        print("Test ADD FieldElement Valides: KO")
    else:
        print("Test ADD FieldElement Valides: OK")
print("---------------------------<SUB FieldElement>-----------------------------")
for _ in range(1,3):
    try:
        a = FieldElement(170,prime) 
        b = FieldElement(142,prime+_)
        c = a - b     
    except TypeError:
        print("Test SUB FieldElement Invalides: OK")
    else:
        print("Test SUB FieldElement Invalides: KO")  
for _ in range(1,4):
    try:
        a = FieldElement(170,prime+5*_) 
        b = FieldElement(142,prime+5*_)
        c = a - b  
    except TypeError:
        print("Test SUB FieldElement Valides: KO")
    else:
        print("Test SUB FieldElement Valides: OK")
print("---------------------------<MUL FieldElement>-----------------------------")
for _ in range(1,3):
    try:
        a = FieldElement(170,prime) 
        b = FieldElement(142,prime+_)
        c = a * b     
    except TypeError:
        print("Test MUL FieldElement Invalides: OK")
    else:
        print("Test MUL FieldElement Invalides: KO")  
for _ in range(1,4):
    try:
        a = FieldElement(170,prime+5*_) 
        b = FieldElement(142,prime+5*_)
        c = a * b  
    except TypeError:
        print("Test MUL FieldElement Valides: KO")
    else:
        print("Test MUL FieldElement Valides: OK")
print("---------------------------<POW FieldElement>-----------------------------")
for _ in range(1,3):
    try:
        a = FieldElement(170,prime) 
        b = FieldElement(142,prime+_)
        c = a ** b     
    except TypeError:
        print("Test POW FieldElement Invalides: OK")
    else:
        print("Test POW FieldElement Invalides: KO")  
for _ in range(1,4):
    try:
        a = FieldElement(170,prime+5*_) 
        c = a ** _  
    except TypeError:
        print("Test POW FieldElement Valides: KO")
    else:
        print("Test POW FieldElement Valides: OK")
print("-------------------------<TrueDIV FieldElement>---------------------------")
for _ in range(1,3):
    try:
        a = FieldElement(170,prime) 
        b = FieldElement(142,prime+_)
        c = a / b     
    except TypeError:
        print("Test TrueDIV FieldElement Invalides: OK")
    else:
        print("Test TrueDIV FieldElement Invalides: KO")  
for _ in range(1,4):
    try:
        a = FieldElement(170,prime+5*_) 
        b = FieldElement(5,prime+5*_)
        c = a / b  
    except TypeError:
        print("Test TrueDIV FieldElement Valides: KO")
    else:
        print("Test TrueDIV FieldElement Valides: OK")
print("--------------------------<RMUL FieldElement>-----------------------------")
for _ in range(1,3):
    try:
        a = FieldElement(170,prime+_) 
        a = _ * a     
    except AttributeError:
        print("Test RMUL FieldElement Invalides: KO")
    else:
        print("Test RMUL FieldElement Invalides: OK")  
for _ in range(1,4):
    try:
        a = FieldElement(170,prime+5*_) 
        a = a * _  
    except AttributeError:
        print("Test RMUL FieldElement Valides: OK")
    else:
        print("Test RMUL FieldElement Valides: KO")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#/////////////////////////////////////////////////// Points ////////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
print("----------------------------<Init Points>---------------------------------")
a = FieldElement(0,prime)
b = FieldElement(7,prime)
c = FieldElement(0,prime)
d = FieldElement(1,prime)  
valid_points = ((192,105),(17,56),(1,193))
invalid_points = ((200,119),(42,99))
for x_raw,y_raw in valid_points:
    try:
        x = FieldElement(x_raw,prime)
        y = FieldElement(y_raw, prime)
        Point(x,y,a,b)
    except ValueError:
        print("Test Points Valides: K0")
    else:
        print("Test Points Valides: OK")

for x_raw,y_raw in invalid_points:
    try:    
        x = FieldElement(x_raw,prime)
        y = FieldElement(y_raw, prime)
        Point(x,y,a,b)
    except ValueError:
        print("Test Points Invalides: OK")
    else:
        print("Test Points Invalides: KO") 
print("----------------------------<ADD Points>----------------------------------")    
x1 = FieldElement(170,prime) 
y1 = FieldElement(142,prime)     
x2 = FieldElement(60,prime)
y2 = FieldElement(139,prime)
x3 = FieldElement(2 ,prime)
y3 = FieldElement(3,prime)
p1 = Point(x1,y1,a,b)
p2 = Point(x2,y2,a,b)
p3 = Point(x3,y3,c,d)
p4 = p3
try:
    p1 += p3
except TypeError:
    print("Test ADD Invalides: OK")
else:
    print("Test ADD Invalides: KO")
try:
    p2 += p3 
except TypeError:
    print("Test ADD Invalides: OK")
else:
    print("Test ADD Invalides: KO") 
try:
    p1 += p2
except TypeError:
    print("Test ADD Valides: KO")
else:
    print("Test ADD Valides: OK")
try:
    p3 += p3
except TypeError:
    print("Test ADD Valides: KO")
else:
    print("Test ADD Valides: OK")
try:
    p3 += p4
except TypeError:
    print("Test ADD Valides: KO")
else:
    print("Test ADD Valides: OK")
print("----------------------------<RMul Points>---------------------------------")             
try:
    p1 = p1 * p3
except TypeError:
    print("Test RMul Invalides: OK")
else:
    print("Test RMul Invalides: KO")
try:
    p2 = p2 * p3
except TypeError:
    print("Test RMul Invalides: OK")
else:
    print("Test RMul Invalides: KO") 
try:
    p3 = 2*p3
except TypeError:
    print("Test RMul Valides: KO")
else:
    print("Test RMul Valides: OK")
try:
    p2 = 69*p3
except TypeError:
    print("Test RMul Valides: KO")
else:
    print("Test RMul Valides: OK")
try:
    p1 = 21*p3
except TypeError:
    print("Test RMul Valides: KO")
else:
    print("Test RMul Valides: OK")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#////////////////////////////////////////////////// Mineurs ////////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#  
mineur_test = Mineur("Rtx4090",Sergio)      
mineurs = [Mineur("Rtx4080",Brand), Mineur("Rtx4060ti", Youss), Mineur("Gtx1650", Ali)]
mineurs2 = [Mineur("Rtx4090",Sergio) , Mineur("Rtx4090",Sergio)]
print("------------------------------<EQ Mineurs>--------------------------------") 
for _ in mineurs2:
    a = _ == mineur_test
    if a:
        print("Test EQ Mineurs Valides: OK")
    else:
        print("Test EQ Mineurs Valides: KO")
for _ in mineurs:
    a = _ != mineur_test
    if a:
        print("Test NE Mineurs Valides: OK")
    else:
        print("Test NE Mineurs Valides: KO")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////// Transaction //////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
Sergio.wallet,Youss.wallet = 500,500
print("-----------------------------<Transaction>--------------------------------") 
for _ in range(5):
    try:
        t1 = transaction(Sergio, Youss, 50, _+1)
    except ValueError:
        print("Test transaction Valides: KO")
    else:
        print("Test transactions Valides: OK")
        
Sergio.wallet,Youss.wallet = 0,0 
t1 = transaction(Sergio, Youss, 50, _+1) 
for _ in range(5):
    try:
        t1 = transaction(Sergio, Youss, 50, _+1)
    except ValueError:
        print("Test transaction Invalides: KO")
    else:
        print("Test transactions Invalides: OK")