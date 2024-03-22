class Personaje:

    # Creación constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0


    # Getter
    @property
    def estado(self):
        return f"""
    Nombre: {self.nombre}
    Nivel: {self.nivel}
    Experiencia {self.experiencia}
    """


    # Setter
    @estado.setter
    def estado(self, exp):
        temporal_exp = self.experiencia + exp

        while temporal_exp >= 100:
            self.nivel += 1
            temporal_exp -= 100

        #ejemplo
        # -30 nivel 2 0 exp exp temporal es -30
        # nivel 1 70 exp
        while temporal_exp < 0:
            if self.nivel > 1:
                temporal_exp = exp + 100
                self.nivel -= 1
            else:
                temporal_exp = 0
        self.experiencia = temporal_exp


    # Método de instancia que retorna la probabilidad de la instancia actual de ganar respecto de otra instancia (opcional).
    def get_probabilidad_de_ganar(self,other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.5
        
    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(input(
            
            f"""Con tu nivel actual, tienes {probabilidad_ganar*100}% de probabilidades
            de ganarle al Orco.
            Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
            si pierdes, perderas 30 puntos de experiencia y el orco ganara 50.
            Que deseas hacer?
            1. Atacar
            2. Huir
            """
            ))
            

    def __lt__(self, other):
        return (
            self.nivel < other.nivel
        )  # este metodo se activa cuando yo aplico el menor que "<"


    def __gt__(self, other):
        return (
            self.nivel > other.nivel
        )  # este metodo se activa cuando yo aplico el mayor que ">"


    def __eq__(self, other):
        return (
            self.nivel == other.nivel
        )  # este metodo se activa cuando yo aplico el igual que "=="

    # Método que muestra diálogo de enfrentamiento al orco (incluyendo probabilidad de ganar) y retorna opción escogida por el jugador (opcional)
