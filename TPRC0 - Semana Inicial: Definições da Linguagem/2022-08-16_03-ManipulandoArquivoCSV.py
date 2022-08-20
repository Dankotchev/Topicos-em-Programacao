# converte a data para o padrão do SQL, dividindo a data original e retornando na formatação desejada
def altera_data(original):
    alterada = original.split("/")
    return alterada[2] + "-" + alterada[1] + "-" + alterada[0]


caminhoEntrada = "EntradaDeDados.csv"
with open(caminhoEntrada) as entrada:
    dados = entrada.read().split('\n')

with open("script.sql", "w") as escrita:
    for i in dados:
        if i != "":
            linha = i.split(";")
            data = altera_data(linha[1])
            dezenas = linha[2:8]
            dezenas = " ".join([str(int(y) + 100)[1:3] for y in dezenas])
            sql = "INSERT INTO MEGASENA VALUES ({}, '{}', '{}');".format(linha[0], data, dezenas)
            print(sql)
            escrita.write(sql + "\n")

entrada.close()
escrita.close()
