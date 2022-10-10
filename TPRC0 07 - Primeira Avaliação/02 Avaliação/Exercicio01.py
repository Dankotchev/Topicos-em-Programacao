def criarDicionario(dicionario, lista):
    for i in lista:
        try:
            dicionario[i] += 1
        except:
            dicionario[i] = 1


arquivoEntrada = "EntradaDeDados.txt"
with open(arquivoEntrada) as f:
    dados = f.read().split('\n')

with open("saidaDados.txt", "w") as arquivoSaida:
    contador = 1
    palavras = []

    # Imprimindo cada linha numerada
    for linha in dados:
        arquivoSaida.write("{} ".format(contador) + linha + "\n")
        contador = contador + 1

    # Criando uma lista de palavras do texto
    for linha in dados:
        palavra = linha.split(" ")
        for i in palavra:
            palavras.append(i)

    # Procura da maior e menor palavra do texto
    maiorPalavraTamanho, maiorPalavraPosicao = len(palavras[0]), 0
    menorPalavraTamanho, menorPalavraPosicao = len(palavras[0]), 0
    posicao = 0
    for j in palavras:
        if len(j) > maiorPalavraTamanho:
            maiorPalavraPosicao = posicao
            maiorPalavraTamanho = len(j)
        if len(j) < menorPalavraTamanho:
            menorPalavraPosicao = posicao
            menorPalavraTamanho = len(j)
        posicao = posicao + 1

    arquivoSaida.write("\nMaior palavra: {}\tMenor Palavra: {}".format(
        palavras[maiorPalavraPosicao], palavras[menorPalavraPosicao]))

    #Palavras repetidas
    arquivoSaida.write("\nPalavras Repetidas: \n")
    dicionarioPalavras = {}

    criarDicionario(dicionarioPalavras, palavras)
    for palavra, repetições in dicionarioPalavras.items():
        if repetições > 1:
            arquivoSaida.write("{} ==> {}\n".format(palavra, repetições))

    # Tamanhos Repetidos
    arquivoSaida.write("\nResumo:\n")
    dicionarioTamanhos = {}
    for i in palavras:
        try:
            dicionarioTamanhos[len(i)] += 1
        except:
            dicionarioTamanhos[len(i)] = 1

    for j in sorted(dicionarioTamanhos):
        arquivoSaida.write("Com {} letras = {}\n".format(j, dicionarioTamanhos[j]))

arquivoSaida.close()

