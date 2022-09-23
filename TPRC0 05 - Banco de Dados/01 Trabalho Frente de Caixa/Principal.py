from controledao.ControleCliente import *
from controledao.ControleItemVenda import *
from controledao.ControleProduto import *
from controledao.ControleVenda import *
from controledao.CBD import *

def cadastrarCliente():
    cliente = Cliente()
    cliente.idcliente = int(input("ID Cliente: "))
    cliente.nome = input("Nome: ")
    cliente.endereco = input("endereço: ")
    cliente.telefone = input("Telefone: ")
    cliente.email = input("email: ")
    cliente.cidade = input("Cidade: ")
    cliente.uf = input("UF: ")
    return cliente

def alterarCliente(chave):
    cliente = Cliente()
    cliente.idcliente = chave
    cliente.nome = input("Nome: ")
    cliente.endereco = input("endereço: ")
    cliente.telefone = input("Telefone: ")
    cliente.email = input("email: ")
    cliente.cidade = input("Cidade: ")
    cliente.uf = input("UF: ")
    return cliente

def cadastrarVenda():
    venda = Venda()
    venda.idvenda = int(input("Id Venda: "))
    venda.data = input("Data venda: ")
    venda.valortotal = 0
    venda.idcliente = int(input("ID cliente: "))
    return venda

def alterarVenda(chave, oldVenda):
    venda = Venda()
    venda.idvenda = chave
    venda.data = input("Data venda: ")
    venda.valortotal = oldVenda.valorTotal
  #  venda.idcliente = int(input("ID cliente: "))
    return venda


def cadastrarProdutos():
    produto = Produto()
    produto.idProduto = int(input("ID Produto: "))
    produto.nome = input("Nome do Produto: ")
    produto.quantidade = int(input("Quantidade do Produto:"))
    produto.valor = float(input("Valor: "))
    return  produto

def alterarProduto(chave):
    produto = Produto()
    produto.idProduto = chave
    produto.nome = input("Nome do Produto: ")
    produto.quantidade = int(input("Quantidade do Produto:"))
    produto.valor = float(input("Valor: "))
    return produto

def cadastrarItemVenda(idVenda):
    itemvenda = ItemVenda()
    itemvenda.idVenda = idVenda
    itemvenda.idProduto = int(input("ID Produto:"))
    itemvenda.quantidade = int(input("Quantidade"))
    itemvenda.valor = float(input("Valor: "))
    return itemvenda

def alterarItemVenda(idVenda, idProduto):
    itemvenda = ItemVenda()
    itemvenda.idVenda = idVenda
    itemvenda.idProduto = idProduto
    itemvenda.quantidade = int(input("Quantidade"))
    itemvenda.valor = float(input("Valor: "))
    return itemvenda

flag = True
daoCliente = ControleCliente()
cliente = Cliente()
daoVenda = ControleVenda()
venda = Venda()
daoProduto = ControleProduto()
produto = Produto()
daoItemVenda = ControleItemVenda()
itemVenda = ItemVenda()

while flag:
    print(" 1 - Cadastrar Produto")
    print(" 2 - Cadastrar Venda")
    print(" 3 - Listar Vendas")
    print(" 4 - Cadastrar Cliente")
    print(" 5 - Mostrar Cliente")
    print(" 0 - Sair")

    opcao = int(input("Escolha sua opção: "))

    if opcao == 0:
        flag = False

    if opcao == 1:
        while flag:
            print("Cadastrar Produto\n")
            produto = cadastrarProdutos()
            daoProduto.incluir(produto)
            c = int(input("\nContinuar?\n\t0 - ENCERRAR\n\t: "))
            if c == 0:
                flag = False
        flag = True

    if opcao == 2:
        continuarVendas = True
        continuarItemVendas = True

        while continuarVendas:
            print("Cadastrar Venda\n")
            venda = cadastrarVenda()
            daoVenda.incluir(venda)

            while continuarItemVendas:
                itemVenda = cadastrarItemVenda(venda.idvenda)
                venda.valortotal = venda.valortotal + (itemVenda.quantidade * itemVenda.valor)
                daoItemVenda.incluir(itemVenda)
                c = int(input("\nContinuar?\n\t0 - ENCERRAR\n\t: "))
                if c == 0:
                    continuarItemVendas = False

            daoVenda.alterar(venda)
            c = int(input("\nContinuar?\n\t0 - ENCERRAR\n\t: "))
            if c == 0:
                continuarVendas = False

    if opcao == 3:
        daoVenda.listaTodos()

    if opcao == 4:
        while flag:
            print("Cadastrar Cliente\n")
            cliente = cadastrarCliente()
            daoCliente.incluir(cliente)
            c = int(input("\nContinuar?\n\t0 - ENCERRAR\n\t: "))
            if c == 0:
                flag = False
        flag = True
