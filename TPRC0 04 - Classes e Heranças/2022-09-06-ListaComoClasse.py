class Lista:
    def __init__(self):
        self.lista = []

    def __repr__(self):
        saida = [str(x) for x in self.lista]
        return " ".join(saida)

    def adicionar(self, valor):
        self.lista.append(valor)

    def remover(self, valor):
        self.lista.remove(valor)

    def somar(self):
        auxiliar = 0
        for x in self.lista:
            auxiliar = auxiliar + x
        return auxiliar


lista = Lista()
lista.adicionar(3)
lista.adicionar(5)
lista.adicionar(10)
print(lista)
print(lista.somar())
lista.remover(10)
print(lista)