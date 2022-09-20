import random


class Loteria:
    def __init__(self):
        self.nomeJogo ='MEGASENA'
        self.resultado = ''

    def gerarCartela(self):
        if self.nomeJogo == 'MEGASENA':
            numeros = 60
            quantidade = 6
        else:
            numeros = 80
            quantidade = 5

        jogo = []
        continuar = True
        contador = 1
        while continuar:
            x = int(random.random() * numeros) + 1
            if not x in jogo:
                jogo.append(x)
                contador += 1
                if contador > quantidade:
                    continuar = False
        jogo = [str(y + 100)[1:3] for y in jogo]
        jogo.sort()
        return " ".join(jogo) # cartela gerada

    def conferir (self, jogo):
        dezenas = set(self.resultado.split(" "))
        print(dezenas)
        conta = len(dezenas & set(jogo.split(" ")))
        acertos= "Você acertou {} dezenas".format(conta)
        return acertos

    def informarResultado(self, resultado):
        self.resultado = resultado

    def __repr__(self):
        return self.nomeJogo + " " + self.resultado

mega = Loteria()
jogoGerado = mega.gerarCartela()
print(jogoGerado)
mega.informarResultado(mega.gerarCartela())
print(mega.conferir(jogoGerado))
