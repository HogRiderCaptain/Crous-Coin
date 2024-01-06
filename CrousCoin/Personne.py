<<<<<<< HEAD
from hash_256bits import hash256
from PrivateKey import *

class Personne:
    def __init__(self, name, wallet, mdp):
        self.name = name
        self.wallet = wallet
        self.sk = PrivateKey(hash256(mdp.encode()))
        self.pk = self.sk.secret*G

    def __repr__(self):
        return "{} possède {}MC".format(self.name, self.wallet)

    def modifyMC(self, amount):
        self.wallet += amount
=======
from hash_256bits import hash256
from PrivateKey import *

class Personne:
    def __init__(self, name, wallet, mdp):
        self.name = name
        self.wallet = wallet
        self.sk = PrivateKey(hash256(mdp.encode()))
        self.pk = self.sk.secret*G

    def __repr__(self):
        return "{} possède {}MC".format(self.name, self.wallet)

    def modifyMC(self, amount):
        self.wallet += amount
>>>>>>> c43a8e61742a36c5474e07e7851ba98b2d8ed839
