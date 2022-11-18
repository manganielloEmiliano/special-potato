from model.comuna import Comuna 


class Barrio():
    def __init__(self, nombre, comuna:Comuna):
        self.nombre = nombre
        self.comuna = comuna

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def comuna(self):
        return self.__comuna

    @comuna.setter
    def comuna(self, valor):
        self.__comuna = valor

    def __str__(self):
        return "barrio: " + self.nombre + " de la comuna: " + self.comuna
