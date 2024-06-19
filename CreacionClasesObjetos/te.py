# te.py

class Te:
    DURACION = 365  # duración en días

    def __init__(self, sabor, formato):
        self.sabor = sabor
        self.formato = formato

    @staticmethod
    def obtener_tiempo_recomendacion(sabor):
        if sabor == 1:
            return 3, "Consuma al desayuno"
        elif sabor == 2:
            return 5, "Consuma al medio día"
        elif sabor == 3:
            return 6, "Consuma al atardecer"
        else:
            raise ValueError("Sabor no válido")

    @staticmethod
    def obtener_precio(formato):
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        else:
            raise ValueError("Formato no válido")

# Fin de te.py
