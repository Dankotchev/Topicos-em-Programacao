"""
    OBJETIVOS:
    1. Inserindo valores em uma lista, até o usuário entrar com 0;
    2. Apresentando o maior e menor valor da lista;
    3. Ordenar a lista de forma crescente e decrescente;
    4. Adicionar outros elementos não numericos a lista e apresentar
    5. Apresentar o par indice e conteúdo.
"""
lista = []
valor = True
while valor:
    a = int(input("Informe um valor: "))
    if a == 0:
        valor = False
    else:
        lista.append(a)

# Apresentação de toda a lista
for i in lista:
    print(i)

print("O maior valor: {}." .format(max(lista)))
print("O menor valor: {}." .format(min(lista)))

# Apresentação ordenada
lista.sort()
print("Lista crescente: ", lista)
lista.sort(reverse=True)
print("Lista decrescente: ", lista)

# inclusão de string na lista
lista.append("danilo")
lista.append("IFSP Presidente Epitácio")
print(lista)

# Inclusão de uma lista dentro da lista
print(lista.extend(['limão', 'goiaba']))

for indice, conteudo in enumerate(lista):
    print("Indice {} valor {}".format(indice, conteudo))
