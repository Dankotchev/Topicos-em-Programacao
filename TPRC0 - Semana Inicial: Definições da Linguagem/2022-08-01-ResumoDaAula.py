# ENTRADA DE DADOS NO PYTHON

# Entradas simples de dados e sem validação
nome = input("Nome: ")
idade1 = input("Idade: ")
idade2 = int(input("Idade: "))
valor = input("Número: ")

# Mostrando os tipos dos dados inseridos
print("Antes da conversão ==========================")
print(type(nome))
print(type(idade1))
print(type(idade2))
print(type(valor))

# Convertendo os tipos de dados
print("Depois da conversão =========================")
if idade1.isnumeric():
   idade3 = int(idade1)
   print("convertido")


# ENTRADA DE DADOS UTILIZANDO BIBLITOECA PROMPT
import prompt

# Com a biblioteca prompt é possivel validar um tipo de dado
numero = prompt.integer(prompt="Entre com um número: ")
email = prompt.email("Seu e-mail:")
nome = prompt.string("Seu nome: ")

print(type(nome))
print(type(numero))
print(type(email))

# SAIDA DE DADOS NA TELA
cidade = "Epitácio"

# Opções de concatenar strings de saídas com dados
print(f'Ola {nome}, bem vindo ao curso em {cidade}')
print("%s Bem vindo %s"%("Danilo","Epitacio"))
print("Olá, {} o seu email é {}!".format(nome, email))

print('{:,}'.format(1234567890))
print('Gasolina: R${:.2f}'.format(4.356))
print('Respostas corretas: {:.2%}'.format(53/60))


# MANIPULAÇÃO DE STRING

# As posições do "vetor" ao selecionar um intervalo sõa contadas [x:y]
# Onde x inicia na posição 0 do vetor
# E onde y é o elemento do vetor

# X     012345678901234567890123
nome = 'DANILO DOMINGUES QUIRINO'
# Y     123456789012345678901234

print(nome[0:nome.index(" ")].title())      # DANILO
print(nome[0:nome.find(("L"))])             # DANI
print(nome[0:3])                            # DAN
print(nome[7:16].upper())                   # DOMINGUES
print(nome.split())                         # ['DANILO','DOMINGUES', 'QUIRINO']
print(nome.replace("DOMINGUES", ""))        # DANILO QUIRINO
print(nome.lower())                         # danilo domingues quirino
# print(nome.upper()) Transforma em maiúsculas

letrasnome = [x for x in nome[:6]]
print(letrasnome)                           # ['D','A','N','I','L','O']
print(nome[7:])                             # QUIRINO
print(nome[::-1])                           # ONIRIUQ OLINAD
print(nome[::2])                            # DNL OIGE URN
print(" \"apelido\" ".join(nome.split(" ")))   # DANILO "apelido" DOMINGUES "apelido" QUIRINO

# COMANDO REPETIÇÃO FOR

vogais = "aeiou"
print("for percorre todo o nome e apresenta as vogais")
for i in nome:
    if vogal.find(i) >= 0:
        print(i)

nome = ["DANILO", "VILSON", "JOAO"]

# Enumerate retornar um par de chave e valor
# O for percorre cada elemento dentro do vetor nome, retornando uma chave "index" e seu valor
for key, value in enumerate(nome):
    print(key, value)
print("-------------------------")

for key in nome[0]:
    print(key*(nome[0].index(key)+1))
else:
    print("---------------------")

print("for percorrendo cada elemento: ")
for i in ['Tamanduá', 'Tatu', 'Boto Cor-De-Rosa']:
    print(i)
print("---------------------")

print("for percorrendo valores de 0 até 10: ")
for i in range(10):
    print(i)
print("---------------------")

print("for percorrendo de 5 até 10 ao passo 2: ")
for i in range(5,10,2):
    print(i)
print("---------------------")


k = [('a','b1','c1','d1','e1')]
for a, b, c, d, e in k:
    print(a, b, c, d, e)
