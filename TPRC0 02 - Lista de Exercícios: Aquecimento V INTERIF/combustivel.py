gasolina = float(input("Gasolina: "))
etanol = float(input("Etanol: "))

if ((etanol / gasolina) <= 0.7) :
    print("GASOLINA\n")
else:
    print("ETANOL\n")

# combustivel = "ETANOL\n" if etanol/gasolina <= 0.7 else "GASOLINA\n"
# print(combustivel)