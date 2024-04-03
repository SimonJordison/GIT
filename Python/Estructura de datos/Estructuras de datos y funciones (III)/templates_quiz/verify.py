def verificar(alternativas, eleccion):
    if alternativas[eleccion] == 1:
        print("Respuesta Correcta")
        return True
    else:
        print("Respuesta Incorrecta")
        return False
