# campaña.py

from anuncio import Video, Display, Social
from error import LargoExcedidoException

class Campaña:
    def __init__(self, nombre, anuncios_data):
        self.nombre = nombre
        self.anuncios = self._crear_anuncios(anuncios_data)
    
    def _crear_anuncios(self, anuncios_data):
        anuncios = []
        for anuncio_data in anuncios_data:
            tipo = anuncio_data['tipo']
            if tipo == 'Video':
                anuncios.append(Video(anuncio_data['sub_tipo'], anuncio_data['duracion']))
            elif tipo == 'Display':
                anuncios.append(Display(anuncio_data['alto'], anuncio_data['ancho'], anuncio_data['sub_tipo']))
            elif tipo == 'Social':
                anuncios.append(Social(anuncio_data['alto'], anuncio_data['ancho'], anuncio_data['sub_tipo']))
        return anuncios
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if len(valor) > 250:
            raise LargoExcedidoException("El nombre de la campaña no puede superar los 250 caracteres")
        self._nombre = valor
    
    @property
    def anuncios(self):
        return self._anuncios
    
    def __str__(self):
        tipos = {'Video': 0, 'Display': 0, 'Social': 0}
        for anuncio in self.anuncios:
            tipos[anuncio.__class__.__name__] += 1
        
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {tipos['Video']} Video, {tipos['Display']} Display, {tipos['Social']} Social"
