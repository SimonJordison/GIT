# anuncio.py

from error import SubTipoInvalidoException

class Anuncio:
    def __init__(self, alto, ancho, sub_tipo):
        self.alto = alto if alto > 0 else 1
        self.ancho = ancho if ancho > 0 else 1
        self._sub_tipo = None
        self.sub_tipo = sub_tipo  # Usar el setter para validación
        self.url_archivo = ""
        self.url_clic = ""
    
    @property
    def sub_tipo(self):
        return self._sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, valor):
        if valor not in self.SUB_TIPOS:
            raise SubTipoInvalidoException(f"Subtipo '{valor}' no es válido para el tipo '{self.__class__.__name__}'")
        self._sub_tipo = valor
    
    @staticmethod
    def mostrar_formatos():
        for cls in Anuncio.__subclasses__():
            print(f"{cls.__name__.upper()}:")
            print("=" * 10)
            for subtipo in cls.SUB_TIPOS:
                print(f"- {subtipo}")
            print()
    
class Video(Anuncio):
    SUB_TIPOS = ("Corto", "Largo")

    def __init__(self, sub_tipo, duracion):
        super().__init__(1, 1, sub_tipo)
        self.duracion = duracion if duracion > 0 else 5
    
    @property
    def duracion(self):
        return self._duracion
    
    @duracion.setter
    def duracion(self, valor):
        self._duracion = valor if valor > 0 else 5
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    SUB_TIPOS = ("Banner", "Sidebar")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    SUB_TIPOS = ("Facebook", "Instagram")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
