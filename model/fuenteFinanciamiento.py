class FuenteFinanciamiento():
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def descripcion(self):
        return self.__nombre

    @descripcion.setter
    def cuit(self, valor):
        self.__nombre = valor
    def __str__(self):
        return " la comuna: " + self.nombre