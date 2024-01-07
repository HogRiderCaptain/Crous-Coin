from FieldElement import FieldElement
from Point import Point

P = 2**256 - 2**32 - 977
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
A, B = 0, 7

class S256Field(FieldElement):
    
    def __init__(self,num,prime=None):
        """Initialisation de la class avec une valeur num. L'init est simplement le même que celui du 
        FieldElement, avec comme prime le P choisi"""
        super().__init__(num,prime=P)
        
    def __repr__(self):
        """Fonction overwrite pour remplacer l'affichage de l'objet S256Field en affichant l'hexadécimal
        de l'élément du corps."""
        return '{:x}'.format(self.num).zfill(8)


class S256Point(Point):
    def __init__(self, x, y, a=None, b=None):
        """Initialisation de la class avec les coordonnées x,y. L'init est simplement le même que celui du 
        FieldElement, avec comme a et b de l'équation les fieldElements A et B choisis"""
        a, b = S256Field(A), S256Field(B)
        if type(x) == int:
            super().__init__(x=S256Field(x), y=S256Field(y), a=a, b=b)
        else:
            super().__init__(x=x, y=y, a=a, b=b)
            
    def __repr__(self):
        """Fonction overwrite pour remplacer l'affichage de l'objet S256Point en affichant l'hexadécimal
        de l'objet Point. Si celui si est un point null(ou infini), il bénéficie d'una affichage spéciale."""
        if self.x is None:
            return '256Point(infinity)'
        return '256Point({},{})_{}_{}'.format(self.x, self.y, A, B)

    def __rmul__(self, coefficient):
        """Fonction qui retourne le produit d'un 256Point avec un coefficient. Le seule ajout avant d'appeler
        la fonction rmul de Point et que le coefficient est d'abord passé au modulo N pour s'assurer que le 
        produit restera dans le corps et ne le dépassera donc pas."""
        coef = coefficient%N  #avec NG = 0
        return super().__rmul__(coef)

    def verify(self, z, signature):
        """Fonction permettant dfe vérifier la signature. Elle prend donc en paramètre la signature ainsi que le
        message encodé. Ici il suffit de réinverser la signature obtenu et de réappliquer une série d'opération
        pour retomber sur le produit d'un nombre random et le point générateur G."""
        s_inv = pow(signature.s, N-2, N)
        u = s_inv * z % N
        v = s_inv * signature.r.num % N
        V = u*G + v*self
        return V.x == signature.r

G = S256Point(
 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
#print((N-1)*G)