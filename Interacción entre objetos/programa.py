from tienda import Restaurante, Supermercado, Farmacia

def crear_tienda():
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo = input("Ingrese el tipo de tienda (Restaurante, Supermercado, Farmacia): ")

    if tipo == "Restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo == "Supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo == "Farmacia":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return None

def ingresar_productos(tienda):
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        tienda.ingresar_producto(nombre, precio, stock)
        continuar = input("¿Desea ingresar otro producto? (s/n): ")
        if continuar.lower() != 's':
            break

def listar_productos(tienda):
    print(tienda.listar_productos())

def realizar_venta(tienda):
    nombre = input("Ingrese el nombre del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    tienda.realizar_venta(nombre, cantidad)

def main():
    tienda = crear_tienda()
    if tienda is None:
        return

    while True:
        print("1. Ingresar productos")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ingresar_productos(tienda)
        elif opcion == "2":
            listar_productos(tienda)
        elif opcion == "3":
            realizar_venta(tienda)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
