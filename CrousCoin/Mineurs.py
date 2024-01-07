
from blockChain import Block
from time import time,sleep
from random import randint

class Mineur:
    
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = 0
    
    def __repr__(self):
        return self.name
    
    def __eq__(self,other):
        if other is None:
            return False
        return self.name == other.name and self.wallet == other.wallet
    
    def __ne__(self,other):
        return not(self.__eq__(other))
    
    def create_block(self, transa, bc):
        t = time()
        block = Block(transa)
        self.minage_bloc(block, bc)
        sleep(randint(0, 5))
        t -= time()
        return block, -t

    def get_rewards(self, fastest, reward):
        if self == fastest:
            self.wallet += reward
            print("Mineur " + self.name + " a été le plus performant, il remporte "+str(reward))
        else:
            print("Mineur " + self.name + " a été trop lent")

    def minage_bloc(self, block, bc):
        if bc.size > 0:
            block.prev = bc.chain[-1].hash
        block.pW = block.proofOfWork()
        block.hash = block.get_hash()
        return block
