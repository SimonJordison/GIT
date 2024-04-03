def choose_level(n_pregunta, preguntas_por_nivel):
    if preguntas_por_nivel == 1:
        if n_pregunta % 3 == 0:
            return "avanzada"
        elif n_pregunta % 2 == 0:
            return "intermedia"
        else:
            return "básica"
    elif preguntas_por_nivel == 2:
        if n_pregunta <= 2:
            return "básica"
        elif n_pregunta <= 4:
            return "intermedia"
        else:
            return "avanzada"
    elif preguntas_por_nivel == 3:
        if n_pregunta <= 3:
            return "básica"
        elif n_pregunta <= 6:
            return "intermedia"
        else:
            return "avanzada"
