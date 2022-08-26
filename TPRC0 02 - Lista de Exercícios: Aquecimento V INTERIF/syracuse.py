def syracuse(valor):
    contador = 0
    while valor > 1:
        if (valor % 2) == 0:
            contador = contador + 1
            valor = valor / 2
        else:
            contador = contador + 1
            valor = 3 * valor + 1
    return contador


entrada = int(input("Entrada: "))
print(syracuse(entrada))
