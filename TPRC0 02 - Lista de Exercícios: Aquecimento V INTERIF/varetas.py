jogadores = ['Jogador 1', 'Jogador 2', 'Jogador 3']
varetas = [5, 10, 15, 20, 50]
print(varetas)

# while True:
jogadorInicial = int(input("Jogador Inicial da Rodada: "))
if  jogadorInicial > -1:
    #jogo = input("Jogo: ").split(" ")
    #jogo = [int(valores) for valores in jogo]
    jogo = [int(valores) for valores in input("Jogo: ").split(" ")]
    print(jogo)
    for i in jogo:
        if i != 0:
            print(jogo)


