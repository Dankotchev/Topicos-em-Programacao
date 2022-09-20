class Venda: 

   def __init__(self):
        __idvenda = '' 
        __data = '' 
        __valortotal = '' 
        __idcliente = '' 

   @property 
   def idvenda(self): 
       return self.__idvenda 

   @property 
   def data(self): 
       return self.__data 

   @property 
   def valortotal(self): 
       return self.__valortotal 

   @property 
   def idcliente(self): 
       return self.__idcliente 

   @idvenda.setter 
   def idvenda(self,entrada): 
       self.__idvenda = entrada

   @data.setter 
   def data(self,entrada): 
       self.__data = entrada

   @valortotal.setter 
   def valortotal(self,entrada): 
       self.__valortotal = entrada

   @idcliente.setter 
   def idcliente(self,entrada): 
       self.__idcliente = entrada

   def __eq__(self,entrada): 
       self.__xxxxxxxxxxx == entrada.xxxxxxx

   def __repr__(self,entrada): 
       return self.__xxxxxxxxxxx 
