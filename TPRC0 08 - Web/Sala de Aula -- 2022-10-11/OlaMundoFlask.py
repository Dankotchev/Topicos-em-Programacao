from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Bem vindo"


@app.route('/principal')
def principal():
    return "Voce esta na pagina principal"

@app.route('/contatos')
def contatos():
    return '''<p>Nossos contatos</p> \
              <p>Email: python@gmail.com '''

@app.route('/conttemplate')
def contatos1():
    return render_template("/homepage.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("pessoal.html", nome_usuario=nome_usuario)


#Colocar site no ar
if __name__ == "__main__":
   app.run(debug=True)