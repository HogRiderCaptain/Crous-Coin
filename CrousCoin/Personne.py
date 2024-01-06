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
