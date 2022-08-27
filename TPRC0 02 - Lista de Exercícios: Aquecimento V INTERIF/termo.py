"""
    Esse problema pode ser resolvido conhecendo a sequência de Padovan
----------------------------------------------------------------------------

# Forma recursiva da solução, a desvantagem é sua complexidade ser O(c^n)
def padovan_recursiva(n):
    if n < 4:
        return 1
    else:
        return padovan_recursiva(n - 2) + padovan_recursiva(n - 3)

"""
posicaoEntrada = int(input("Entrada: "))
# print(padovan_recursiva(posicaoEntrada))

# Forma não recursiva da solução com complexidade O(n)
posiZero, posiUm, posiDois, posiTres= 1, 1, 1, 1
if  posicaoEntrada <= 3:
    print("1")
else:
    for i in range (3, posicaoEntrada):
        posiTres = posiUm + posiZero
        posiZero = posiUm
        posiUm = posiDois
        posiDois = posiTres
    print(posiDois)
