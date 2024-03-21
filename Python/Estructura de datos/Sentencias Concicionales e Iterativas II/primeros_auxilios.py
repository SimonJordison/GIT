def inicio():
    print("Inicio del programa.")
    responder_estimulos()

def responder_estimulos():
    respuesta = input("¿Responde a estímulos? (SI/NO): ").upper()
    if respuesta == "SI":
        print("Valorar la necesidad de llevarlo al hospital más cercano. Fin del programa.")
    elif respuesta == "NO":
        abrir_via_aerea()
    else:
        print("Respuesta inválida. Por favor, responda con 'SI' o 'NO'.")
        responder_estimulos()

def abrir_via_aerea():
    print("Abrir vía aérea.")
    respira()

def respira():
    respuesta = input("¿Respira? (SI/NO): ").upper()
    if respuesta == "SI":
        print("Permitir posición de suficiente ventilación. Fin del programa.")
    elif respuesta == "NO":
        administrar_ventilaciones()
    else:
        print("Respuesta inválida. Por favor, responda con 'SI' o 'NO'.")
        respira()

def administrar_ventilaciones():
    print("Administrar 5 ventilaciones y llamar ambulancia.")
    signos_de_vida()

def signos_de_vida():
    respuesta = input("¿Signos de vida? (SI/NO): ").upper()
    if respuesta == "SI":
        print("Reevaluar a la espera de la ambulancia.")
        llego_ambulancia()
    elif respuesta == "NO":
        administrar_compresiones_toracicas()
    else:
        print("Respuesta inválida. Por favor, responda con 'SI' o 'NO'.")
        signos_de_vida()

def administrar_compresiones_toracicas():
    print("Administrar compresiones torácicas hasta que llegue la ambulancia.")

    # Simulando la llegada de la ambulancia
    llegada_ambulancia = input("¿Llegó la ambulancia? (SI/NO): ").upper()
    if llegada_ambulancia == "SI":
        print("La ambulancia ha llegado. Fin del programa.")
    else:
        print("La ambulancia aún no ha llegado. Continuar administrando compresiones torácicas.")

        # Volvemos a llamar a esta misma función recursivamente hasta que llegue la ambulancia
        administrar_compresiones_toracicas()

def llego_ambulancia():
    llegada_ambulancia = input("¿Llegó la ambulancia? (SI/NO): ").upper()
    if llegada_ambulancia == "SI":
        print("La ambulancia ha llegado. Fin del programa.")
    elif llegada_ambulancia == "NO":
        signos_de_vida()
    else:
        print("Respuesta inválida. Por favor, responda con 'SI' o 'NO'.")
        llego_ambulancia()

# Inicio del programa
inicio()
