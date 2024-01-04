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
        data_sign = hash32(input.name.encode() + output.name.encode() + str(amount).encode() + str(numT).encode())
        self.signature = input.sk.sign(data_sign)
        while not (input.pk.verify(data_sign, self.signature)):
            self.signature = input.sk.sign(data_sign)



        self.input.modifyMC(-amount)
        self.output.modifyMC(amount)

    def __repr__(self):
        return "{} envoi {}MC à {}".format(self.input.name, self.amount, self.output.name)

    def verifyGentil(self):
        if self.amount > self.input.wallet:
            return False
        return True



y = Personne("Youssef", 10000000000000000000000)
a = Personne("Ali", 0)

t = transaction(y, a, 1000000000000, 0)
print(t.signature, a.wallet, y.wallet)


data_sign = hash32(y.name.encode()+t.output.name.encode()+str(t.amount).encode()+str(t.numT).encode())
print(y.pk.verify(data_sign, t.signature))












