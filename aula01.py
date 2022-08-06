'''a1 = int(input("entre com um numero 1: "))
a2 = int(input("entre com um numero 2: "))
print(type(a1))
print(type(a2))



if a1 > a2 :
    print("O maior eh o primeiro")
else:
    print("O maior eh o segundo")

print("fim...")

nome = "Danilo Domingues Quirino"
vogal = "aeiou"
print(nome[0:10])
print(nome[0:nome.index(" ")])
print(nome[::-1])
print(nome.upper())
print(nome.split(" "))


letras = [x for x in nome]
print(letras)


for i in nome :
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i)

for i in nome :
    if vogal.find(i)>=0 :
        print(i)



def soma (a,b) :
    return  a + b

def multiplica (a,b) :
    return  a * b


print(soma(10, 20))
print(multiplica(10,10))



texto = "DANILO DOMINGUES QURINO"

def retornarpalavra (frase, posicao) :
    frase = frase.split(" ")
    return frase[posicao]

print(retornarpalavra(texto, 2))
#print(texto.replace("DANILO", ""))

i = "X"
while i in texto :
    print("tem a letra no nome, agora ficamos para sempre aqui....")
else:
    print("nao tem a letra no nome")

'''

def CelsiusToFar(valor) :
    return round(9.*valor/5 + 32.,2)


print("A temperatura de 0ºC em Far eh {:.2f}".format(CelsiusToFar(0)))