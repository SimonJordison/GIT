class Medicamento():
    descuento = 0.5
    IVA = 0.19

    @staticmethod
    def validar_mayor_a_cero(numero:int):
        return numero > 0 