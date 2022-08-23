import random
'''
    OBJETIVOS:
    1. Gerar um programa que ouve a opção de qual jogo o usuário deseja e a quantidade de jogos
    2. Não gerar números repetidos dentro de um mesmo jogo
    3. Não gerar o número 0
    4. Poder voltar a gerar outros jogos
    
    INFORMAÇÕES:
        MEGA-SENA :: 60 números; jogo de 6 números
        LOTOFÁCIL :: 25 números; jogo de 15 números
        QUINA :: 80 números; jogo de 5 números
'''


def gerarJogos(num, aposta):
    apostas = []
    continuar = True
    contador = 1
    while continuar:
        x = int(random.random() *num) + 1
        if not x in apostas:
            apostas.append(x)
            contador += 1
            if contador > aposta:
                continuar = False
    apostas = [str(y + 100)[1:3] for y in apostas]
    apostas.sort()
    return apostas

continuar = True
while continuar:
    print(" :: Gerador de Apostas :: ")
    print("1 - MEGA-SENA")
    print("2 - LOTOFACIL")
    print("3 - QUINA")
    print("0 - SAIR")

    tipo_jogo = int(input("Qual jogo deseja apostar? "))
    if tipo_jogo != 0:
        quantidade = int(input("Quantos jogos gerar? "))
        if quantidade != 0:
            for j in range(0, quantidade):
                if tipo_jogo == 1:
                    jogo = (" ".join(gerarJogos(60, 6)))
                elif tipo_jogo == 2:
                    jogo = (" ".join(gerarJogos(25, 15)))
                elif tipo_jogo == 3:
                    jogo = (" ".join(gerarJogos(80, 5)))
                print(jogo)
            print()
    else:
        continuar = False
        print("Saindo")
