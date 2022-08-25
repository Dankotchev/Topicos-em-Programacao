entrada = input("Entrada: ")
somapar, somaimpar = 0, 0

def apresentar (soma):
    print("S" if (soma % 3 == 0) else "N")

for i in entrada:
    i = int(i)
    if (i % 2) == 0:
        somapar = somapar + i
    else:
        somaimpar = somaimpar + i

apresentar(somapar)
apresentar(somaimpar)
