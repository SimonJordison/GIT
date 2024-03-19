# Paso 1: Definir la función para calcular la productoria de una lista de números
def productoria(lista):
    # Inicializar una variable para almacenar el resultado de la productoria
    resultado = 1
    # Iterar sobre cada elemento de la lista y multiplicarlo por el resultado acumulado
    for elemento in lista:
        resultado *= elemento
    # Retornar el resultado de la productoria
    return resultado

# Paso 2: Definir la función para calcular el factorial de un número
def factorial(n):
    # Inicializar una variable para almacenar el resultado del factorial
    resultado = 1
    # Iterar sobre un rango de 1 a n (inclusive) y multiplicar cada número por el resultado acumulado
    for numero in range(1, n + 1):
        resultado *= numero
    # Retornar el resultado del factorial
    return resultado

# Paso 3: Definir una función que maneje los cálculos basada en los parámetros recibidos
def calcular(**parametros):
    # Iterar sobre cada par clave-valor de los parámetros
    for clave, valor in parametros.items():
        # Determinar si la clave indica un cálculo de factorial
        if 'fact' in clave:
            # Llamar a la función factorial y imprimir el resultado con un mensaje adecuado
            print(f"Factorial de {valor}: {factorial(valor)}")
        # Determinar si la clave indica un cálculo de productoria
        elif 'prod' in clave:
            # Llamar a la función productoria y imprimir el resultado con un mensaje adecuado
            print(f"Productoria de {valor}: {productoria(valor)}")

# Paso 4: Ejecutar la función calcular con ejemplos de factorial y productoria
# Llamar a la función calcular con diferentes combinaciones de argumentos para probar su funcionamiento
calcular(fact_1=1, prod_2=[1, 2], fact_3=3, prod_4=[1, 2, 3, 4])
