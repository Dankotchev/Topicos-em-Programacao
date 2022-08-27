jogadores = ['Jogador 1', 'Jogador 2', 'Jogador 3']
pontuacao = [0, 0, 0]
varetas = [5, 10, 15, 20, 50]
rodada = 1
print(varetas)

while True:
    jogadorInicial = int(input("Jogador Inicial da Rodada: "))
    if  jogadorInicial > -1:
        jogo = [int(valores) for valores in input("Jogo: ").split(" ")]
        print("RODADA {}".format(rodada))
        print(jogo)
    for indice in jogo:
        if indice != 0:
            pontuacao[jogadorInicial -1 ] = pontuacao[jogadorInicial -1] + varetas[indice - 1]
            #print(varetas[i-1])
            #print(i)
        if indice == 0:
            jogadorInicial += 1
        if jogadorInicial == 4:
            jogadorInicial = 1
        if indice == -1:
            break
    for indice, valor in jogadores:
        print("{} fez {} pontos".format(valor, pontuacao[indice]))
    if jogadorInicial == -1:
        break
