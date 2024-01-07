from transaction import transaction
from Personne import Personne
from blockChain import *
from random import choice, randint
from Mineurs import Mineur

Brand = Personne("Brand", 100, "brand123")
Sergio = Personne("Sergio", 100, "laroja34")
Youss = Personne("Mugsy99", 100, "andorrayehaw")
personne = Personne("Levy", 100, "idk4000")
Ali = Personne("Goat", 100, "goatultime.")


#transactions = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
n = 0
goats = [Brand, Sergio, Youss, personne, Ali]

mineurs = [Mineur("Rtx4080", 0), Mineur("Rtx4090", 0), Mineur("Rtx4060ti", 0), Mineur("Rtx4070", 0), Mineur("Gtx1650", 0)]


numT = 0
transactions = []
bc = BlockChain()


reward = 50
def print_resultats(fastest):
    for mineur in mineurs:
        mineur.get_rewards(fastest, reward)

def minage(bloc):
    liste_tps = []
    bloc_mine = bloc
    for mineur in mineurs:
        bloc_mine, tps = mineur.create_block(bloc.transa, bc)
        liste_tps.append(tps)

    print("Block " + bloc_mine.hash[2:].zfill(64))
    print("---------------------------------------------------")
    print_resultats(mineurs[liste_tps.index(min(liste_tps))])
    print("---------------------------------------------------")
    print("")

    return bloc_mine

for i in range(20):
    if i % 10 == 0 and i!=0:
        reward = reward/2 #halving a chaque 10 blocs minés
    while len(transactions) < 5:
        input = choice(goats)
        output = choice(goats)
        while output == input:
            output = choice(goats)
        amount = randint(0, input.wallet)
        transactions.append(transaction(input, output, amount, numT))
        numT += 1

    bloc = Block(transactions)
    bc.add(minage(bloc))

    transactions = []

print(bc)

for _ in goats:
    print(_)
for _ in mineurs:
    print(_, ": ", _.wallet)

print(bc.chain[0].transa)




