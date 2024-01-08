import hashlib
import hmac
from Signature import Signature
from S256 import G, N

class PrivateKey:
    
    def __init__(self, secret):
        """Initialisation de la class avec la clé secrète. On décide alors de stocker cette clé secrète 
        ainsi que le produit de cette clé et du point générateur."""
        self.secret = secret
        self.point = secret*G
    
    def __eq__(self,other):
        """Fonction overwrite pour tester l'égalité entre deux PrivateKey (même secret, et même points)."""
        return self.secret == other.secret and self.point == other.point
    
    def __ne__(self,other):
        """Fonction overwrite pour tester l'inégalité entre deux PrivateKey."""
        return not(self == other)  
       
    def hex(self):
        """Fonction permmetant le retour de l'hexadécimal de la clé secrète d'un l'objet PrivateKey."""
        return '{:x}'.format(self.secret).zfill(64)

    def sign(self, z):
        """Fonction permettant de signer un message encode z avec l'objet PrivateKey. """
        k = self.deterministic_k(z)                  # appel de la fonction codée juste en-dessous afin de remplacer un randint(0,t) pour un random plus random
        R = k*G                                      # produit de ce k random avec le point générateur G
        k_inv = pow(k,N-2,N)                         # calcul de l'inverse de K avec tips des Corps
        s = k_inv * (z + self.secret*R.x.num) % N    # signature
        if s > N / 2:                                
            s = N - s                                # réduction de la signature si elle est supérieur à la moitié de s
        return Signature(R.x, s)                     # retour de l'objet Signature

    def deterministic_k(self, z):
        """Fonction retournant in nombre random selon un message_encodé."""
        k = b'\x00' * 32
        v = b'\x01' * 32
        if z > N:
            z -= N
        z_bytes = z.to_bytes(32, 'big')
        secret_bytes = self.secret.to_bytes(32, 'big')
        s256 = hashlib.sha256
        k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        while True:
            v = hmac.new(k, v, s256).digest()
            candidate = int.from_bytes(v, 'big')
            if candidate >= 1 and candidate < N:
                return candidate
            k = hmac.new(k, v + b'\x00', s256).digest()
            v = hmac.new(k, v, s256).digest()
