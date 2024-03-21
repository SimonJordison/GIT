from itertools import product
from string import ascii_lowercase

def fuerza_bruta(contraseña):
    intentos = 0
    for longitud in range(1, len(contraseña) + 1):
        for combinacion in product(ascii_lowercase, repeat=longitud):
            intentos += 1
            if ''.join(combinacion) == contraseña:
                return intentos

if __name__ == "__main__":
    contraseña = input("Ingrese la contraseña: ")
    intentos = fuerza_bruta(contraseña)
    print(f"La contraseña fue forzada en {intentos} intentos")
