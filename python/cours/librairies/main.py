import pendulum

# Obtenir la date et l'heure actuelles
maintenant = pendulum.now()
print("Heure locale :", maintenant)

# Spécifier un fuseau horaire
paris = pendulum.now("Europe/Paris")
tokyo = pendulum.now("Asia/Tokyo")

print("Heure à Paris :", paris)
print("Heure à Tokyo :", tokyo)

# Créer une date spécifique
evenement = pendulum.datetime(2025, 10, 19, 14, 30, tz="Europe/Paris")
print("Événement :", evenement)

# Ajouter ou soustraire du temps
print("Dans 10 jours :", evenement.add(days=10))
print("Il y a 3 heures :", evenement.subtract(hours=3))

# Calculer la différence entre deux dates
diff = evenement.diff(paris)
print("Différence :", diff.in_days(), "jours")

# Afficher une durée dans un format humain
print("Événement dans :", evenement.diff_for_humans())
