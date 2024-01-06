from transaction import transaction
from Personne import Personne
from blockChain import *
from random import choice, randint
from Mineurs import Mineur

Brand = Personne("Brand", 1000, "jaimelecaca")
Sergio = Personne("Sergio", 1000, "jesuispd")
Youss = Personne("Mugsy99", 1000, "fumernetuepas")
personne = Personne("Levy", 1000, "jsp")
Ali = Personne("Goat", 1000, "goatultime.")

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



mineurs = [Mineur("Rtx4080",0),Mineur("Rtx4090",0),Mineur("Rtx4060ti",0),Mineur("Rtx4070",0),Mineur("Rtx4060",0)]
list_time = [0 for i in range(len(mineurs))]

block = None
for _ in range(len(mineurs)):
    block,list_time[_] = mineurs[_].create_block(transactions[0])
print(block.hash)   
min = list_time[0]
fastest_block = mineurs[0]
for _ in range(1,len(list_time)):
    if list_time[_] < min:
        min = list_time[_]
        fastest_block = mineurs[_]

for _ in mineurs:
    _.get_rewards(fastest_block)

bc = BlockChain(block)

for i in transactions[1:]:
    for _ in range(len(mineurs)):
        block,list_time[_] = mineurs[_].create_block(i)
    print(block.hash)
    min = list_time[0]
    fastest_block = mineurs[0]
    for _ in range(1,len(list_time)):
        if list_time[_] < min:
            min = list_time[_]
            fastest_block = mineurs[_]

    for _ in mineurs:
        _.get_rewards(fastest_block)
    
    bc.add(block)
        


#print(Brand.wallet, Ali.wallet, Youss.wallet, personne.wallet, Sergio.wallet)
for _ in mineurs:
    print(_.name + ": " + str(_.wallet) + "MC\n")
    
print(bc)