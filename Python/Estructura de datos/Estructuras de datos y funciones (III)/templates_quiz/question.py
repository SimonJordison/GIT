from preguntas import pool_preguntas
from shuffle import shuffle_alt

def choose_q(dificultad):
    preguntas = pool_preguntas[dificultad]
    pregunta_elegida = preguntas.pop(0)  # Eliminar y devolver la primera pregunta
    return pregunta_elegida['enunciado'], shuffle_alt(pregunta_elegida)
