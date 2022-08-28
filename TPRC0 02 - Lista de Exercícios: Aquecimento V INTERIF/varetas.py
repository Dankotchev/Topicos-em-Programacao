jogadores = ['Jogador 1', 'Jogador 2', 'Jogador 3']
pontuacao = [0, 0, 0]
varetas = [5, 10, 15, 20, 50]
rodada = 1

with open ("SaidasResultados.txt", "w") as saida:
    while True:
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
            vencedor = pontuacao.index(max(pontuacao))  # Verifica a posição do vencedor
            # Não verifica se ocorre empates
            strFinal = "RODADA {}".format(rodada) + "\n"
            #print(strRodada)
            strFinal += "Ganhador com {} pontos".format(max(pontuacao)) + "\n"
            #print(strGanhador)
            strFinal += "{}".format(jogadores[vencedor]) + "\n\n"
            print(strFinal)
            # print("Ganhador com {} pontos".format(max(pontuacao)))
            # print("{}".format(jogadores[vencedor]))
        pontuacao = [0, 0, 0]  # Resetando pontuações após a finalização de uma partida
        rodada += 1
        saida.write(strFinal)
        if jogadorInicial == -1:
            break
saida.close()