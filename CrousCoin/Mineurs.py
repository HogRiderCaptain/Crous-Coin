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
    
    def create_block(self,transa):
        t = time()
        block = Block(transa)
        sleep(randint(0,5))
        t-= time()
        return block,-t
    
    def get_rewards(self,fastest):
        if self.__eq__(fastest):
            self.wallet += 10
            print("Mineur " + self.name + " a été le plus performant, il remporte 10MC")
        else:
            print("Mineur " + self.name + " a trop lent")
    
    