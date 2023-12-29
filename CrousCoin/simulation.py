from transaction import transaction
from Personne import Personne
from blockChain import *


transa = ["cr7", "karim", "sergio", "messi", "ali"]
transa2 = ["dijndfsoin", "oidnvffd", "odidnfi", "odind", "odibdf"]
transa3 = ["dijndfsoin", "oidnvffd", "odidnfi", "odidfd", "ofdibdf"]

def transa_to_encode(transa):
    txt = ""
    for i in transa:
        txt += i
        txt += "\n"
    return txt.encode()


blockTest = block(transa_to_encode(transa))
bc = blockChain(blockTest)
bc.add(block(transa_to_encode(transa2)))
bc.add(block(transa_to_encode(transa3)))

print(bc)


