from personaje import Personaje
import random #Aleatorio para probabilidades

print("Bienvenido a Gran Fantasía")
nombre = input("Por favor indique nombre de su personaje: \n")

p = Personaje(nombre)
print("Oh no, ha aparecido un orco!")

o = Personaje('Orco')
probabilidad_ganar = p.get_probabilidad_de_ganar(o)
opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

while opcion_orco == 1:
    numero = random.uniform(0,1)
    
    resultado = 'G' if numero < probabilidad_ganar else 'P'

    #Otra opcion de validar probabilidad de ganar

    #resultado = ''

    # if numero < probabilidad_ganar:
    #     resultado = 'G'
    # else:
    #     resultado = 'P'
    if resultado == 'G':
        print(f"""Le has ganado al orco, felicidades""
        Recibirás 50 puntos de experiencia! """)
        p.estado = 50
        o.estado = -30
    elif resultado == 'P':
        print(f"""Oh no, el orco te ha ganado
        Has perdido 30 puntos de experiencia!  """)
        p.estado = -30
        o.estado = 50

    print(p.estado)
    print(o.estado)
    probabilidad_ganar = p.get_probabilidad_de_ganar(o)
    opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)
print("Has huido, el orco ha quedado atras")




        
















