from flask import Flask
from ControleCliente import *

app = Flask(__name__)

@app.route('/principal/')
def pricipal():
    return "<h1>Você está na página principal</h1>"

@app.route('/pagina2/')
def pagina2():
    return  "<h2>você está na página 2</h2>"

@app.route('/pagina2/p/')
def pagina2p():
    return "<h3>você está na página 3</h3>"

@app.route('/mostrar/<codigo>/')
def mostrar(codigo):
    return "<h3>O código informado foi {}</h3>".format(codigo)

@app.route('/apresentar/<nome>')
def apresentar(nome):
    return '''
        <h1> Olá {}</h1>
        <p> Seja bem Vindo  </p>
    '''.format(nome)

@app.route('/tabuada/<valor>')
def tabuada(valor):
    retorno = "<h1>Tabuada do {}</h1>".format(valor)
    for i in range(0, 11):
        retorno = retorno + "<p>{} x {} = {}</p>".format(valor, i, (i * int(valor)))
    return retorno

@app.route('/cliente/<id>')
def cliente(id):
    daoCliente = ControleCliente()
    cliente = daoCliente.procuraPorID(id)
    retorno = '''
            <p>Cliente ID...........{}</p>
            <p>Nome.................{}</p>
            <p>CPF..................{}</p>
            <p>Telefone.............{}</p>
    '''.format(cliente.idCliente, cliente.nome, cliente.cpf, cliente.telefone)
    return retorno

if __name__ == "__main__":
    app.run(debug=True)
