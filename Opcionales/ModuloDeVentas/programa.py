from venta import Venta

venta = Venta()
opcion = int(input(f"""
Desea ingresar un item a la venta? 

1. Si
2. No
                   

"""))

while opcion == 1:
    producto = input(f"""
Ingrese nombre del producto: """)
    
    cantidad = int(input(f"""
Ingrese cantidad vendida del producto: """))

    venta.modificar_detalle(producto, cantidad)
    opcion = int(input(f"""
Desea ingresar un item a la venta? 

1. Si
2. No
                   

"""))
    
print(venta.detalle)


