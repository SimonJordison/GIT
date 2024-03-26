# Lista de recordatorios proporcionada
recordatorios = [
    ['2021-01-01', '11:00', 'Levantarse y ejercitar'],
    ['2021-07-15', '13:00', 'No hacer nada es feriado'],
    ['2021-09-18', '16:00', 'Ramadas']
]

# 1. Agregar un evento el 2 de Febrero de 2021 a las 6 de la mañana para "Empezar el Año"
nuevo_evento = ['2021-02-02', '06:00', 'Empezar el año']
recordatorios.append(nuevo_evento)

# 2. Corregir el evento del 15 de Julio para que sea el 16 de Julio
for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'

# 3. Eliminar el evento del día del trabajo
recordatorios = [evento for evento in recordatorios if evento[2] != 'Día del Trabajo']

# 4. Agregar una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
cena_navidad = ['2021-12-24', '22:00', 'Cena de Navidad']
navidad = ['2021-12-25', '00:00', 'Navidad']
cena_ano_nuevo = ['2021-12-31', '22:00', 'Cena de Año Nuevo']

recordatorios.append(cena_navidad)
recordatorios.append(navidad)
recordatorios.append(cena_ano_nuevo)

# Ordenar los eventos por fecha y hora
recordatorios.sort()

# Imprimir la lista final de recordatorios
for evento in recordatorios:
    print(evento)