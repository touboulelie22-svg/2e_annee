import random
def generer_combinaison():
    combinaison = []
    for i in range(4):
        chiffre = random.randint(0,6)
        combinaison.append(chiffre)
    return combinaison

print(generer_combinaison())