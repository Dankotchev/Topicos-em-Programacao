from builtins import len
textoTransporte = ''
segredo = input("Segredo: ")
fraseFinal = []

def binaryToDecimal(binario):
    return int(binario, 2) if binario != "" else 0

def decimalToBinary(decimal):
    binario = ''
    while decimal > 0:
        binario += str(decimal % 2)
        decimal //= 2
    while len(binario) < 8:
        binario += '0'
    return binario[::-1]

def traduza(entrada):
  volta = "".join(["0" if x.islower() else "1" for x in entrada])
  return volta

def traslateToBinary(texto, binario):
    for xB, vB in binario:
        if vB == '0':


    return  "".join([])


frase=[]
# texto = "".join([x for x in texto if x not in " .,0123456789"])
for x in segredo:
    binary = decimalToBinary(ord(x))     # Uma letra é transformada em um string de 0/1
    for oitoLetras in range(8, len(textoTransporte), 8):
        parte = traslateToBinary(oitoLetras, binary)
        fraseFinal.append(parte)
print("".join(fraseFinal))


"""    
for x in range(8, len(texto), 8):
      caracter = binaryToDecimal(traduza(texto[x-8:x]))
      if caracter != 0:
         frase.append(chr(caracter))
print("".join(frase))
"""