class Produto: 

   def __init__(self):
        __idProduto = '' 
        __nome = '' 
        __quantidade = '' 
        __valor = '' 

   @property 
   def idProduto(self): 
       return self.__idProduto 

   @property 
   def nome(self): 
       return self.__nome 

   @property 
   def quantidade(self): 
       return self.__quantidade 

   @property 
   def valor(self): 
       return self.__valor 

   @idProduto.setter 
   def idProduto(self,entrada): 
       self.__idProduto = entrada

   @nome.setter 
   def nome(self,entrada): 
       self.__nome = entrada

   @quantidade.setter 
   def quantidade(self,entrada): 
       self.__quantidade = entrada

   @valor.setter 
   def valor(self,entrada): 
       self.__valor = entrada

   def __eq__(self,entrada): 
       self.__xxxxxxxxxxx == entrada.xxxxxxx

   def __repr__(self,entrada): 
       return self.__xxxxxxxxxxx 
