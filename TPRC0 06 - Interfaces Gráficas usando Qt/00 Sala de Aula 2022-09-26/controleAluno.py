from Conectarbanco import *
from aluno import *

import datetime
from controleGenerico import *

class ControleAluno(ControleGenerico):

    def incluirAluno(self,aluno):
        self.incluir(aluno)

    def alterarAluno(self, aluno):
        self.alterar(aluno)

    def deletarAluno(self, aluno):
        self.delete(aluno)

    def pesquisaCodigo(self,entrada):
        aluno = self.procuraRegistro(entrada)
        retorno = Aluno()
        if len(aluno) >= 1:
            retorno.idaluno = aluno[0][0]
            retorno.nome = aluno[0][1]
            retorno.flag = aluno[0][2]
            retorno.endereco = aluno[0][3]
            retorno.cidade = aluno[0][4]
            retorno.uf = aluno[0][5]
            retorno.cep = aluno[0][6]
            retorno.nascimento = aluno[0][7]
        return retorno

    def listarTodosRegistros(self,objeto):
        return self.listarTodos(objeto)

    def converteObjeto(self,entrada):
        aluno = Aluno()
        aluno.idaluno=entrada[0]
        aluno.nome=entrada[1]
        aluno.endereco=entrada[2]

        return aluno

    def dadosJson(self,entrada):
        pesquisa = self.procuraRegistro(entrada)
        dados = Aluno()
        dados = self.converteObjeto(pesquisa[0])
        retorno = {}
        retorno = {'idaluno': dados.idaluno,
                   'nome': dados.nome,
                   'flag': dados.flag,
                   'endereco': dados.endereco,
                   'cidade': dados.cidade,
                   'uf': dados.uf,
                   'cep': dados.cep,
                   'nascimento': '{}'.format(dados.nascimento)}
        return json.dumps(retorno)


