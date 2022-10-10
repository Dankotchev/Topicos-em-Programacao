def contarVogais (entrada):
    quantidadeVogais = 0
    vogais = "aeiou"

    entrada = entrada.lower()
    for letra in entrada:
        if letra != " ":
            # Contando as vogais
            if vogais.find(letra) >= 0:
                quantidadeVogais = quantidadeVogais + 1
    return quantidadeVogais


arquivoEntrada = "EntradaDeDados.txt"
with open(arquivoEntrada) as f:
    dados = f.read().split('\n')


# Criando uma lista de palavras do texto
palavras = []
for linha in dados:
    palavra = linha.split(" ")
    for i in palavra:
        palavras.append(i)

# Procura da palavra com mais vogais
maiorNumeroVogais, maiorNumeroPosicao = contarVogais(palavras[0]), 0
posicao, auxiliar = 0, 0

for palavra in palavras:
    auxiliar = contarVogais(palavra)
    if auxiliar > maiorNumeroVogais:
        maiorNumeroVogais = auxiliar
        maiorNumeroPosicao = posicao

print("Palavras com {} vogais".format(maiorNumeroVogais))
contador = 1
for palavrasMaiores in palavras:
    if contarVogais(palavrasMaiores) == maiorNumeroVogais:
        print("{}\t{}".format(contador, palavrasMaiores))
        contador += 1
