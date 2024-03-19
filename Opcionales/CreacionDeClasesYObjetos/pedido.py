from te import Te

# Solicitar datos al usuario
sabor = int(input("Ingrese el número correspondiente al sabor (1 para té negro, 2 para té verde, 3 para agua de hierbas): "))
formato = int(input("Ingrese el formato (300 gr o 500 gr): "))

# Obtener información del té
tiempo, recomendacion = Te.obtener_tiempo_y_recomendacion(sabor)
precio = Te.obtener_precio(formato)

# Mostrar detalle del pedido
if tiempo is not None and recomendacion is not None and precio is not None:
    if sabor == 1:
        nombre_sabor = "Té negro"
    elif sabor == 2:
        nombre_sabor = "Té verde"
    elif sabor == 3:
        nombre_sabor = "Agua de hierbas"
    
    print("Detalle del pedido:")
    print(f"Sabor: {nombre_sabor}")
    print(f"Formato: {formato} gr")
    print(f"Precio: ${precio}")
    print(f"Tiempo de preparación: {tiempo} minutos")
    print(f"Recomendación: {recomendacion}")
else:
    print("Error: Sabor o formato no válidos.")
