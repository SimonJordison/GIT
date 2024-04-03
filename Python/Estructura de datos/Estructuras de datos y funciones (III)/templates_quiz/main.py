# # No modificar
# from verify import verificar
# import preguntas as p
# from question import choose_q
# from print_preguntas import print_pregunta
# from level import choose_level
# from validador import validate
# import time
# import os
# import sys

# # valores iniciales - 
# n_pregunta = 0
# continuar = 'y'
# correcto = True
# p_level = 10
# op_sys = 'cls' if sys.platform == 'win32' else 'clear'


# # ----------------------------------------

# os.system(op_sys) # limpiar pantalla

# print('Bienvenido a la Trivia')
# opcion = input('''Ingrese una opción para Jugar!
#         1. Jugar
#         0. Salir
        
#     > ''')
# # 1. validar opcion
# opcion = validate(['0', '1'])

# # 2. Definir el comportamiento de Salir
# if opcion == '0':
#     print()
#     time.sleep(2)
#     os.system(op_sys)
#     # finalizar programa
#     print("Nos vemos pronto!")
#     exit()

# # Funcionamiento de preguntas
# while correcto and n_pregunta < 3*p_level:
    
#     if n_pregunta == 0:
#         p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
#         # 3. Validar el número de preguntas por nivel
#         p_level = validate(['1', '2', '3'])
        
#     if continuar == 'y':
#         #contador de preguntas
#         n_pregunta += 1
#         # 4. Escoger el nivel de la pregunta
#         nivel = choose_level(n_pregunta, int(p_level))
#         print(f'Pregunta {n_pregunta}:')
#         # 5. Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
#         enunciado, alternativas = choose_q(nivel)
#         #6. Imprimir el enunciado y sus alternativas en pantalla
#         print_pregunta(enunciado, alternativas)
        
#         respuesta = input('Escoja la alternativa correcta:\n> ').lower()
#         # 7. Validar la respuesta entregada
#         respuesta = validate(['a', 'b', 'c', 'd'])
#         # 8. Verificar si la respuesta es correcta o no
#         correcto = verificar(alternativas, ord(respuesta) - 97)
        
#         if correcto and n_pregunta < 3*p_level:
#             print('Muy bien sigue así!')
#             continuar = input('Desea continuar? [y/n]: ').lower()
#             #9. Validar si es que se responde y o n
#             continuar = validate(['y', 'n'])
#             os.system(op_sys)
#         elif correcto and n_pregunta == 3*p_level:
#             print(f'Felicitaciones, Has respondido {3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
#             time.sleep(3)
#             os.system(op_sys)
#             exit()
#         else: 
#             print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas,\n Sigue participando!!')
#             time.sleep(3)
#             exit()
#     else: 
#         print('Nos vemos la proxima vez, sigue practicando')
#         time.sleep(3)
#         exit()

# No modificar
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import time
import os
import sys

# Función para jugar
def jugar():
    # valores iniciales - 
    correcto = True
    p_level = 10
    op_sys = 'cls' if sys.platform == 'win32' else 'clear'

    os.system(op_sys) # limpiar pantalla

    n_pregunta = 0
    while correcto and n_pregunta < 3*p_level:
        if n_pregunta % p_level == 0:
            p_level = int(input('¿Cuántas preguntas por nivel? (Máximo 3): '))
            p_level = validate(['1', '2', '3'])

        n_pregunta += 1
        nivel = choose_level(n_pregunta, p_level)
        print(f'Pregunta {n_pregunta}, nivel: {nivel}')
        enunciado, alternativas = choose_q(nivel)
        print_pregunta(enunciado, alternativas)

        opciones_validas = ['A', 'B', 'C', 'D']
        print("Opciones válidas:", ", ".join(opciones_validas))
        
        respuesta = input('Escoja la alternativa correcta:\n> ').upper()
        respuesta = validate(opciones_validas)
        correcto = verificar(alternativas, ord(respuesta) - 65)

        if correcto and n_pregunta < 3*p_level:
            print('Muy bien sigue así!')
            continuar = input('Desea continuar? [y/n]: ').lower()
            continuar = validate(['y', 'n'])
            os.system(op_sys)
        elif correcto and n_pregunta == 3*p_level:
            print(f'Felicitaciones, Has respondido {3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
            time.sleep(3)
            os.system(op_sys)
            return
        else: 
            print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas,\n Sigue participando!!')
            time.sleep(3)
            return

# ----------------------------------------

# No modificar
print('Bienvenido a la Trivia')

while True:
    opcion = input('''Ingrese una opción para Jugar!
        1. Jugar
        0. Salir
        
    > ''')
    opcion = validate(['0', '1'])

    if opcion == '0':
        print("Nos vemos pronto!")
        break
    elif opcion == '1':
        jugar()
