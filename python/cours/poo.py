class Fraction:
    numerateur = 1
    denominateur = 1

    def quotient(self):  # self = tiers ou quart selon l'appel
        return self.numerateur / self.denominateur

tiers = Fraction()
tiers.denominateur = 3

quart = Fraction()
quart.denominateur = 4

print(tiers.quotient())
print(quart.quotient())