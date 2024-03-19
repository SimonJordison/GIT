# Paso 1: Importar el módulo sys para usar argumentos de la línea de comandos
import sys

# Definir la función para filtrar los productos
def filtrar(precios, umbral, mayor_que=True):
    # Completar: Inicializar una lista vacía para guardar los nombres de los productos filtrados
    filtro = []

    if mayor_que:
        # Completar: Usar una comprensión de lista para filtrar productos cuyo precio sea mayor que el umbral
        filtro = [producto for producto, precio in precios.items() if precio > umbral]

    else:
        # Completar: Similar al bloque anterior, pero para productos con precio menor que el umbral
        filtro = [producto for producto, precio in precios.items() if precio < umbral]

    # Paso 4: Imprimir los resultados
    # Completar: Usar .join() para convertir la lista de nombres de productos en una cadena de texto formateada
    if mayor_que:
        print(f"Productos con precio mayor que {umbral}: {' '.join(filtro)}")
    else:
        print(f"Productos con precio menor que {umbral}: {' '.join(filtro)}")

# Paso 5: Controlar el flujo del script basado en los argumentos proporcionados
if __name__ == "__main__":
    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }
    if len(sys.argv) == 2:
        # Obtener el umbral desde los argumentos de la línea de comandos. Convertirlo a float para manejar números con decimales.
        umbral = float(sys.argv[1])
        # Llamar a la función filtrar solo con el umbral, usando el valor por defecto para 'mayor_que'
        filtrar(precios, umbral)
    elif len(sys.argv) == 3:
        # Verificar si el segundo argumento es 'mayor' o 'menor' y llamar a la función filtrar con el valor adecuado para 'mayor_que'
        umbral = float(sys.argv[1])
        if sys.argv[2] == 'mayor':
            filtrar(precios, umbral, mayor_que=True)
        elif sys.argv[2] == 'menor':
            filtrar(precios, umbral, mayor_que=False)
        else:
            print("El segundo argumento debe ser 'mayor' o 'menor'.")
    else:
        print("Uso: python script.py umbral [mayor|menor]")
