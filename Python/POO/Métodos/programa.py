from medicamento import Medicamento

precio = int(imput("Ingrese un precio a validar: "))
es_valido = Medicamento.validar_mayor_a_cero(precio)

