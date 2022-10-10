arquivoEntrada = "EntradaDeDados.txt"
with open(arquivoEntrada) as f:
    dados = f.read().split('\n')

# Criando uma lista de palavras para cada linha
for linha in dados:
    apresentar = "|"

    # Ordenando cada linha pelo tamanho das palavras
    palavras = sorted(linha.split(" "), key=len)

    # Formando a String para ser apresentada
    for i in palavras:
        apresentar = apresentar + i + "|"
    print(apresentar)
    