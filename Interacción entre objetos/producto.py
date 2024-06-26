class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = max(0, value)

    def __add__(self, other):
        if isinstance(other, Producto) and self.__nombre == other.__nombre:
            return Producto(self.__nombre, self.__precio, self.__stock + other.__stock)
        return self

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.__nombre == other.__nombre
        return False

    def __str__(self):
        return f"{self.__nombre} - ${self.__precio} - Stock: {self.__stock}"
