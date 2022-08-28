from builtins import len

def binaryToDecimal(binario):
    return int(binario, 2) if binario != "" else 0

def traduza(entrada):
  volta = "".join(["0" if x.islower() else "1" for x in entrada])
  return volta

def descriptografar(textoTransporte):
    fraseFinal = []
    textoTransporte = "".join([x for x in textoTransporte if x not in " .,0123456789"])
    for x in range(8, len(textoTransporte), 8):
        caracter = binaryToDecimal(traduza(textoTransporte[x - 8:x]))
        if caracter != 0:
            fraseFinal.append(chr(caracter))
    return "".join(fraseFinal)


arquivoEntrada = "EntradasCodificadas.txt"
with open(arquivoEntrada) as arq:
    linhas = arq.read().split('\n')

with open ("SaidasDecodificadas.txt", "w") as saida:
    for l in linhas:
        descifrado = descriptografar(l)
        print(descifrado)
        saida.write(descifrado)
saida.close()
arq.close()

