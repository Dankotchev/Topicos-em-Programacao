class Produto:

    def __init__(self):
        self.__idProduto = 0
        self.__nome = ''
        self.__quantidade = 0
        self.__valor = 0

    @property
    def idProduto(self):
        return self.__idProduto

    @property
    def nome(self):
        return self.__nome

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def valor(self):
        return self.__valor

    @idProduto.setter
    def idProduto(self, entrada):
        self.__idProduto = entrada

    @nome.setter
    def nome(self, entrada):
        self.__nome = entrada

    @quantidade.setter
    def quantidade(self, entrada):
        self.__quantidade = entrada

    @valor.setter
    def valor(self, entrada):
        self.__valor = entrada

    def __eq__(self, entrada):
        return self.__idProduto == entrada.idProduto

    def __repr__(self):
        return "ID Produto: {}\tEstoque: {}\tValor: R${}" \
            .format(self.idProduto, self.quantidade, self.valor)
