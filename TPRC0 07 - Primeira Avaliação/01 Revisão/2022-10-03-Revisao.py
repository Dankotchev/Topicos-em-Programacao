def contarTipos (entrada, resumoDicionario):
    quantidadeVogais, quantidadeConsoantes = 0, 0
    vogais = "aeiou"

    entrada = entrada.lower()
    for letra in entrada:
        if letra != " ":

            # formando o dicionário de letras
            try:
                resumoDicionario[letra] += 1
            except:
                resumoDicionario[letra] = 1

            # Contando as vogais e consoantes
            if vogais.find(letra) >= 0:
                quantidadeVogais = quantidadeVogais + 1
            else:
                quantidadeConsoantes = quantidadeConsoantes + 1
    return quantidadeVogais, quantidadeConsoantes


arquivoEntrada = "EntradaDeDados.txt"
with open(arquivoEntrada) as f:
    dados = f.read().split('\n')
dados.sort()

with open("saidaDados.txt", "w") as arquivoSaida:
    linhaMaior = [1, 0]
    contador = 1
    vogais = "aeiou"
    quantidadeVogais, quantidadeConsoantes = 0, 0
    dicionarioLetras = {}

    for i in dados:
        quantidadeVogais, quantidadeConsoantes = contarTipos(i, dicionarioLetras)

        linha = i.split(" ")
        if len(linha) > linhaMaior[1]:
            linhaMaior[0] = contador
            linhaMaior[1] = len(linha)

        print(" ".join(linha) + " ==> ({}, {})".format(quantidadeVogais, quantidadeConsoantes))
        arquivoSaida.write(" ".join(linha) + " ==> ({}, {})".format(quantidadeVogais, quantidadeConsoantes) + "\n")
        contador = contador + 1

    print("Linha: {}\tPalavras: {}".format(linhaMaior[0], linhaMaior[1]))
    arquivoSaida.write("Linha: {}\tPalavras: {}".format(linhaMaior[0], linhaMaior[1]))
    print("\nResumo de ocorrências das Letras:\n")
    print(dicionarioLetras)
    arquivoSaida.write("\nResumo de ocorrências das Letras:")
    for entradaDicionario in dicionarioLetras:
        arquivoSaida.write("\n{} - {}\t".format(entradaDicionario, dicionarioLetras[entradaDicionario]))
        for tamanho in range(0, dicionarioLetras[entradaDicionario]):
            arquivoSaida.write("|")

arquivoSaida.close()
