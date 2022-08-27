from builtins import len
segredo = input("Segredo: ")

def binaryToDecimal(n):
    return int(n, 2) if n != "" else 0

def decimalToBinary(n):
    return int(n, 10) if n != "" else 0

def traduza(entrada):
  volta = "".join(["0" if x.islower() else "1" for x in entrada])
  return volta

frase=[]
# texto = "".join([x for x in texto if x not in " .,0123456789"])
for x in segredo:
    a = decimalToBinary(ord(x))
    print(a)
#    print(str(ord(x))))




"""    
for x in range(8, len(texto), 8):
      caracter = binaryToDecimal(traduza(texto[x-8:x]))
      if caracter != 0:
         frase.append(chr(caracter))
print("".join(frase))
"""