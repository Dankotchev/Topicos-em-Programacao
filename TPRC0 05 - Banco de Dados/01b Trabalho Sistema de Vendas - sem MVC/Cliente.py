class Cliente:

    def __init__(self):
        self.__idCliente = 0
        self.__nome = ''
        self.__cpf = ''
        self.__endereco = ''
        self.__telefone = ''
        self.__email = ''
        self.__cidade = ''
        self.__uf = ''
        self.__cep = ''

    @property
    def idCliente(self):
        return self.__idCliente

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email

    @property
    def cidade(self):
        return self.__cidade

    @property
    def uf(self):
        return self.__uf

    @property
    def cep(self):
        return self.__cep

    @idCliente.setter
    def idCliente(self, entrada):
        self.__idCliente = entrada

    @nome.setter
    def nome(self, entrada):
        self.__nome = entrada

    @cpf.setter
    def cpf(self, entrada):
        self.__cpf = entrada

    @endereco.setter
    def endereco(self, entrada):
        self.__endereco = entrada

    @telefone.setter
    def telefone(self, entrada):
        self.__telefone = entrada

    @email.setter
    def email(self, entrada):
        self.__email = entrada

    @cidade.setter
    def cidade(self, entrada):
        self.__cidade = entrada

    @uf.setter
    def uf(self, entrada):
        self.__uf = entrada

    @cep.setter
    def cep(self, entrada):
        self.__cep = entrada

    def __eq__(self, entrada):
        return self.__idCliente == entrada.idCliente

    def __repr__(self):
        return "ID Cliente : {} \tCPF: {}\tNome: {}".format(self.idCliente, self.cpf, self.nome)
