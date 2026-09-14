import random
def generer_combinaison():
    combinaison = [random.randint(0,6) for i in range (4)]
    return combinaison
#print(generer_combinaison())

def demander_proposition():
    while True:
        saisie = input("veuillez entré 4 chiffre entre 0 et 6 uniquement\n")
        if len(saisie) == 4  and saisie.isdigit():
            proposition = [int(combinaison) for combinaison in saisie]
            return proposition
        else :
            print("votre saisie n'est pas valide veuillez reessayer avec 4 chifre seulement")
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

def jouer():
    combinaison = generer_combinaison()
    historique = []
    tentative_effectuer = 0
    while tentative_effectuer < 10:
        print(f"tentative restente {10 - tentative_effectuer}")
        proposition = demander_proposition()
        tentative_effectuer += 1
        bien_places, mal_places = comparer(combinaison, proposition)
        historique.append((proposition, bien_places, mal_places))
        afficher_historique(historique)
        if bien_places == 4 :
            print("felicitation!! vous avez gagné")
            break
    else:
        print(f"vous avez perdu, le nombre dessaie maximum a été attain le code secret était: {combinaison}")

while True:
    jouer()
    while True:
        rejouer = input("voulez vous rejouer une partie (y/n)")
        if rejouer == "y" or rejouer == "n":
            break
        else:
            print("réponse invalide tapez y ou n")
    if rejouer == "n":
        break