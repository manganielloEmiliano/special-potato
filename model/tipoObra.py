class TipoObra():
    def __init__(self, descripcion):
        self.descripcion = descripcion

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def cuit(self, valor):
        self.__descripcion = valor