
from hash_256bits import hash256
from Personne import Personne


class transaction:
    def __init__(self, input, output, amount, numT):
        """Initialisation de la class avec l'indice de transaction (numT), la quantité (amount) ainsi que les objets 
        Personne  input et output (pour expéditeur et receveur respectivement)."""
        self.input = input
        self.output = output
        self.amount = amount
        self.numT = numT
        self.signature = input.sk.sign(self.data_sign())    # Signature de la transaction
        self.appliquer_transa()                             # application des transactions aux personnes concernées


    def data_sign(self):
        """Fonction pour retourner le hashage des transactions en utilisant la fonction hash256 de notre projet.
        Il suffit de "coller" tous les attributs encodés, à savoir le nom des personnes concernés la quantité et 
        le numéro de la transa pour éviter les doublons et passer le string dans le hashage."""
        return hash256(self.input.name.encode() + self.output.name.encode() + str(self.amount).encode() + str(self.numT).encode())
        
    def __repr__(self):
        """Fonction overwrite pour remplacer l'affichage de l'objet Transaction en affichant une phrase comportant
        le numéro de transa, le nom de l'expéditeur et celui du receveur ainsi que le nombre de MidlCoin envoyé."""
        return "Tx num {} : {} envoi {}MC à {}.".format( self.numT, self.input.name, self.amount, self.output.name)

    def verify_amount(self):
        """Fonction permettant la vérification de la quantité afin d'éviter qu'une personne puisse dépenser plus que 
        ce qu'elle ne possède."""
        if self.amount > self.input.wallet:
            return False
        return True

    def verify_transa(self):
        """Fonction vérifiant que la signature de la transa c'est bien effectué."""
        return self.input.pk.verify(self.data_sign(), self.signature)

    def appliquer_transa(self):
        """Fonction qui applique les transactions après avoir vérifier que la transaction était possible"""
        if self.verify_amount() and self.verify_transa():
            self.input.modifyMC(-self.amount)
            self.output.modifyMC(self.amount)
        return




