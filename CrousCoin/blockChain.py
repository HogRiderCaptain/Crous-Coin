from hash_256bits import hash256


class Block:

    def __init__(self, transa):
        self.prev = "0x0"
        self.transa = transa
        self.pW = self.proofOfWork()
        self.hash = hex(hash256(str(self.prev).encode() + self.transa_to_encode() + str(self.pW).encode()))

    def transa_to_encode(self):
        txt = ""
        for i in self.transa:
            txt += str(i)
            # txt += "\n"
        return txt.encode()

    def __repr__(self):
        block_repr = f"Prev Code: {self.prev} \n\n"

        block_repr += f"Transactions : \n"
        for i in self.transa:
            block_repr += str(i) + "\n"
        self.transa = []
        block_repr += f"Proof of Work: {self.pW}\n"
        block_repr += f"Hash block: {self.hash}"
        final_repr = f"+----------------------------------------------------------------------------+\n{block_repr}\n+----------------------------------------------------------------------------+"

        return final_repr

    def proofOfWork(self):
        c = 0
        hash_c = str(self.prev).encode() + self.transa_to_encode() + str(c).encode()
        while hash256(hash_c) > 2**240:
            c += 1
            hash_c = str(self.prev).encode() + self.transa_to_encode() + str(c).encode()
        return c

    def block_is_full(self):
        return len(self.transa) == 5


    def verify_block(self):
        return hash256(str(self.prev).encode() + self.transa_to_encode() + str(self.pW).encode()) < 2 ** 240 and self.block_is_full()


class BlockChain:

    def __init__(self, block):
        self.size = 1
        self.chain = [block]

    def __repr__(self):
        blockchain_repr = ""
        for i in range(self.size):
            objet = self.chain[i]
            if i > 0:
                blockchain_repr += f"\n{' ' * 26}||| \n{' ' * 26}VVV\n"
            blockchain_repr += str(objet)
        return blockchain_repr

    def add(self, block):
        if block.block_is_full():
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