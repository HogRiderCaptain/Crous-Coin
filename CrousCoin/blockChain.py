from hash_32bit import hash32

class block:
    
    def __init__(self, transa):
        self.prev = "0x"
        self.transa = transa.encode()
        self.pW = self.proofOfWork()
    
    def __repr__(self):
        return '| {} / {} / {} |'.format(self.prev,self.transa,self.pW) 
    
    def proofOfWork(self):
        i=0
        test = self.transa + str(i).encode() 
        while len(str(hex(hash32(test)))) > 9:
            i+=1
            test = self.transa + str(i).encode()
        return i
        
        
class blockChain:
    
    def __init__(self,block):
        self.size = 1
        self.chain = [block]
        
    def __repr__(self):
        for i in range(self.size):
            objet = self.chain[i]
            if objet!=None and i<self.size-1:
                print("{} ---> " .format(objet), end='')
            else:
                print("{}" .format(objet), end='')
        return ""
    
    def add(self,block):
        block.prev = hex(hash32(self.chain[-1].transa + str(self.chain[-1].pW).encode()))
        self.chain.append(block)
        self.size+=1
        
    def sub(self, block):
        return
    
    def swap(self, block1, block2):
        return
        
a = block("Sergio")
b = block("Youssef") 
c = block("Ali")
d = block("Brandon")
blockChainTest = blockChain(a)
blockChainTest.add(b)
blockChainTest.add(c)
blockChainTest.add(d)
print(blockChainTest)