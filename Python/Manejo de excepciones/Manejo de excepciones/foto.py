from error import DimensionError

class Foto:

    MAX = 2500

    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._alto <= 0 and self._alto > Foto.MAX :
            raise DimensionError("El alto debe ser un número positivo y no mayor a 2500 pixeles", dimension="alto", maximo=None)
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._ancho <= 0 and self._ancho > Foto.MAX :
            raise DimensionError("El ancho debe ser un número positivo y no mayor a 2500 pixeles", dimension="Ancho", maximo=None)
        self._ancho = ancho
