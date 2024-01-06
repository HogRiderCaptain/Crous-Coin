from hash_256bits import hash256
from Personne import Personne


class transaction:
    def __init__(self, input, output, amount, numT):
        self.input = input
        self.output = output
        self.amount = amount
        self.numT = numT
        self.signature = input.sk.sign(self.data_sign())
        self.appliquer_transa()


    def data_sign(self):
        return hash256(self.input.name.encode() + self.output.name.encode() + str(self.amount).encode() + str(self.numT).encode())
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
















