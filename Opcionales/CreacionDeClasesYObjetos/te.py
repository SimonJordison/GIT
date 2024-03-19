class Te:
    # Atributos de clase
    precio_300gr = 3000
    precio_500gr = 5000

    @staticmethod
    def obtener_tiempo_y_recomendacion(sabor):
        if sabor == 1:
            return 3, "Se recomienda consumir el té negro al desayuno."
        elif sabor == 2:
            return 5, "Se recomienda consumir el té verde al medio día."
        elif sabor == 3:
            return 6, "Se recomienda consumir el agua de hierbas al atardecer."
        else:
            return None, None

    @staticmethod
    def obtener_precio(formato):
        if formato == 300:
            return Te.precio_300gr
        elif formato == 500:
            return Te.precio_500gr
        else:
            return None
