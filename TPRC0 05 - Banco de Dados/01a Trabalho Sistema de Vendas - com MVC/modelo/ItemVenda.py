class ItemVenda:

    def __init__(self):
        self.__idVenda = 0
        self.__idProduto = 0
        self.__quantidade = 0
        self.__valor = 0

    @property
    def idVenda(self):
        return self.__idVenda

    @property
    def idProduto(self):
        return self.__idProduto

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def valor(self):
        return self.__valor

    @idVenda.setter
    def idVenda(self, entrada):
        self.__idVenda = entrada

    @idProduto.setter
    def idProduto(self, entrada):
        self.__idProduto = entrada

    @quantidade.setter
    def quantidade(self, entrada):
        self.__quantidade = entrada

    @valor.setter
    def valor(self, entrada):
        self.__valor = entrada

    def __eq__(self, entrada):
        return self.__idVenda == entrada.idVenda and self.idProduto == entrada.idProduto

    def __repr__(self):
        return "Id Produto #{}\tQuantidade: {}\tValor uni: R${}" \
            .format(self.idProduto, self.quantidade, self.valor)
