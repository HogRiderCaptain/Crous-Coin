from hash_32bit import hash32
from transaction import transaction
class block:
    
    def __init__(self, transa):
        self.prev = "0x0"
        self.transa = transa
        self.pW = self.proofOfWork()

    def transa_to_encode(self):
        txt = ""
        for i in self.transa:
            txt += str(i)
            txt += "\n"
        return txt.encode()
    
    def __repr__(self):
        block_repr = f"Prev Code: {self.prev} \n\n"


        block_repr += f"Transactions : \n"
        for i in self.transa:
            block_repr += str(i)+"\n"

        block_repr += f"Proof of Work: {self.pW}\n"
        block_repr += f"Hash block: {self.hash_block()}"
        final_repr = f"+----------------------------+\n{block_repr}\n+----------------------------+"

        return final_repr
    
    def proofOfWork(self):
        i = 0
        hash_c = str(self.prev).encode()+self.transa_to_encode() + str(i).encode()
        while len(str(hex(hash32(hash_c)))) > 9:
            i += 1
            hash_c = str(self.prev).encode()+self.transa_to_encode() + str(i).encode()
        return i

    def block_is_full(self):
        return len(self.transa) == 5

    def add_transa(self, transa):
        if not self.block_is_full() and transa.verify_amount():
            self.transa.append(transa)

    def hash_block(self):
        return hex(hash32(str(self.prev).encode()+self.transa_to_encode() + str(self.pW).encode()))



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
        if block.block_is_full():
            block.prev = self.chain[-1].hash_block()
            block.pW = block.proofOfWork()
            self.chain.append(block)
            self.size += 1
        else:
            print("Pour créer un bloc il nous faut 5 transactions")

    def index_block(self, block):
        for i in range(self.size):
            if self.chain[i] == block:
                return i

    def verify_block(self, block):
        index_block = self.index_block(block)
        if index_block == 0 :
            return self.chain[0].prev == "0x0" and self.chain[0].hash_block()<2**28
        else:
            return self.chain[index_block].prev==self.chain[index_block-1].hash_block() and self.verify_block(self.chain[index_block-1]) and self.chain[index_block].hash_block()<2**28



#TEEEEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSST






