# demo.py

from campana import Campaña
from error import SubTipoInvalidoException, LargoExcedidoException

# Crear una campaña con un anuncio de tipo Video
anuncios_data = [
    {"tipo": "Video", "sub_tipo": "Corto", "duracion": 10}
]

campaña = Campaña("Campaña Inicial", anuncios_data)

try:
    nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: ")
    campaña.nombre = nuevo_nombre
except LargoExcedidoException as e:
    with open("error.log", "a") as log:
        log.write(f"{str(e)}\n")

try:
    nuevo_sub_tipo = input("Ingrese un nuevo subtipo para el anuncio: ")
    campaña.anuncios[0].sub_tipo = nuevo_sub_tipo
except SubTipoInvalidoException as e:
    with open("error.log", "a") as log:
        log.write(f"{str(e)}\n")

print(campaña)