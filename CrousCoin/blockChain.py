
from hash_256bits import hash256


class Block:
    def __init__(self, transa):
        """Initialisation de la class avec un tableau contenant des transitions effectués par les personnes. 
        L'objet Block possède alors un attribut prev qui représente le hashage du bloc précédent (init à 0x0 par 
        choix), un attribut pour les transactions ainsi que la proof of work du bloc calculé dans un fonction 
        tiers. Le dernier attribut est le hashage du bloc (utile pour le prev du bloc suivant dans la chaine)."""
        self.prev = "0x0"
        self.transa = transa
        self.pW = 0
        self.hash = self.get_hash()

    def get_hash(self):
        """Fonction pour retourner le hashage du bloc en utilisant la fonction hash256 de notre projet.
        Il suffit de "coller" tous les attributs encodés de notre bloc et passer le string dans le hashage."""
        return hex(hash256(str(self.prev).encode()+self.transa_to_encode() + str(self.pW).encode()))
        
    def proofOfWork(self):
        """Fonction qui permet de vérifier la validité d'un bloc. Elle consiste simplement à tester 1 à 1 toutes 
        les possibilités jusqu'à trouver la bonne valeur tel qu'il y a 5x 0 devant (dans notres cas)."""
        while not self.verify_block():
            self.pW += 1
        return self.pW
        
    def transa_to_encode(self):
        """Fonction qui permet d'encoder la liste de transactions à l'aide d'un simple boucle sur l'attribut
        transa du bloc passée en paramètre."""
        txt = ""
        for i in self.transa:
            txt += str(i)
            # txt += "\n"
        return txt.encode()

    def __repr__(self):
        """Fonction d'overwrite qui remplace l'affichage d'un bloc sous une forme plus esthétique contenant les 
        3 attributs que l'on souhaite afficher: prev,transa,proofOfWork. """
        block_repr = f"Prev Code: {self.prev[2:].zfill(64)} \n\n"   # self.prev[2:].zfill(64) permet l'affichage de 0x015 à la 
        block_repr += f"Transactions : \n"                          # place de 0x15 (le premier zéro n'ai jamais affiché sinon)
        for i in self.transa:
            block_repr += str(i) + "\n"
        block_repr += f"Proof of Work: {self.pW}\n"
        block_repr += f"Hash block: {self.hash[2:].zfill(64)}"
        final_repr = f"+----------------------------------------------------------------------------+\n{block_repr}\n+----------------------------------------------------------------------------+"

        return final_repr

    def block_is_full(self):
        """Fonction qui retourne le booléen vérifiant que le bloc possède 5 transactions (limites que nous nous 
        sommes fixés)."""
        return len(self.transa) == 5


    def verify_block(self):
        """Fonction pour vérifier le bloc. Elle retourne un booléen prenant en compte que le bloc contient 5 transa 
        et que le hashage est inférieur à 2^236. Cela implique que le code hexadécimal possède au moins 5x 0."""
        return hash256(str(self.prev).encode() + self.transa_to_encode() + str(self.pW).encode()) < 2 ** 236 and self.block_is_full()

class BlockChain:
    def __init__(self):
        """Initialisation de la class avec une taille de 0 (chaine de bloc vide) et un tableau vide également"""
        self.size = 0
        self.chain = []

    def __repr__(self):
        """Fonction d'overwrite qui remplace l'affichage d'une blockChain sous une forme plus esthétique contenant les 
        bloc un à un."""
        blockchain_repr = ""
        for i in range(self.size):
            objet = self.chain[i]
            if i > 0:
                blockchain_repr += f"\n{' ' * 26}||| \n{' ' * 26}VVV\n"
            blockchain_repr += str(objet)
        return blockchain_repr

    def add(self, block):
        """Fonction permettant d'ajouter un bloc passé en paramètre à une chaine."""
        if self.size == 0 and block.block_is_full():                # vérifie que le bloc est complet (contient 5 transactions)
            self.chain.append(block)
            self.size += 1
        elif self.size != 0 and block.block_is_full():              # vérifie que le bloc est complet (contient 5 transactions) + si la taille est diff de 0 alors 
            block.prev = self.chain[-1].hash                        # le prev du bloc est modifié selon le bloc qui le précède
            block.pW = block.proofOfWork()
            self.chain.append(block)
            self.size += 1
        else:
            print("Pour créer un bloc il nous faut 5 transactions") # Ce print n'est jamais affiché car une vérification tiers et toujours effectué.
                                                                    # Cependant nous laissons ceci pour des tests unitaires

    def index_block(self, block):
        """Fonction permmettant de récuperer l'indice d'un bloc dans une chaine effectué par une simple boucle 
        de parcours linéaire."""
        for i in range(self.size):
            if self.chain[i] == block:
                return i

    def verify_block_chain(self):
        """Fonction vérifiant que la chaine est correct en vérifiant la totalité de chque bloc par prevention."""
        for block in self.chain:
            if not block.verify_block():
                return False
        return True