class Calculadora:
    # construtor
    def __init__(self, a, b):
        self.operandoA = a
        self.operandoB = b

    def soma (self):
        return self.operandoA + self.operandoB

    def subtracao(self):
        return self.operandoA - self.operandoB

    def multiplicacao(self):
        return self.operandoA * self.operandoB

    def divisao(self):
        return self.operandoA / self.operandoB

    def set_operandos(self, a, b):
        self.operandoA = a
        self.operandoB = b

    def __repr__(self):
        return 'O valor de a = {} & valor de b = {}'.format(self.operandoA, self.operandoB)


c = Calculadora(56.9, 1.807)
print(c)
print(c.soma())
print(c.subtracao())
print(c.multiplicacao())
print(c.divisao())
