from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('estudante.html')

@app.route('/editar/<id>')
def editar(id):
    daoAluno = ControleAluno()
    dados = daoAluno.pesquisaCodigo(id)
    return render_template("editaestudante.html",dados = dados)

@app.route('/delete/<id>')
def delete(id):
    daoAluno = ControleAluno()
    daoAluno.deletarAluno(id)
    return redirect(url_for('tabela'))

@app.route('/gravar', methods = ['POST', 'GET'])
def gravar():
    if request.method == 'POST':
       result = request.form
       al = Aluno()
       al.nome = result['nome']
       al.endereco = result['endereco']
       al.cidade = result['cidade']
       al.uf = result['uf']
       al.cep = result['cep']
       al.nascimento = result['data']
       daoAluno = ControleAluno()

       if result['botao']=='Gravar':
           daoAluno.incluirAluno(al)
       else:
           al.idaluno=result['codigo']
           daoAluno.alterarAluno(al)

    return redirect(url_for('tabela'))

@app.route('/tabela/')
def tabela():
    daoAluno = ControleAluno()
    dados = daoAluno.listarTodosRegistros()
    return render_template("resultadotabela.html", result=dados)

import sys
import subprocess as sp
sys.path.insert(0, 'modelo')
sys.path.insert(1, 'controle')
from aluno import *
from controleAluno import *

if __name__ == '__main__':
   app.run(debug = True)