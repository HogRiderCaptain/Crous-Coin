
from hash_256bits import hash256
from PrivateKey import *

class Personne:
    def __init__(self, name, wallet, mdp):
        """Initialisation de la class avec un nom, un porte-feuille et un mot de passe (utilisé 
        pour la clé privé qui sera alors différent pour deux personnes avec le même nom)."""
        self.name = name
        self.wallet = wallet
        self.sk = PrivateKey(hash256(mdp.encode()))
        self.pk = self.sk.secret*G

    def __repr__(self):
        """Fonction overwrite pour remplacer l'affichage de l'objet Personne en affichant 
        simplement son nom et le contenu de son porte-feuille."""
        return "{} possède {}MC".format(self.name, self.wallet)

    def modifyMC(self, amount):
        """Fonction pour ajouter ou retirer une quantité (amount) de son porte-feuille."""
        self.wallet += amount
