from builtins import len

def decimalToBinary(decimal):
    binario = ''
    while decimal > 0:
        binario += str(decimal % 2)
        decimal //= 2
    while len(binario) < 8:
        binario += '0'
    return binario[::-1]


textoTransporte = input("Texto de Transporte: ")
segredo = input("Segredo: ")
fraseFinal = []
binaryText = ''

# Transformando a frase segredo em uma string de 0 e 1
for letra in segredo:
    binary = decimalToBinary(ord(letra))  # Uma letra é transformada em um string de 0/1
    binaryText += binary
posicao = 0
# Cifrando a mensagem no texto de Transporte
for l in textoTransporte:
    if l != ' ':
        if posicao > len(binaryText) - 1:
            fraseFinal.append(
                l.lower())  # Caso o texto de transporte seja maior que o segredo, todas as letras ficam minusculas
        else:
            if binaryText[posicao] == "0":
                fraseFinal.append(l.lower())
            else:
                fraseFinal.append(l.upper())
        posicao += 1
    else:
        fraseFinal.append(l)
print("".join(fraseFinal))
