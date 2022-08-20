nome = "EntradaDeDados.txt"
with open(nome) as f:
    dados = f.read().split('\n')

with open("saidaDados.txt", "w") as arquivo:
    for i in dados:
        linha = i.split(" ")
        print(" ".join(linha[2:8]))
        arquivo.write(" ".join(linha[2:8]) + "\n")

arquivo.close()
