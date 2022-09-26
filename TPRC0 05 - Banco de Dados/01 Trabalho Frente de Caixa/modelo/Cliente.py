class Cliente: 

   def __init__(self):
        __idCliente = '' 
        __nome = '' 
        __endereco = '' 
        __telefone = '' 
        __email = '' 
        __cidade = '' 
        __uf = '' 
        __cep = '' 

   @property 
   def idCliente(self): 
       return self.__idCliente 

   @property 
   def nome(self): 
       return self.__nome 

   @property 
   def endereco(self): 
       return self.__endereco 

   @property 
   def telefone(self): 
       return self.__telefone 

   @property 
   def email(self): 
       return self.__email 

   @property 
   def cidade(self): 
       return self.__cidade 

   @property 
   def uf(self): 
       return self.__uf 

   @property 
   def cep(self): 
       return self.__cep 

   @idCliente.setter 
   def idCliente(self,entrada): 
       self.__idCliente = entrada

   @nome.setter 
   def nome(self,entrada): 
       self.__nome = entrada

   @endereco.setter 
   def endereco(self,entrada): 
       self.__endereco = entrada

   @telefone.setter 
   def telefone(self,entrada): 
       self.__telefone = entrada

   @email.setter 
   def email(self,entrada): 
       self.__email = entrada

   @cidade.setter 
   def cidade(self,entrada): 
       self.__cidade = entrada

   @uf.setter 
   def uf(self,entrada): 
       self.__uf = entrada

   @cep.setter 
   def cep(self,entrada): 
       self.__cep = entrada

   def __eq__(self,entrada): 
       self.__xxxxxxxxxxx == entrada.xxxxxxx

   def __repr__(self,entrada): 
       return self.__xxxxxxxxxxx 
