def gen_carres(n):
    for i in range(1, n + 1):
        yield i ** 2

carres = gen_carres(10)

for carre in carres:
    if carre > 50:
        break
    print(carre)
    carres = gen_carres(10)
for carre in carres:
    if carre % 2 == 0:
        continue
    print(carre)

    nombres = [3, 6, 9, 12, 15]
    for i in nombres[::-1]:
        print(i)

    for i in range(len(nombres) -1, -1, -1):
        print(nombres[i])

nombres = [3, 6, 9, 12, 15]
for i, n in enumerate(nombres):
    print(f"{i} : {n}")
    def gen_carres(n, limite):
        for i in range(1, n + 1):
            carre = i ** 2
            if carre > limite:
                break
            yield carre