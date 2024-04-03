import random

def shuffle_alt(pregunta):
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    return alternativas
