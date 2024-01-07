class Signature:
    def __init__(self, r, s):
        """Initialisation de la class avec le produit du nombre random et le générateur G 
        (ici r) et s la signature."""
        self.r = r
        self.s = s
        
    def __repr__(self):
        """Fonction overwrite pour remplacer l'affichage de l'objet Signature seulement 
        l'hexadécimal de la valeur entière de la signature."""
        return 'Signature : {}'.format(hex(self.s))