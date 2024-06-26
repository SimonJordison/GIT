from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery

    def ingresar_producto(self, nombre, precio, stock=0):
        nuevo_producto = Producto(nombre, precio, stock)
        for producto in self.__productos:
            if producto == nuevo_producto:
                producto.stock += stock
                return
        self.__productos.append(nuevo_producto)

    def listar_productos(self):
        return '\n'.join(str(producto) for producto in self.__productos)

    def realizar_venta(self, nombre, cantidad):
        pass

    def __str__(self):
        return f"Tienda: {self.__nombre} - Costo de delivery: {self.__costo_delivery}"

class Restaurante(Tienda):
    def ingresar_producto(self, nombre, precio, stock=0):
        super().ingresar_producto(nombre, precio, 0)

    def listar_productos(self):
        return '\n'.join(f"{producto.nombre} - ${producto.precio}" for producto in self._Tienda__productos)

    def realizar_venta(self, nombre, cantidad):
        pass  # No se modifica el stock en restaurantes

class Supermercado(Tienda):
    def listar_productos(self):
        productos_str = []
        for producto in self._Tienda__productos:
            stock_info = f" - Stock: {producto.stock}"
            if producto.stock < 10:
                stock_info += " (Pocos productos disponibles)"
            productos_str.append(f"{producto.nombre} - ${producto.precio}{stock_info}")
        return '\n'.join(productos_str)

    def realizar_venta(self, nombre, cantidad):
        for producto in self._Tienda__productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                else:
                    producto.stock = 0

class Farmacia(Tienda):
    def listar_productos(self):
        productos_str = []
        for producto in self._Tienda__productos:
            precio_info = f" - ${producto.precio}"
            if producto.precio > 15000:
                precio_info += " (Envío gratis al solicitar este producto)"
            productos_str.append(f"{producto.nombre}{precio_info}")
        return '\n'.join(productos_str)

    def realizar_venta(self, nombre, cantidad):
        if cantidad > 3:
            return
        for producto in self._Tienda__productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                else:
                    producto.stock = 0
