from Personne import Personne
from PrivateKey import PrivateKey
from hash_32bit import hash32
from S32 import G,N

class transaction:
    def __init__(self, input, output, amount, numT):
        self.input = input
        self.output = output
        self.amount = amount
        self.numT = numT

        self.signature = input.sk.sign(self.data_sign())
        self.appliquer_transa()

    def data_sign(self):
        return hash32(self.input.name.encode() + self.output.name.encode() + str(self.amount).encode() + str(self.numT).encode())
    def __repr__(self):
        return "Tx num {} : {} envoi {}MC à {}.".format( self.numT, self.input.name, self.amount, self.output.name)

    def verify_amount(self):
        if self.amount > self.input.wallet:
            return False
        return True

    def verify_transa(self):
        return self.input.pk.verify(self.data_sign(), self.signature)

    def appliquer_transa(self):
        if self.verify_amount() and self.verify_transa():
            self.input.modifyMC(-self.amount)
            self.output.modifyMC(self.amount)
        return

"""y = Personne("Youssef? Gay ?", 10000000000000000000000, "gayd'andorre.")
a = Personne("Ali", 0, "goat212.")

t = transaction(a, y, 1000000000000, 0)
print(t.signature, a.wallet, y.wallet)

data_sign = hash32(y.name.encode()+t.output.name.encode()+str(t.amount).encode()+str(t.numT).encode())
print(y.pk.verify(data_sign, t.signature))"""












