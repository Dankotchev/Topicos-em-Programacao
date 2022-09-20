from ConectarBancoDados import *
from aluno import *

class ControleAluno:

    def __init__(self):
        self.__lista = []
        self.ob = Banco()
        self.ob.configura(ho="localhost", db="aula_python", us="root", se="ifsp")

    def incluir(self, aluno):
        self.ob.abrirConexao();
        sql = "insert into aluno values({}, '{}', {}, '{}','{}','{}','{}','{}')".format(
                                                                    aluno.idaluno,
                                                                    aluno.nome,
                                                                    aluno.flag,
                                                                    aluno.endereco,
                                                                    aluno.nascimento,
                                                                    aluno.cidade,
                                                                    aluno.uf,
                                                                    aluno.cep)
        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def alterar(self, aluno):
        self.ob.abrirConexao();
        sql = "UPDATE aluno SET nome = '{}', endereco = '{}', " \
              "nascimento '{}', cidade = '{}', uf = '{}, cep = '{}' " \
              "WHERE idaluno = {}".format(
                                    aluno.nome,
                                    aluno.endereco,
                                    aluno.nascimento,
                                    aluno.cidade,
                                    aluno.uf,
                                    aluno.cep,
                                    aluno.idaluno)
        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()



    def procuraRegistro(self,entrada):
        self.ob.abrirConexao();
        aluno = self.ob.selectQuery("select * from aluno where idaluno = {}".format(entrada))
        retorno = Aluno()
        if len(aluno)>=1:
            retorno.idaluno = aluno[0][0]
            retorno.nome = aluno[0][1]
            retorno.flag = aluno[0][2]
            retorno.endereco = aluno[0][3]
            retorno.cidade = aluno[0][4]
            retorno.uf = aluno[0][5]
            retorno.cep = aluno[0][6]
            retorno.nascimento = aluno[0][7]
        return retorno

    def listaTodos (self):
        return self.__lista

