from io import open

from controleAluno import *
from aluno import *

def cadastrarAluno():
    aluno = Aluno()
    aluno.idaluno = input("Id: ")
    aluno.nome = input("Nome: ")
    aluno.endereco = input("Enderço: ")
    aluno.nascimento = input("Data de Nascimento: ")
    aluno.cidade = input("Cidade: ")
    aluno.uf = input("UF: ")
    aluno.cep = input("CEP: ")
    aluno.flag = 1
    return aluno

def alterarAluno(chave):
    aluno = Aluno()
    aluno.idaluno = chave
    aluno.nome = input("Nome: ")
    aluno.endereco = input("Enderço: ")
    aluno.nascimento = input("Data de Nascimento: ")
    aluno.cidade = input("Cidade: ")
    aluno.uf = input("UF: ")
    aluno.cep = input("CEP: ")
    aluno.flag = 1
    return aluno



flag = True
daoAluno = ControleAluno()
aluno = Aluno()

while flag:
    print(" 1 - Cadastrar")
    print(" 2 - Consultar")
    print(" 3 - Alterar")
    print(" 4 - Remover")
    print(" 5 - Listar")
    print(" 0 - Sair")

    opcao = int(input("Escolha sua opção: "))

    if opcao == 0:
        flag = False

    if opcao == 1:
        aluno = cadastrarAluno()
        daoAluno.incluir(aluno)

    if opcao == 2:
        chave = int(input("Informe o id do aluno: "))
        aluno = daoAluno.procuraRegistro(chave)
        print(aluno)


    if opcao == 3:
        chave = int(input("Informe o id do aluno: "))
        aluno = daoAluno.procuraRegistro(chave)
        print(aluno)
        aluno = alterarAluno(chave)
        daoAluno.alterar(aluno)
