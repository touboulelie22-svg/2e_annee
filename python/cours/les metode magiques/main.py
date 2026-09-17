class Fraction:
    def __init__(self, numerateur: int, denominateur: int) -> None:
        self.numerateur = numerateur
        self.denominateur = denominateur

def __repr__(self) -> str:
    return f"{self.numerateur}/{self.denominateur}"

def __mul__(self, other: int) -> "Fraction":
    if isinstance(other, int):
        return Fraction(self.numerateur * other, self.denominateur)
    raise TypeError("Multiplication possible uniquement avec un entier")

def __rmul__(self, other: int) -> "Fraction":
    return self.__mul__(other)