from typing import re

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('Cliente.html')

@app.route('/tabela/')
def tabela():
    daoCliente = ControleCliente()
    dados = daoCliente.listaTodos()
    return render_template("TabelaListarTodos.html", result=dados)

@app.route('/editar/<id>')
def editar(id):
    daoCliente = ControleCliente()
    dados = daoCliente.procuraPorID(id)
    return render_template("EditarCliente.html", dados=dados)

@app.route('/delete/<id>')
def delete(id):
    daoCliente = ControleCliente()
    daoCliente.deletarPorID(id)
    return redirect(url_for('tabela'))

@app.route('/gravar', methods = ['POST', 'GET'])
def gravar():
    if request.method == 'POST':
       result = request.form
       cliente = Cliente()
       cliente.nome = result['nome']
       cliente.cpf = result['cpf']
       cliente.endereco = result['endereco']
       cliente.telefone = result['telefone']
       cliente.email = result['email']
       cliente.cidade = result['cidade']
       cliente.uf = result['uf']
       cliente.cep = result['cep']
       daoCliente = ControleCliente()

       if result['botao']=='Gravar':
           daoCliente.incluir(cliente)
       else:
           cliente.idCliente = int(result['codigo'])
           daoCliente.alterar(cliente)

    return redirect(url_for('tabela'))

import sys
sys.path.insert(0, 'modelo')
sys.path.insert(1, 'controle')

from modelo.Cliente import *
from controle.ControleCliente import *

if __name__ == '__main__':
   app.run(debug=True)
