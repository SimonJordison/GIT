import sys

def convertir_pesos_chilenos(tasas, cantidad):
    conversiones = {}
    for divisa, tasa in tasas.items():
        conversiones[divisa] = cantidad * tasa
    return conversiones

def main():
    if len(sys.argv) != 5:
        sys.exit(1)

    try:
        tasas = {
            'Soles': float(sys.argv[1]),
            'Pesos_Argentinos': float(sys.argv[2]),
            'Dólares': float(sys.argv[3])
        }
        cantidad_en_pesos = float(sys.argv[4])
    except ValueError:
        print("Error: Los argumentos deben ser números.")
        sys.exit(1)

    conversiones = convertir_pesos_chilenos(tasas, cantidad_en_pesos)

    print(f"Los {cantidad_en_pesos} pesos equivalen a:")
    for divisa, cantidad in conversiones.items():
        print(f"{cantidad} {divisa}")

if __name__ == "__main__":
    main()
