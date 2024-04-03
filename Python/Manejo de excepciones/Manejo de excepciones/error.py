class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo=None):
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is not None and self.maximo is not None:
            return f"{self.dimension} no cumple con el requisito máximo de {self.maximo}: {self.args[0]}"
        elif self.dimension is not None:
            return f"La dimensión {self.dimension} es inválida: {self.args[0]}"
        else:
            return super().__str__()
