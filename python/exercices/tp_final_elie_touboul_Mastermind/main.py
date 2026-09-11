import random
def generer_combinaison():
    combinaison = []
    for i in range(4):
        chiffre = random.randint(0,6)
        combinaison.append(chiffre)
    return combinaison

#print(generer_combinaison())

def demander_proposition():
    while True:
        saisie = input("veuillez entré 4 chiffre seulement ")
        if len(saisie) == 4  and saisie.isdigit():
            proposition = [int(combinaison) for combinaison in saisie]
            return proposition
        else :
            print("votre saisie n'est pas valide veuilly reessayer avec une saisie valide")
#print(demander_proposition())

def comparer(combinaison, proposition):
    bien_places = 0
    mal_places = 0
    for i in range(len(combinaison)):
        if combinaison[i] == proposition[i]:
            bien_places  += 1
        elif proposition[i] in combinaison:
            mal_places += 1
    return bien_places, mal_places
#print(comparer([1, 2, 3, 4], [1, 3, 2, 5]))

def afficher_historique(historique):
    for proposition, bien_places, mal_places in historique:
        print(f"proposition : {proposition}, bien_places : {bien_places}, mal_places : {mal_places} ")

#afficher_historique([([1, 4, 3, 2], 1, 2), ([1, 2, 3, 4], 2, 1)])


