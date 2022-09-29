from builtins import int

from ControleCliente import *
from Cliente import *
from ControleItemVenda import *
from ItemVenda import *
from ControleProduto import *
from Produto import *
from ControleVenda import *
from Venda import *


def cadastrarCliente():
    cadCliente = Cliente()
    cadCliente.nome = input("Nome: ")
    cadCliente.cpf = input("CPF: ")
    cadCliente.endereco = input("Endereço: ")
    cadCliente.telefone = input("Telefone: ")
    cadCliente.email = input("Email: ")
    cadCliente.cidade = input("Cidade: ")
    cadCliente.uf = input("UF: ")
    return cadCliente


def cadastrarVenda():
    cadVenda = Venda()
    cadVenda.data = input("Data venda: ")
    cadVenda.valortotal = 0
    cadVenda.idCliente = int(input("ID cliente: "))
    return cadVenda


def cadastrarProdutos():
    cadProduto = Produto()
    cadProduto.nome = input("Nome do Produto: ")
    cadProduto.quantidade = int(input("Quantidade do Produto:"))
    cadProduto.valor = float(input("Valor: "))
    return cadProduto


def cadastrarItemVenda(idVenda):
    cadItemVenda = ItemVenda()
    cadItemVenda.idVenda = idVenda
    cadItemVenda.idProduto = int(input("ID Produto:"))
    cadItemVenda.quantidade = int(input("Quantidade"))
    cadItemVenda.valor = float(input("Valor: "))
    return cadItemVenda


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
    print("\n")
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
            # clienteVenda = Cliente()
            print("Cadastrar Venda\n")
            venda = cadastrarVenda()

            # Verificar se o cliente informado existe no banco de dados
            clienteVenda = daoCliente.procuraPorID(venda.idCliente)
            if clienteVenda.idCliente == -1:
                print("Cliente não cadastrado;\n\tRealizando cadastro agora:")
                clienteVenda = cadastrarCliente()
                # Propagar no banco para receber um idCliente
                daoCliente.incluir(clienteVenda)
                # Procurando no banco, em busca do idCliente
                clienteVenda = daoCliente.retornarUltimoCliente(clienteVenda)

                # Atribuindo cliente corretamente na Venda
                venda.idCliente = clienteVenda.idCliente

            # Inclui a venda no Banco de Dados
            daoVenda.incluir(venda)

            # Gera cada Item Venda para a venda atual
            venda = daoVenda.retornarUltimaVenda(venda)

            if venda.idVenda != -1:
                print("Venda #{}\n".format(int(venda.idVenda)))
                itemNumero = 1
                while continuarItemVendas:
                    print("Item Venda #{}\n".format(itemNumero))
                    itemVenda = cadastrarItemVenda(venda.idVenda)
                    venda.valortotal = float(venda.valortotal) + (itemVenda.quantidade * float(itemVenda.valor))
                    daoItemVenda.incluir(itemVenda)

                    # Atualizar o estoque do produto
                    daoProduto.atualizarEstoque(itemVenda.idProduto, itemVenda.quantidade)

                    c = int(input("\nContinuar inserindo Itens?\n\t0 - ENCERRAR\n\t: "))
                    if c == 0:
                        continuarItemVendas = False
                    itemNumero = itemNumero + 1
                daoVenda.alterar(venda)

                c = int(input("\nContinuar inserindo Vendas?\n\t0 - ENCERRAR\n\t: "))
                if c == 0:
                    continuarVendas = False
    # Listar todas as Vendas realizadas

    if opcao == 3:
        # listaVendas = []
        listaVendas = daoVenda.listarTodos()
        for venda in listaVendas:
            print(Venda().apresentarVenda(venda))

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
        cliente = daoCliente.procuraPorID(chaveProcura)

        if cliente.idCliente != -1:
            print("\nInformações do cliente ::")
            print(cliente)

            print("Compras realizadas:")
            listaVendas = daoVenda.procurarPorCliente(cliente.idCliente)
            if listaVendas != -1:
                for venda in listaVendas:
                    somatorio = somatorio + venda[2]
                    print(Venda().apresentarVenda(venda))
                print("O cliente realizou R${} em compras".format(somatorio))
            else:
                print("\tO cliente não possuiu compras realizadas.")
