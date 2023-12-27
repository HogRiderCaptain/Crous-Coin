from hash_32bit import hash32

class block:
    
    def __init__(self, transa):
        self.prev = "0x"
        self.transa = transa.encode()
        self.pW = self.proofOfWork()
    
    def __repr__(self):
        block_repr = f"Prev Code: {self.prev} \n"
        block_repr += f"Transaction: {self.transa.decode()} \n"
        block_repr += f"Proof of Work: {self.pW} "
        final_repr = f"+----------------------------+\n{block_repr}\n+----------------------------+"

        return final_repr
    
    def proofOfWork(self):
        i=0
        test = self.transa + str(i).encode() 
        while len(str(hex(hash32(test)))) > 9:
            i += 1
            test = self.transa + str(i).encode()
        return i
        
        
class blockChain:
    
    def __init__(self,block):
        self.size = 1
        self.chain = [block]
        
    def __repr__(self):
        blockchain_repr = ""
        for i in range(self.size):
            objet = self.chain[i]
            if i>0:
                blockchain_repr += f"\n{' ' * 13}||| \n{' ' * 13}VVV\n"
            blockchain_repr += str(objet)
        return blockchain_repr
    def add(self, block):
        block.prev = hex(hash32(self.chain[-1].transa + str(self.chain[-1].pW).encode()))
        self.chain.append(block)
        self.size+=1

    def index_block(self, block):
        for i in range(self.size):
            if self.chain[i] == block:
                return i

    def sub(self, block):
        index_block = self.index_block(block)
        if index_block == 0:
            self.chain[1].prev = "0x"
        elif index_block != self.size-1:
            self.chain[index_block+1].prev = block.prev
        self.chain.pop(index_block)
        self.size -= 1
    
    def swap(self, block1, block2):
        index_block1 = self.index_block(block1)
        index_block2 = self.index_block(block2)
        self.chain[index_block1], self.chain[index_block2] = self.chain[index_block2], self.chain[index_block1]
        block1.prev, block2.prev = block2.prev, block1.prev

        #cas1 le plus simple : on swap pas avec le dernier block
        if index_block1<self.size-1 and index_block2<self.size-1:
            self.chain[index_block1+1].prev, self.chain[index_block2+1].prev = self.chain[index_block2+1].prev, self.chain[index_block1+1].prev
        #ya d'autres cas, ça ressemble beaucoup à algo3, il est 4h24 je vais chill et en + jsp si cette fonction va nous servir finalement


#TEEEEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSST
a = block("Sergio")
b = block("Youssef") 
c = block("Ali")
d = block("Brandon")
blockChainTest = blockChain(a)
blockChainTest.add(b)
blockChainTest.add(c)
blockChainTest.add(d)
print(blockChainTest)

print("    ")
print("      zeb")
blockChainTest.swap(a, c)
print(blockChainTest)

