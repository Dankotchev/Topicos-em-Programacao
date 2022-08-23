"""
def mostrar(lista, procurado):
    dezenas = ""
    for j in lista:
        if j == procurado:
            dezenas += procurado + " "  # Caso fosse um inteiro seria necessário o cast para string: str(procurado)
        else:
            dezenas += "-- "
    return dezenas
"""

def mostrar(lista, procurado):
    linha = [x + " " if x == procurado else "ºº " for x in lista]
    # coloca x + espaço na linha se ele for igual ao valor procurado, ou -- se não estiver, para cada valor da lista
    return " ".join(linha)

nome = "EntradaDeDados.txt"
with open(nome) as f:
    dados = f.read().split('\n')

procurar = input("Numero procurado: ")
for i in dados:
    dados = i.split(" ")
    lista = dados[2:7]
    if procurar in lista:
        print(dados[0], mostrar(lista, procurar))

f.close()
