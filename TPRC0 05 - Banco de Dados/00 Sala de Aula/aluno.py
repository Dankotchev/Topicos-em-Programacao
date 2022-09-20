class Aluno:
    __idaluno = ''
    __nome = ''
    __flag = ''
    __endereco = ''
    __nascimento = ''
    __cidade = ''
    __uf = ''
    __cep = ''

    def __init__(self):
        self.__idaluno = ""
        self.__nome = ""
        self.__flag = ""
        self.__endereco = ""
        self.__nascimento = ""
        self.__cidade = ""
        self.__uf = ""
        self.__cep = ""

    @property  ##getter
    def idaluno(self):
        return self.__idaluno

    @idaluno.setter
    def idaluno(self, entrada):
        self.__idaluno = entrada

    @property  ##getter
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, entrada):
        self.__nome = entrada

    @property  ##getter
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, entrada):
        self.__flag = entrada

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, entrada):
        self.__endereco = entrada

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, entrada):
        self.__nascimento = entrada

    @property  ##getter
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, entrada):
        self.__cidade = entrada

    @property  ##getter
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, entrada):
        self.__uf = entrada

    @property  ##getter
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, entrada):
        self.__cep = entrada


    def __eq__(self, entrada):
        return self.__registro == entrada.__registro

    def __repr__(self):
        return "\nID: " + str(self.__idaluno) + "\tNome: " + self.__nome + "\n"

    def apresentarTudo(self):
        return "\nID: " + str(self.__idaluno) + "\tNome: " + self.__nome + "\nEndereço: " + self.__endereco + " - " + self.__cidade + " - " + self.__uf + "\nCEP: " + self.__cep