def ganhador (pontuacoes, jogadores):
    if pontuacoes.count(max(pontuacoes)) == 1:  # Apenas uma ocorrência do MAIOR valor, logo um ganhador
        resultado = "Ganhador com {} pontos".format(max(pontuacoes)) + "\n"
        resultado += "{}".format(jogadores[pontuacoes.index(max(pontuacoes))])
    else:
        resultado = "Empate com {} pontos".format(max(pontuacao)) + "\n"
        for i in range(len(pontuacoes)):
            if pontuacoes[i] == max(pontuacoes):
                resultado += "{}, ".format(jogadores[i])
    return resultado + "\n"


jogadores = ['Jogador 1', 'Jogador 2', 'Jogador 3']
varetas = [5, 10, 15, 20, 50]
rodada = 1
jogadorInicial = 0
strIntermediaria = ''

with open ("SaidasResultados.txt", "w") as saida:
    while jogadorInicial != -1:
        pontuacao = [0, 0, 0]  # Resetando pontuações após a finalização de uma partida
        jogadorInicial = int(input("Jogador Inicial da Rodada: "))
        if jogadorInicial > -1:
            partida = [int(valores) for valores in input("Jogo: ").split(" ")]
            for i in partida:
                if i == -1:
                    break
                elif i != 0:
                    pontuacao[jogadorInicial - 1] += varetas[i - 1]
                else:
                    jogadorInicial += 1
                    if jogadorInicial == 4:
                        jogadorInicial = 1
            strIntermediaria += "RODADA {}".format(rodada) + "\n" + ganhador(pontuacao, jogadores) + "\n"
        rodada += 1
    print(strIntermediaria)
    saida.write(strIntermediaria)
saida.close()