class ItemVenda: 

   def __init__(self):
        __idVenda = '' 
        __idProduto = '' 
        __quantidade = '' 
        __valor = '' 

   @property 
   def idVenda(self): 
       return self.__idVenda 

   @property 
   def idProduto(self): 
       return self.__idProduto 

   @property 
   def quantidade(self): 
       return self.__quantidade 

   @property 
   def valor(self): 
       return self.__valor 

   @idVenda.setter 
   def idVenda(self,entrada): 
       self.__idVenda = entrada

   @idProduto.setter 
   def idProduto(self,entrada): 
       self.__idProduto = entrada

   @quantidade.setter 
   def quantidade(self,entrada): 
       self.__quantidade = entrada

   @valor.setter 
   def valor(self,entrada): 
       self.__valor = entrada

   def __eq__(self,entrada): 
       self.__xxxxxxxxxxx == entrada.xxxxxxx

   def __repr__(self,entrada): 
       return "Id Produto #{}\tQuantidade: {}\tValor uni: R${}"\
           .format(self.idProduto, self.quantidade, self.valor)
