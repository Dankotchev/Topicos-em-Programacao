from builtins import len

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

def criptografar (textoTransporte):
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


def descriptografar(textoTransporte):
    fraseFinal = []
    textoTransporte = "".join([x for x in textoTransporte if x not in " .,0123456789"])
    for x in range(8, len(textoTransporte), 8):
        caracter = binaryToDecimal(traduza(textoTransporte[x - 8:x]))
        if caracter != 0:
            fraseFinal.append(chr(caracter))
    print("".join(fraseFinal))


print("Escolha uma opção...\n1- Criptografar uma mensagem\n2- descriptografar uma mensagem")
escolha = int(input("ESCOLHA :: "))
textoTransporte = input("Texto de Transporte: ")

if escolha == 1:
    criptografar(textoTransporte)
else escolha == 2:
    descriptografar(textoTransporte)

