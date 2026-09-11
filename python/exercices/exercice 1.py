def creer_inventaire():
    return {
        "ordinateur_portable": 12,
        "imprimante_laser": 4,
        "tablette": 7,
    }
def ajouter_materiel(inventaire, appareil, quantite):
    if appareil not in inventaire:
        inventaire[appareil] = quantite
    return inventaire

def mettre_a_jour_stock(inventaire, appareil, nombre):
    if appareil in inventaire:
        inventaire[appareil] = nombre
    return inventaire

def supprimer_materiel(inventaire, appareil):
    if appareil in inventaire:
        return (appareil, inventaire.pop(appareil))

    def afficher_inventaire(inventaire):
        for appareil in inventaire:
            print(f"{appareil} : {inventaire[appareil]}")

    def trier_inventaire(inventaire):
        return sorted(inventaire.items(), key=lambda x: x[1], reverse=False)