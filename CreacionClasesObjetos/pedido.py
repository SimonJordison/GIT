# pedido.py

from te import Te

# Solicitar al usuario que ingrese los detalles del pedido
sabor = int(input("Ingrese el sabor del té (1: Té negro, 2: Té verde, 3: Agua de hierbas): "))
formato = int(input("Ingrese el formato del té (300 o 500 gramos): "))

# Obtener los valores necesarios utilizando la clase Te
tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor)
precio = Te.obtener_precio(formato)

# Determinar el nombre del sabor
if sabor == 1:
    nombre_sabor = "Té negro"
elif sabor == 2:
    nombre_sabor = "Té verde"
elif sabor == 3:
    nombre_sabor = "Agua de hierbas"
else:
    nombre_sabor = "Sabor no válido"

# Mostrar en pantalla el detalle del pedido
print(f"Detalle del pedido:")
print(f"Sabor del tipo de té: {nombre_sabor}")
print(f"Formato: {formato} gramos")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")

# Fin de pedido.py
