
from blockChain import Block
from time import time,sleep
from random import randint

class Mineur:
    
    def __init__(self, name, wallet):
        """Initialisation de la class avec le nom du mineur ainsi que le porte-feuille de celui-ci."""
        self.name = name
        self.wallet = 0
    
    def __repr__(self):
        """Fonction overwrite pour remplacer l'affichage de l'objet mineur en affichant simplement son nom."""
        return self.name
    
    def __eq__(self,other):
        """Fonction overwrite pour tester l'égalité entre deux mineurs (même nom et même porte-feuille). 
        Nous partons du principe que deux mineurs ne doivent pas avoir le même nom."""
        if other is None:
            return False
        return self.name == other.name and self.wallet == other.wallet
    
    def __ne__(self,other):
        """Fonction overwrite pour tester l'inégalité entre deux mineurs (vérifiant qu'ils ont le même nom et 
        le même porte-feuille)."""
        return not(self.__eq__(other))
    
    def create_block(self, transa, bc):
        """Fonction permettant le minage d'un bloc. Elle prend en paramètre un tableau de transactions et la 
        chaine de bloc. On utilise la biblio time afin de mesurer le temps mis à miner un bloc selon la chaine.
        La fonction time() recupère l'heure actuelle tandis que sleep(t) endort le processur pour t secondes.
        Elle retourne le bloc miné ainsi que la durée de son minage."""
        t = time()
        block = Block(transa)
        self.minage_bloc(block, bc)     # Minage du bloc
        sleep(randint(0, 5))            # S'endort pendant un nbnre aléatoire entre 0 et 5 secondes
        t -= time()                     # heure de lancement - heure de finition du minage
        return block, -t                # return du bloc et de -t car t<0 et que l'on souhaite une durée > 0 par simplicité

    def get_rewards(self, fastest, reward):
        """Fonction qui gère les récompenses des mineurs. Les paramètres sont le mineur le plus rapide, et la 
        récompenses à attribuer."""
        if self == fastest:                                                                        # test pour savoir si le mineur question est celui qui a été le plus rapide
            self.wallet += reward
            print("Mineur " + self.name + " a été le plus performant, il remporte "+str(reward))   # affichage si le mineur question est celui qui a été le plus rapide
        else:
            print("Mineur " + self.name + " a été trop lent")                                      # affichage si le mineur question n'est pas celui qui a été le plus rapide

    def minage_bloc(self, block, bc):
        """Fonction qui gère le minage appelée par la fonction create_block. Elle incrémente le bloc en conséquent de
        la chaine bc en changeant son prev (si besoin), sa proofOfWork ainsi que son hash et le retourne."""
        if bc.size > 0:
            block.prev = bc.chain[-1].hash
        block.pW = block.proofOfWork()
        block.hash = block.get_hash()
        return block
