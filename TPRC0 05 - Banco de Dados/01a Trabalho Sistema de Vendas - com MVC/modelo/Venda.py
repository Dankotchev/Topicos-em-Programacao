class Venda:

    def __init__(self):
        self.__idVenda = 0
        self.__data = ''
        self.__valortotal = 0
        self.__idCliente = ''

    @property
    def idVenda(self):
        return self.__idVenda

    @property
    def data(self):
        return self.__data

    @property
    def valortotal(self):
        return self.__valortotal

    @property
    def idCliente(self):
        return self.__idCliente

    @idVenda.setter
    def idVenda(self, entrada):
        self.__idVenda = entrada

    @data.setter
    def data(self, entrada):
        self.__data = entrada

    @valortotal.setter
    def valortotal(self, entrada):
        self.__valortotal = entrada

    @idCliente.setter
    def idCliente(self, entrada):
        self.__idCliente = entrada

    @staticmethod
    def apresentarVenda(entrada):
        return "Id Venda #{}\tId Cliente #{}\nData da Venda: {}\tTotal da Venda: R$ {}\n----------" \
            .format(entrada[0],
                    entrada[3],
                    entrada[1],
                    entrada[2])

    def __eq__(self, entrada):
        return self.__idVenda == entrada.idVenda

    def __repr__(self):
        return "Id Venda #{}\tId Cliente #{}\nData da Venda: {}\tTotal da Venda: R$ {}" \
            .format(self.idVenda,
                    self.idCliente,
                    self.data,
                    self.valortotal)
