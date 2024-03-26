import sys

def contar_caracteres_distintos(texto):
    return len(set(texto))

def contar_palabras_distintas(texto):
    return len(set(texto.split()))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    archivo = sys.argv[1]

    try:
        with open(archivo, "r", encoding="utf-8") as file:
            texto = file.read()
    except FileNotFoundError:
        sys.exit(1)

    num_caracteres_distintos = contar_caracteres_distintos(texto)
    num_palabras_distintas = contar_palabras_distintas(texto)

    print(f"El número de caracteres distintos es: {num_caracteres_distintos}")
    print(f"El número de palabras distintas es: {num_palabras_distintas}")
