from CrousCoin.hash_32bit import hash32
from PrivateKey import *
class Personne:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.sk = PrivateKey(hash32(name.encode()))
        self.pk = self.sk.secret*G

    def __repr__(self):
        return "{} possède {}MC".format(self.name, self.wallet)

    def modifyMC(self, amount):
        self.wallet += amount
