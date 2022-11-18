from abc import ABC
from model.etapa import Etapa

class GestionarModelo(ABC):
    __listado_etapas = []
    
    @classmethod
    def nueva_etapa(cls,nombre) -> Etapa:
        obj = Etapa(nombre)
        cls.__listado_etapas.append(obj)
        return obj