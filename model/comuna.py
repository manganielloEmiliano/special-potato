class Comuna():
    def __init__(self, numero):
        self.numero = numero

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        self.__numero = valor
    
    def __str__(self):
        return " la comuna: " + self.numero
