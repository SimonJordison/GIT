
def validate(opciones):
    eleccion = input("Ingrese una opción válida: ")
    while eleccion not in opciones:
        print("Opción no válida, ingrese una de las opciones válidas: ")
        eleccion = input("Ingrese una opción válida: ")
    return eleccion

if __name__ == '__main__':
    opciones = ['opcion1', 'opcion2', 'opcion3']  # Ejemplo de opciones
    eleccion = validate(opciones)
    print("Ha elegido:", eleccion)
