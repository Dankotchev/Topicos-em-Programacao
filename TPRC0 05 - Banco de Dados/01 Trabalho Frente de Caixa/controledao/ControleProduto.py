from ConectarBancoDados import *
from ..modelo.Produto import *

class ControleProduto:

    def __init__(self):
        self.__lista = []
        self.ob = Banco()
        self.ob.configura(ho="localhost", db="aula_python", us="root", se="ifsp")

    def incluir(self, produto):
        self.ob.abrirConexao();
        sql = "insert into produto values({}, '{}', {}, {})".format(
                                                                    produto.idProduto,
                                                                    produto.nome,
                                                                    produto.quantidade,
                                                                    produto.valor)
        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def alterar(self, produto):
        self.ob.abrirConexao();
        sql = "UPDATE produto SET nome = '{}', quantidade = {}, valor = {} " \
              "WHERE idproduto = {}".format(
                                    produto.nome,
                                    produto.quantidade,
                                    produto.valor,
                                    produto.idProduto)
        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()



    def procuraRegistro(self,entrada):
        self.ob.abrirConexao();
        resultQuery = self.ob.selectQuery("SELECT * FROM produto WHERE idproduto = {}".format(entrada))
        retorno = Produto()
        if len(resultQuery)>=1:
            retorno.idproduto = resultQuery[0][0]
            retorno.nome = resultQuery[0][1]
            retorno.quantidade = resultQuery[0][2]
            retorno.valor = resultQuery[0][3]
        return retorno

    def listaTodos (self):
        return self.__lista

