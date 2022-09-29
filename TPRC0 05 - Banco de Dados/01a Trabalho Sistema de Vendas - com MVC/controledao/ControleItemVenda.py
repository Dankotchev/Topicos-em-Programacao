from CBD import *
from ItemVenda import *


class ControleItemVenda:

    def __init__(self):
        self.__lista = []
        self.ob = Banco()
        self.ob.configura(ho="localhost", db="bd_trabalho_sistemavenda", us="root", se="")

    def incluir(self, itemvenda):
        self.ob.abrirConexao()
        sql = "INSERT INTO item_venda VALUES ({}, '{}', {}, {})".format(
                    itemvenda.idVenda,
                    itemvenda.idProduto,
                    itemvenda.quantidade,
                    itemvenda.valor)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def alterar(self, itemvenda):
        self.ob.abrirConexao()
        sql = "UPDATE item_venda SET quantidade = '{}', valor = {} " \
              "WHERE idvenda = {} AND idProduto = {}".format(
                    itemvenda.quantidade,
                    itemvenda.valor,
                    itemvenda.idVenda,
                    itemvenda.idProduto)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def procuraPorIDs(self, entradaVenda, entradaProduto):
        self.ob.abrirConexao()
        resultQuery = self.ob.selectQuery("SELECT * FROM item_venda "
                                          "WHERE idvenda = {} AND idProduto = {}".format(entradaVenda, entradaProduto))
        retorno = ItemVenda()
        if len(resultQuery) >= 1:
            retorno.idVenda = resultQuery[0][0]
            retorno.idProduto = resultQuery[0][1]
            retorno.quantidade = resultQuery[0][2]
            retorno.valor = resultQuery[0][3]
        return retorno
