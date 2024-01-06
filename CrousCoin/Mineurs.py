from blockChain import Block
from time import time,sleep
from random import randint

class Mineur:
    
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = 0
    
    def __eq__(self,other):
        if other is None:
            return False
        return self.name == other.name and self.wallet == other.wallet
    
    def __ne__(self,other):
        return not(self.__eq__(other))
    
   def create_block(self, transa, bc):
        t = time()
        Block = block(transa)
        self.minage_bloc(Block, bc)
        sleep(randint(0, 5))
        t -= time()
        return Block, -t

    def get_rewards(self, fastest):
        if self.eq(fastest):
            self.wallet += 10
            print("Mineur " + self.name + " a été le plus performant, il remporte 10MC")
        else:
            print("Mineur " + self.name + " a été trop lent")

    def minage_bloc(self, bloc, bc):
        if bc.size > 0:
            bloc.prev = bc.chain[-1].hash
        bloc.pW = bloc.proofOfWork()
    
    
