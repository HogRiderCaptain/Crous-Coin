from hash_32bit import hash32
from transaction import transaction
class block:
    
    def __init__(self, transa):
        self.prev = "0x0"
        self.transa = transa
        self.pW = self.proofOfWork()


    
    def __repr__(self):
        block_repr = f"Prev Code: {self.prev} \n\n"


        block_repr += f"Transaction : \n{self.transa.decode()} \n"
        block_repr += f"Proof of Work: {self.pW}\n"
        block_repr += f"Hash block: {hex(hash32(str(self.prev).encode()+self.transa + str(self.pW).encode()))}"
        final_repr = f"+----------------------------+\n{block_repr}\n+----------------------------+"

        return final_repr
    
    def proofOfWork(self):
        i=0
        test = str(self.prev).encode()+self.transa + str(i).encode()
        while len(str(hex(hash32(test)))) > 9:
            i += 1
            test = str(self.prev).encode()+self.transa + str(i).encode()
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
        block.prev = hex(hash32(str(self.chain[-1].prev).encode()+self.chain[-1].transa + str(self.chain[-1].pW).encode()))
        block.pW = block.proofOfWork()
        self.chain.append(block)
        self.size += 1

    def index_block(self, block):
        for i in range(self.size):
            if self.chain[i] == block:
                return i


#TEEEEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSST






