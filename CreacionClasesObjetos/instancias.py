# instancias.py

from te import Te

# Crear dos instancias
te_negro = Te(1, 300)
te_verde = Te(2, 500)

# Almacenar el tipo de dato de cada instancia creada en una variable
tipo_te_negro = type(te_negro)
tipo_te_verde = type(te_verde)

# Mostrar por pantalla el valor de cada tipo de dato almacenado
print(tipo_te_negro)
print(tipo_te_verde)

# Verificar si ambos tipos son iguales y mostrar el mensaje correspondiente
if tipo_te_negro == tipo_te_verde:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")

# Fin de instancias.py
