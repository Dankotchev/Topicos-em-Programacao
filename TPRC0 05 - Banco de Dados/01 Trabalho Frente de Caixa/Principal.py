from controledao.ControleCliente import *
from modelo.Cliente import *
from controledao.ControleItemVenda import *
from modelo.ItemVenda import *
from controledao.ControleProduto import *
from modelo.Produto import *
from controledao.ControleVenda import *
from modelo.Venda import *


def cadastrarCliente():
    cliente = Cliente()
    cliente.nome = input("Nome: ")
    cliente.nome = input("CPF: ")
    cliente.endereco = input("Endereço: ")
    cliente.telefone = input("Telefone: ")
    cliente.email = input("Email: ")
    cliente.cidade = input("Cidade: ")
    cliente.uf = input("UF: ")
    return cliente

def alterarCliente(chave):
    cliente = Cliente()
    cliente.idCliente = chave
    cliente.nome = input("Nome: ")
    cliente.cpf = input("CPF: ")
    cliente.endereco = input("Endereço: ")
    cliente.telefone = input("Telefone: ")
    cliente.email = input("email: ")
    cliente.cidade = input("Cidade: ")
    cliente.uf = input("UF: ")
    return cliente

def cadastrarVenda():
    venda = Venda()
    venda.data = input("Data venda: ")
    venda.valortotal = 0
    venda.idCliente = int(input("ID cliente: "))
    return venda

def alterarVenda(chave, oldVenda):
    venda = Venda()
    venda.idvenda = chave
    venda.data = input("Data venda: ")
    venda.valortotal = oldVenda.valorTotal
  #  venda.idCliente = int(input("ID cliente: "))
    return venda


def cadastrarProdutos():
    produto = Produto()
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

    # Cadastrar Produto
    if opcao == 1:
        while flag:
            print("Cadastrar Produto\n")
            produto = cadastrarProdutos()
            daoProduto.incluir(produto)
            c = int(input("\nContinuar?\n\t0 - ENCERRAR\n\t: "))
            if c == 0:
                flag = False
        flag = True

    # Cadastrar Venda
    if opcao == 2:
        continuarVendas = True
        continuarItemVendas = True

        while continuarVendas:
            clienteVenda = Cliente()
            print("Cadastrar Venda\n")
            venda = cadastrarVenda()

            # Verificar se o cliente informado existe no banco de dados
            clienteVenda = daoCliente.procuraRegistro(venda.idCliente)
            if clienteVenda.idCliente == -1:
                print("Cliente não cadastrado;\n\tRealizando cadastro agora:")
                clienteVenda = cadastrarCliente()
                # Propagar no banco para receber um idCliente
                daoCliente.incluir(clienteVenda)
                # Procurando no banco, em busca do idCliente
                clienteVenda = daoCliente.procuraRegistro(clienteVenda.cpf)

                # Atribuindo cliente corretamente na Venda
                venda.idCliente = clienteVenda.idCliente

            daoVenda.incluir(venda)

            # Gera cada Item Venda para a venda atual
            print("Venda #{}\n".format(venda.idvenda))
            itemNumero = 0
            while continuarItemVendas:
                print("Item Venda #{}\n".format(itemNumero))
                itemVenda = cadastrarItemVenda(venda.idvenda)
                venda.valortotal = venda.valortotal + (itemVenda.quantidade * itemVenda.valor)
                daoItemVenda.incluir(itemVenda)
                c = int(input("\nContinuar?\n\t0 - ENCERRAR\n\t: "))
                if c == 0:
                    continuarItemVendas = False
                itemNumero = itemNumero + 1
            daoVenda.alterar(venda)

            c = int(input("\nContinuar?\n\t0 - ENCERRAR\n\t: "))
            if c == 0:
                continuarVendas = False

    # Listar todas as Vendas realizadas
    if opcao == 3:
        listaVendas = []
        listaVendas = daoVenda.listarTodos()

        for venda in listaVendas:
            listaItemVenda = []
            listaItemVenda = daoItemVenda.listaTodos(venda.idvenda)
            print(venda)
            for itemVenda in listaItemVenda:
                print(itemVenda)

    # Cadastrar Clientes
    if opcao == 4:
        while flag:
            print("Cadastrar Cliente\n")
            cliente = cadastrarCliente()
            daoCliente.incluir(cliente)
            c = int(input("\nContinuar?\n\t0 - ENCERRAR\n\t: "))
            if c == 0:
                flag = False
        flag = True

    # Listar compras de um determinado Cliente
    if opcao == 5:
        somatorio = 0
        print("Apresentar cliente e suas compras")
        chaveProcura = int(input("Informe o id do cliente: "))
        cliente = daoCliente.procuraRegistro(chaveProcura)

        if cliente.idCliente != -1:
            print("Informações do cliente :: \n")
            print(cliente)

            print("Compras realizadas:\n")
            listaVendas = daoVenda.procurarPorCliente(cliente.idCliente)
            if listaVendas != -1:
                for venda in listaVendas:
                    somatorio = somatorio + venda.valortotal
                    print(venda)
                print("\nO cliente realizou R${} em compras".format(somatorio))
            else:
                print("\n\tO cliente não possuiu compras realizadas.")