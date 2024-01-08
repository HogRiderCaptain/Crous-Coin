#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////// Imports des Class + fonctions ////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
from transaction import transaction
from Personne import Personne
from blockChain import *
from random import choice, randint
from Mineurs import Mineur

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#////////////////////////////////////////// Déclaration des Variables///////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
Brand = Personne("Brand", 100, "brand123")
Sergio = Personne("Sergio", 100, "laroja34")
Youss = Personne("Mugsy99", 100, "andorrayehaw")
personne = Personne("Levy", 100, "idk4000")
Ali = Personne("Goat", 100, "goatultime.")
goats = [Brand, Sergio, Youss, personne, Ali]
mineurs = [Mineur("Rtx4080",Brand),Mineur("Rtx4060",Brand), Mineur("Rtx4090",Sergio), Mineur("Rtx4060ti", Youss), Mineur("Rtx4070", personne), Mineur("Gtx1650", Ali)]
n = 0
numT = 0
reward = 50
transactions = []
bc = BlockChain()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////// Fonctions Simulations/////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#   
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
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////  Simulations ///////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
for i in range(20):                                                     # boucle pour obtenir 20 bloc et donc 100 transactions
    if i % 10 == 0 and i!=0:
        reward = reward/2                                               # halving a chaque 10 blocs minés (division de moitié de la récompense du mineurs)
    while len(transactions) < 5:                                        # boucles permettant d'avoir 5 transactions valides par bloc
        input = choice(goats)                                           # choix random d'une personne qui sera expéditeur du MC
        output = choice(goats)                                          # choix random d'une personne qui sera expéditeur du MC
        while output == input:                                          # Boucle pour éviter d'avoir la même personne en tant qu'input et output
            output = choice(goats)  
        amount = randint(1, input.wallet)                               # valeur à échangé randomisée entre 0 exclu et l'entiereté de son porte feuille inclus
        transactions.append(transaction(input, output, amount, numT))   # tentatives de transactions
        numT += 1
    bloc = Block(transactions)
    bc.add(minage(bloc))
    transactions = []
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////  Affichage /////////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
print(bc)
print(bc.chain[0].transa)
for _ in goats:
    print(_)