class Empresa():
    def __init__(self, cuit, nombre) -> None:
        self.cuit = cuit
        self.razon_social = nombre
    
    @property
    def cuit(self):
        return self.__cuit
    
    @cuit.setter
    def cuit(self, valor):
        self.__cuit = valor
    
    @property
    def razon_social(self):
        return self.__razon_social
    
    @razon_social.setter
    def razon_social(self, valor):
        self.__razon_social = valor
    
    def __str__(self):
        return " el cuit de la empresa es:" + str(self.cuit )+  "\n la razon social es:"+str(self.razon_social)