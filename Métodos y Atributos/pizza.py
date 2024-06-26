class Pizza:
    # Atributos de clase
    precio = 10000
    tamaño = "familiar"
    ingredientes_proteicos = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    tipos_masa = ["tradicional", "delgada"]

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal_1 = None
        self.ingrediente_vegetal_2 = None
        self.tipo_masa = None
        self.pizza_valida = False

    @staticmethod
    def validar_elemento(elemento, lista_posibles):
        return elemento in lista_posibles

    def realizar_pedido(self):
        proteico = input("Ingrese un ingrediente proteico: ").lower()
        if not self.validar_elemento(proteico, self.ingredientes_proteicos):
            print("Ingrediente proteico no válido.")
            return
        
        vegetal_1 = input("Ingrese el primer ingrediente vegetal: ").lower()
        if not self.validar_elemento(vegetal_1, self.ingredientes_vegetales):
            print("Primer ingrediente vegetal no válido.")
            return
        
        vegetal_2 = input("Ingrese el segundo ingrediente vegetal: ").lower()
        if not self.validar_elemento(vegetal_2, self.ingredientes_vegetales):
            print("Segundo ingrediente vegetal no válido.")
            return

        masa = input("Ingrese el tipo de masa: ").lower()
        if not self.validar_elemento(masa, self.tipos_masa):
            print("Tipo de masa no válido.")
            return

        self.ingrediente_proteico = proteico
        self.ingrediente_vegetal_1 = vegetal_1
        self.ingrediente_vegetal_2 = vegetal_2
        self.tipo_masa = masa

        self.pizza_valida = True
        print("Pedido realizado con éxito.")

### Archivo `evaluaciones.py`

```python
from pizza import Pizza

# a. Mostrar los atributos de clase
print("Precio de la pizza:", Pizza.precio)
print("Tamaño de la pizza:", Pizza.tamaño)
print("Ingredientes proteicos disponibles:", Pizza.ingredientes_proteicos)
print("Ingredientes vegetales disponibles:", Pizza.ingredientes_vegetales)
print("Tipos de masa disponibles:", Pizza.tipos_masa)

# b. Validar si "salsa de tomate" está en la lista ["salsa de tomate", "salsa bbq"]
print("¿'salsa de tomate' está en la lista ['salsa de tomate', 'salsa bbq']?",
      Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c. Crear una instancia de Pizza y realizar un pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Mostrar los ingredientes y tipo de masa de la instancia creada, y si es una pizza válida
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Primer ingrediente vegetal:", mi_pizza.ingrediente_vegetal_1)
print("Segundo ingrediente vegetal:", mi_pizza.ingrediente_vegetal_2)
print("Tipo de masa:", mi_pizza.tipo_masa)
print("¿Es una pizza válida?", mi_pizza.pizza_valida)

# e. Mostrar si la clase Pizza es una pizza válida (debería mostrar un error)
try:
    print("¿Es una pizza válida sin crear instancia?", Pizza.pizza_valida)
except AttributeError as e:
    print("Error esperado:", e)
