with open('baseAtributos.txt') as handle:
     dados = handle.read().split("\n")

nomeclasse = "ItemVenda:"
with open('Trabalho Banco de Dados/modelo/ItemVenda.py', 'w') as arquivo:

    arquivo.write('class {} \n'.format(nomeclasse))
    arquivo.write('\n')
    arquivo.write("   def __init__(self):\n")

    for i in dados:
        arquivo.write("        __{} = '' \n".format(i))

    arquivo.write("\n")
    for i in dados:
        arquivo.write('   @property \n')
        arquivo.write('   def {}(self): \n'.format(i))
        arquivo.write('       return self.__{} \n'.format(i))
        arquivo.write('\n')

    for i in dados:
        arquivo.write('   @{}.setter \n'.format(i))
        arquivo.write('   def {}(self,entrada): \n'.format(i))
        arquivo.write('       self.__{} = entrada\n'.format(i))
        arquivo.write('\n')

    arquivo.write('   def __eq__(self,entrada): \n'.format(i))
    arquivo.write('       self.__xxxxxxxxxxx == entrada.xxxxxxx\n')
    arquivo.write("\n")
    arquivo.write('   def __repr__(self,entrada): \n'.format(i))
    arquivo.write('       return self.__xxxxxxxxxxx \n')

handle.close()
arquivo.close()
