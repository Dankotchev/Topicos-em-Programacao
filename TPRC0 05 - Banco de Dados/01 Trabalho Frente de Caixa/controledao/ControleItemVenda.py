from CBD import *
from ..modelo.ItemVenda import *

class ControleItemVenda:

    def __init__(self):
        self.__lista = []
        self.ob = Banco()
        self.ob.configura(ho="localhost", db="bd_trabalho_python", us="root", se="dknilo")

    def incluir(self, itemvenda):
        self.ob.abrirConexao();
        sql = "INSERT INTO itemvenda VALUES values({}, '{}', {}, {})".format(
                                                                    itemvenda.idVenda,
                                                                    itemvenda.idProduto,
                                                                    itemvenda.quantidade,
                                                                    itemvenda.valor)
        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def alterar(self, itemvenda):
        self.ob.abrirConexao();
        sql = "UPDATE itemvenda SET quantidade = '{}', valor = {} " \
              "WHERE idvenda = {} AND idproduto = {}".format(
                                    itemvenda.quantidade,
                                    itemvenda.valor,
                                    itemvenda.idVenda,
                                    itemvenda.idProduto)
        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()



    def procuraRegistro(self,entradaVenda, entradaProduto):
        self.ob.abrirConexao();
        resultQuery = self.ob.selectQuery("SELECT * FROM itemvenda WHERE idvenda = {} AND idproduto = {}".format(
                                                                                    entradaVenda, entradaProduto))
        retorno = ItemVenda()
        if len(resultQuery) >= 1:
            retorno.idVenda = resultQuery[0][0]
            retorno.idProduto = resultQuery[0][1]
            retorno.quantidade = resultQuery[0][2]
            retorno.valor = resultQuery[0][3]
        return retorno

    def listaTodos (self):
        return self.__lista

