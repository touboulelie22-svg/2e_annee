class Fraction:
    def __init__(self, numerateur, denominateur):
        if not isinstance(numerateur, int) or not isinstance(denominateur, int):
            raise TypeError("Le numerateur et le denominateur doivent etre des entiers")
        if denominateur == 0:
            raise ValueError("Le denominateur ne peut etre nul")
        self.numerateur = numerateur
        self.denominateur = denominateur

    def quotient(self):
        return self.numerateur / self.denominateur

print("Début du programme")

try:
    f = Fraction(1, 0)
except ValueError as msg:
    print("Erreur :", msg)
else:
    print("la fraction a eté crée avec succes")

print("Fin du programme")