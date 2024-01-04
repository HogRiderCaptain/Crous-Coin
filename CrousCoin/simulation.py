from transaction import transaction
from Personne import Personne
from blockChain import *
from random import choice, randint





Brand = Personne("Brand", 1000)
Sergio = Personne("Sergio", 1000)
Youss = Personne("Mugsy99", 1000)
personne = Personne("Shingeki", 1000)
Ali = Personne("Goat", 1000)

transactions = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
n=0
goats = [Brand, Sergio, Youss, personne, Ali]

for i in range(len(transactions)):
    for j in range(5):
        input = choice(goats)
        output = choice(goats)
        while output==input:
            output = choice(goats)
        amount = randint(0,1000)
        transactions[i][j] = transaction(input, output, amount, n)
        n+=1


blockTest = block(transactions[0])
bc = blockChain(blockTest)
bc.add(block(transactions[1]))
bc.add(block(transactions[2]))
bc.add(block(transactions[3]))
print(bc)



