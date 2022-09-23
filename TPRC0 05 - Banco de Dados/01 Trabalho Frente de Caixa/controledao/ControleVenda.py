from CBD import *
from ..modelo.Venda import *

class ControleVenda:

    def __init__(self):
        self.__lista = []
        self.ob = Banco()
        self.ob.configura(ho="localhost", db="bd_trabalho_python", us="root", se="dknilo")

    def incluir(self, venda):
        self.ob.abrirConexao();
        sql = "INSERT INTO venda VALUES values({}, '{}', {}, {})".format(
                                                                    venda.idvenda,
                                                                    venda.data,
                                                                    venda.valortotal,
                                                                    venda.idcliente)
        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def alterar(self, venda):
        self.ob.abrirConexao();
        sql = "UPDATE venda SET data = '{}', valortotal = {}, idcliente = {}" \
              "WHERE idvenda = {}".format(
                                    venda.data,
                                    venda.valortotal,
                                    venda.idcliente,
                                    venda.idvenda)
        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()



    def procuraRegistro(self,entrada):
        self.ob.abrirConexao();
        resultQuery = self.ob.selectQuery("SELECT * FROM venda WHERE idvenda = {}".format(entrada))
        retorno = Venda()
        if len(resultQuery) >= 1:
            retorno.idvenda = resultQuery[0][0]
            retorno.data = resultQuery[0][1]
            retorno.valortotal = resultQuery[0][2]
            retorno.idcliente = resultQuery[0][3]
        return retorno

    def listarTodos(self):
        self.ob.abrirConexao();
        dados = self.ob.selectQuery("SELECT * FROM venda")
        print(dados)
        for venda in dados:
            retorno = Venda()
            retorno.idvenda = venda[0]
            retorno.data = venda[1]
            retorno.valortotal = venda[2]
            retorno.idcliente = venda[3]
        return dados

