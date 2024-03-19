from te import Te

# Creación de instancias
te_negro = Te()
te_verde = Te()

# Almacenamiento de tipos
tipo_te_negro = type(te_negro)
tipo_te_verde = type(te_verde)

# Comparación de tipos
if tipo_te_negro == tipo_te_verde:
    print("Ambos objetos son del mismo tipo.")
else:
    print("Los objetos no son del mismo tipo.")
