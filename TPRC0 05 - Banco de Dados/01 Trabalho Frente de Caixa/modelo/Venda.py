class Venda: 

   def __init__(self):
        __idVenda = '' 
        __data = '' 
        __valortotal = '' 
        __idCliente = '' 

   @property 
   def idVenda(self): 
       return self.__idVenda 

   @property 
   def data(self): 
       return self.__data 

   @property 
   def valortotal(self): 
       return self.__valortotal 

   @property 
   def idCliente(self): 
       return self.__idCliente 

   @idVenda.setter 
   def idVenda(self,entrada): 
       self.__idVenda = entrada

   @data.setter 
   def data(self,entrada): 
       self.__data = entrada

   @valortotal.setter 
   def valortotal(self,entrada): 
       self.__valortotal = entrada

   @idCliente.setter 
   def idCliente(self,entrada): 
       self.__idCliente = entrada

   def __eq__(self,entrada): 
       self.__xxxxxxxxxxx == entrada.xxxxxxx

   def __repr__(self,entrada): 
       return "Id Venda #{}\tId Cliente #{}\nData da Venda: {}\tTotal da Venda: R$ {}"\
           .format(self.idVenda, self.idCliente, self.data, self.valortotal)
