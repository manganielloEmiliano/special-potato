class Imagen():
    def __init__(self, Imagen):
        self.Imagen = Imagen

    @property
    def Imagen(self):
        return self.__Imagen

    @Imagen.setter
    def Imagen(self, valor):
        self.__Imagen = valor
    def __str__(self):
        return self.descripcion