from transaction import transaction
from Personne import Personne
from blockChain import *
from random import choice, randint
from mineurs import Mineur

Brand = Personne("Brand", 1000, "jaimelecaca")
Sergio = Personne("Sergio", 1000, "jesuispd")
Youss = Personne("Mugsy99", 1000, "fumernetuepas")
personne = Personne("Levy", 1000, "jsp")
Ali = Personne("Goat", 1000, "goatultime.")

mineur = Mineur("Mineur", 0)

#transactions = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
n = 0
goats = [Brand, Sergio, Youss, personne, Ali]

mineurs = [Mineur("Rtx4080", 0), Mineur("Rtx4090", 0), Mineur("Rtx5090", 0), Mineur("Rtx4070", 0)]


numT = 0
transactions = []
bc = blockChain()



def print_resultats(fastest):
    for mineur in mineurs:
        mineur.get_rewards(fastest)

def minage(bloc):
    liste_tps = []
    bloc_mine = bloc
    for mineur in mineurs:
        bloc_mine, tps = mineur.create_block(bloc.transa, bc)
        liste_tps.append(tps)

    print("Block " + bloc_mine.hash)
    print("----------------------")
    print_resultats(mineurs[liste_tps.index(min(liste_tps))])
    print("----------------------")
    print("")

    return bloc_mine

for i in range(4):
    while len(transactions) < 5:
        input = choice(goats)
        output = choice(goats)
        while output == input:
            output = choice(goats)
        amount = randint(0, 1000)
        while input.wallet < amount:
            amount = randint(0, 1000)
        transactions.append(transaction(input, output, amount, numT))
        numT+=1

    bloc = block(transactions)
    bc.add(minage(bloc))

    transactions = []

print(bc)
