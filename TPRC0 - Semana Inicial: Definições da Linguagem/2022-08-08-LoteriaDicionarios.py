"""
    OBJETIVOS:
    1. Gerar um programa que ouve a opção de qual jogo o usuário deseja e a quantidade de jogos
    2. Não gerar números repetidos dentro de um mesmo jogo
    3. Não gerar o número 0
    4. Poder voltar a gerar outros jogos
    5. Inserir o resultado de um jogo
    6. Conferir os jogos realizados com o resultado informada
    7. Listar os jogos apostados
    8. Resumo das jogadas

    INFORMAÇÕES:
        MEGA-SENA   :: 60 números; jogo de 6 números
        LOTOFÁCIL   :: 25 números; jogo de 15 números
        QUINA       :: 80 números; jogo de 5 números
"""

import random

continuar_escolha = True
resumo = {}
jogos_feitos = []
dezena = []
resultado = ""

# Gerador de apostas para cada tipo de jogo
def gera_jogos(num, aposta):
    apostas = []
    continuar = True
    contador = 1
    while continuar:
        x = int(random.random() * num) + 1
        if not x in apostas:
            apostas.append(x)
            contador += 1
            if contador > aposta:
                continuar = False
    apostas = [str(y + 100)[1:3] for y in apostas]
    apostas.sort()
    return apostas


def conferir(resultado, cartelas):  #Utilizando conjuntos
    dezenas = set(resultado.split(" "))
    for i in cartelas:
       conta = len(dezenas & set(i.split(" ")))
       print(i, "=>", conta)
    return True

def mostrar_apostas(apostas):
    if len(apostas) > 0:
       for x in apostas:
           print(x)
    else:
       print("Nada a listar")


while continuar_escolha:
    print("\n :: ~~ PROGRAMA DE APOSTAS FEDERAIS ~~  :: ")
    print("1 - MEGA-SENA")
    print("2 - LOTOFACIL")
    print("3 - QUINA")
    print("4 - Informe o Resultado do Jogo")
    print("5 - Conferir Apostas")
    print("6 - Listar Últimas Apostas")
    print("7 - Resumo")
    print("0 - SAIR")

    escolha = int(input("Qual opção deseja? "))
    if 0 < escolha < 4:
        quantidade = int(input("Quantos jogos gerar? "))
        if quantidade != 0:
            for j in range(0, quantidade):
                if escolha == 1:
                    jogo = (" ".join(gera_jogos(60, 6)))
                elif escolha == 2:
                    jogo = (" ".join(gera_jogos(25, 15)))
                elif escolha == 3:
                    jogo = (" ".join(gera_jogos(80, 5)))
                print(jogo)
                jogos_feitos.append(jogo)
                dezena = jogo.split(" ")
                for k in dezena:
                    if k in resumo.keys():
                        resumo[k] += 1
                    else:
                        resumo[k] = 1
    elif escolha == 4:
        resultado = input("Informe o resultado: ")
    elif escolha == 5:
        conferir(resultado, jogos_feitos)
    elif escolha == 6:
        mostrar_apostas(jogos_feitos)
    elif escolha == 7:
        for i in sorted(resumo):
            print("Número: {} - Qtd: {}" .format(i, resumo[i]))
    else:
        continuar_escolha = False
        print("Saindo")
