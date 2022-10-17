from CBD import *
from Cliente import *


class ControleCliente:

    def __init__(self):
        self.__lista = []
        self.ob = Banco()
        self.ob.configura(ho="localhost", db="bd_trabalho_sistemavenda", us="root", se="ifsp")

    def incluir(self, cliente):
        self.ob.abrirConexao()
        sql = "INSERT INTO cliente (nome, cpf, endereco, telefone, email, cidade, uf, cep) " \
              "VALUES ('{}', '{}', '{}','{}','{}','{}','{}', '{}')".format(
            cliente.nome,
            cliente.cpf,
            cliente.endereco,
            cliente.telefone,
            cliente.email,
            cliente.cidade,
            cliente.uf,
            cliente.cep)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def alterar(self, cliente):
        self.ob.abrirConexao()
        sql = "UPDATE cliente SET nome = '{}', cpf = '{}', endereco = '{}', " \
              "telefone ='{}', email = '{}', cidade = '{}', uf = '{}', cep = '{}' " \
              "WHERE idCliente = {}".format(
            cliente.nome,
            cliente.cpf,
            cliente.endereco,
            cliente.telefone,
            cliente.email,
            cliente.cidade,
            cliente.uf,
            cliente.cep,
            cliente.idCliente)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def retornarUltimoCliente(self, ultimoCliente):
        self.ob.abrirConexao()
        resultQuery = self.ob.selectQuery("SELECT * FROM cliente "
                                          "WHERE nome = '{}' AND cpf = '{}' AND telefone = '{}' "
                                          "ORDER BY idCliente DESC"
                                          .format(ultimoCliente.nome, ultimoCliente.cpf, ultimoCliente.telefone))
        retorno = Cliente()
        if len(resultQuery) >= 1:
            retorno.idCliente = resultQuery[0][0]
            retorno.nome = resultQuery[0][1]
            retorno.cpf = resultQuery[0][2]
            retorno.endereco = resultQuery[0][3]
            retorno.telefone = resultQuery[0][4]
            retorno.email = resultQuery[0][5]
            retorno.cidade = resultQuery[0][6]
            retorno.uf = resultQuery[0][7]
            retorno.cep = resultQuery[0][8]
        else:
            retorno.idCliente = -1
        return retorno

    def procuraPorID(self, idBusca):
        self.ob.abrirConexao()
        cliente = self.ob.selectQuery("SELECT * FROM cliente WHERE idCliente = {}".format(idBusca))
        retorno = Cliente()
        if len(cliente) >= 1:
            retorno.idCliente = cliente[0][0]
            retorno.nome = cliente[0][1]
            retorno.cpf = cliente[0][2]
            retorno.endereco = cliente[0][3]
            retorno.telefone = cliente[0][4]
            retorno.email = cliente[0][5]
            retorno.cidade = cliente[0][6]
            retorno.uf = cliente[0][7]
            retorno.cep = cliente[0][8]
        else:
            retorno.idCliente = -1
        return retorno

    def listaTodos(self):
        return self.__lista
