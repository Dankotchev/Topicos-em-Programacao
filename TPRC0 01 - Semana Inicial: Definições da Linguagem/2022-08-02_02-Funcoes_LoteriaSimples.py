import random
'''
    OBJETIVOS:
    1. Um programa que gere numeros aleatórios de jogos de loteria, em uma quantidade de jogos definida pelo usuário;
    2. Evitar gerar numeros repetidos dentro de um mesmo jogo;
    3. Não gerar o valor 0;
    4. Não gerar números repetidos dentro de um mesmo jogo.
'''


def gerarCartelas():
    jogo = []
    continuar = True
    contador = 1
    while continuar:
        x = int(random.random() * 60) + 1
        if not x in jogo:
            jogo.append(x)
            contador += 1
            if contador > 6:
                continuar = False
# Trasnforma cada nume gera em uma soma com 100, e retorna apenas os dois ultimos digitos
    jogo = [str(y + 100)[1:3] for y in jogo]
    jogo.sort()
    return jogo

quantidade = int(input("Quantas Cartelas de jogo gerar? "))
for j in range(0, quantidade):
    cartela = (" ".join(gerarCartelas()))
    print(cartela)
