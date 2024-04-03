def print_pregunta(enunciado, alternativas):
    print(enunciado)
    letras = ['A', 'B', 'C', 'D']
    for i, alternativa in enumerate(alternativas):
        print(f"{letras[i]}. {alternativa}")
