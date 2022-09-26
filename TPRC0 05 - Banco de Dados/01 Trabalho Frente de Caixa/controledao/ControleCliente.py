import sys

# sys.path.insert(0,'../controledao')
# sys.path.insert(1,'../modelo')
# from CBD import *

import controledao.CBD
from . import CBD

class ControleCliente:

    def __init__(self):
        self.__lista = []
        self.ob = Banco()
        self.ob.configura(ho="localhost", db="bd_trabalho_python", us="root", se="dknilo")

    def incluir(self, cliente):
        self.ob.abrirConexao()
        sql = "insert into cliente values({}, '{}', '{}','{}','{}','{}','{}', '{}')".format(
            cliente.idCliente,
            cliente.nome,
            cliente.endereco,
            cliente.telefone,
            cliente.email,
            cliente.cidade,
            cliente.uf,
            cliente.cep)
        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def alterar(self, cliente):
        self.ob.abrirConexao();
        sql = "UPDATE cliente SET nome = '{}', endereco = '{}', " \
              "telefone '{}', email = '{}', cidade = '{}', uf = '{}', cep = '{}' " \
              "WHERE idCliente = {}".format(
            cliente.nome,
            cliente.endereco,
            cliente.telefone,
            cliente.email,
            cliente.cidade,
            cliente.uf,
            cliente.cep,
            cliente.idCliente)
        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def procuraRegistro(self, entrada):
        self.ob.abrirConexao()
        cliente = self.ob.selectQuery("SELECT * FROM cliente WHERE idCliente = {}".format(entrada))
        retorno = Cliente()
        if len(cliente) >= 1:
            retorno.idCliente = cliente[0][0]
            retorno.nome = cliente[0][1]
            retorno.endereco = cliente[0][2]
            retorno.telefone = cliente[0][3]
            retorno.email = cliente[0][4]
            retorno.cidade = cliente[0][5]
            retorno.uf = cliente[0][6]
            retorno.cep = cliente[0][7]
        return retorno

    def listaTodos(self):
        return self.__lista
