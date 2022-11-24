
class TipoContratacion():
    def __init__(self, descripcion):
        self.descripcion = descripcion

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor
    def __str__(self):
        return self.descripcion

        