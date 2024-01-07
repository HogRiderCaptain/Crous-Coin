
from hash_256bits import hash256


class Block:
    def __init__(self, transa):
        self.prev = "0x0"
        self.transa = transa
        self.pW = 0
        self.hash = self.get_hash()

    def get_hash(self):
        return hex(hash256(str(self.prev).encode()+self.transa_to_encode() + str(self.pW).encode()))
        
    def proofOfWork(self):
        while not self.verify_block():
            self.pW += 1
        return self.pW
        
    def transa_to_encode(self):
        txt = ""
        for i in self.transa:
            txt += str(i)
            # txt += "\n"
        return txt.encode()

    def __repr__(self):
        block_repr = f"Prev Code: {self.prev[2:].zfill(64)} \n\n"

        block_repr += f"Transactions : \n"
        for i in self.transa:
            block_repr += str(i) + "\n"
        block_repr += f"Proof of Work: {self.pW}\n"
        block_repr += f"Hash block: {self.hash[2:].zfill(64)}"
        final_repr = f"+----------------------------------------------------------------------------+\n{block_repr}\n+----------------------------------------------------------------------------+"

        return final_repr

    def block_is_full(self):
        return len(self.transa) == 5


    def verify_block(self):
        return hash256(str(self.prev).encode() + self.transa_to_encode() + str(self.pW).encode()) < 2 ** 236 and self.block_is_full()


class BlockChain:
    def __init__(self):
        self.size = 0
        self.chain = []

    def __repr__(self):
        blockchain_repr = ""
        for i in range(self.size):
            objet = self.chain[i]
            if i > 0:
                blockchain_repr += f"\n{' ' * 26}||| \n{' ' * 26}VVV\n"
            blockchain_repr += str(objet)
        return blockchain_repr

    def add(self, block):
        if self.size == 0 and block.block_is_full():
            self.chain.append(block)
            self.size += 1
        elif block.block_is_full():
            block.prev = self.chain[-1].hash
            block.pW = block.proofOfWork()
            self.chain.append(block)
            self.size += 1
        else:
            print("Pour créer un bloc il nous faut 5 transactions")

    def index_block(self, block):
        for i in range(self.size):
            if self.chain[i] == block:
                return i

    def verify_block_chain(self):
        for block in self.chain:
            if not block.verify_block():
                return False
        return True

# TEEEEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSST
