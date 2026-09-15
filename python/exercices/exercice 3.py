from datetime import date

class Tache:
    def __init__(self, titre, description, date_limite, terminee=False):
        self.titre = titre
        self.description = description
        self.date_limite = date_limite
        self.terminee = terminee

    def afficher(self):
        statut = "Terminée" if self.terminee else "En attente"
        print(f"Titre       : {self.titre}")
        print(f"Description : {self.description}")
        print(f"Date limite : {self.date_limite}")
        print(f"Statut      : {statut}")
        print()


def ajouter_tache(liste_taches, tache):
    for t in liste_taches:
        if t.titre.lower() == tache.titre.lower():
            print(f"Erreur : la tâche '{tache.titre}' existe déjà.")
            return
    liste_taches.append(tache)
    print(f"Tâche '{tache.titre}' ajoutée avec succès.")


def supprimer_tache(liste_taches, titre):
    for t in liste_taches:
        if t.titre.lower() == titre.lower():
            liste_taches.remove(t)
            print(f"Tâche '{titre}' supprimée.")
            return
    print(f"Erreur : aucune tâche trouvée avec le titre '{titre}'.")


def marquer_comme_terminee(liste_taches, titre):
    for t in liste_taches:
        if t.titre.lower() == titre.lower():
            t.terminee = True
            print(f"Tâche '{titre}' marquée comme terminée.")
            return
    print(f"Erreur : aucune tâche trouvée avec le titre '{titre}'.")


def afficher_taches(liste_taches):
    print("=== Tâches en attente ===")
    for t in liste_taches:
        if not t.terminee:
            t.afficher()

    print("=== Tâches terminées ===")
    for t in liste_taches:
        if t.terminee:
            t.afficher()

def afficher_menu():
    print("""
=== GESTION DE TACHES ===
[1] Ajouter une tâche
[2] Supprimer une tâche
[3] Marquer comme terminée
[4] Afficher les tâches
[0] Quitter
""")


def demander_date():
    saisie = input("Date limite (YYYY-MM-DD) : ").strip()
    try:
        y, m, d = saisie.split("-")
        return date(int(y), int(m), int(d))
    except ValueError:
        raise ValueError("Format de date invalide. Exemple attendu : 2025-12-25")


def demander_tache():
    titre = input("Titre : ").strip()
    description = input("Description : ").strip()
    if not titre:
        raise ValueError("Le titre ne peut pas être vide.")
    dl = demander_date()
    return Tache(titre, description, dl)


def jouer():
    taches = []
    choix_utilisateur = ""

    while choix_utilisateur != "0":
        afficher_menu()
        choix_utilisateur = input("Ton choix : ").strip()

        try:
            if choix_utilisateur == "1":
                t = demander_tache()
                ajouter_tache(taches, t)

            elif choix_utilisateur == "2":
                titre = input("Titre à supprimer : ").strip()
                supprimer_tache(taches, titre)

            elif choix_utilisateur == "3":
                titre = input("Titre à marquer terminée : ").strip()
                marquer_comme_terminee(taches, titre)

            elif choix_utilisateur == "4":
                afficher_taches(taches)

            elif choix_utilisateur == "0":
                print("A bientôt !")

            else:
                print("Choix invalide. Réessaie.")

        except ValueError as msg:
            print(f"Erreur : {msg}")


jouer()