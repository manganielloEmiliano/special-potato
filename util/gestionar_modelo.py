from abc import ABC
from model.etapa import Etapa
from model.tipoObra import TipoObra
from model.area import Area
from model.comuna import Comuna
from model.barrio import Barrio
from model.TipoContratacion import TipoContratacion
from model.empresa import Empresa
from model.fuenteFinanciamiento import FuenteFinanciamiento

class GestionarModelo(ABC):
    __listado_obras = []
    __listado_etapas = []
    __listado_tipos_obras=[]
    __listado_areas=[]
    __listado_comunas=[]
    __listado_barrios=[]
    __listado_tipos_contratacion=[]
    __listado_empresas=[]
    __listado_fuentes_financiamiento=[]
    
    @classmethod
    def nueva_etapa(cls,nombre) -> Etapa:
        obj = Etapa(nombre)
        cls.__listado_etapas.append(obj)
        return obj
    
    @classmethod
    def nuevo_tipo_obra(cls,descripcion)->TipoObra:
        obj=TipoObra(descripcion)
        cls.__listado_tipos_obras.append(obj)
        return obj
    
    @classmethod
    def nueva_area(cls,descripcion:str)->Area:
        obj=Area(descripcion)
        cls.__listado_areas.append(obj)
        return obj
    
    @classmethod
    def nueva_comuna(cls,numero:int)->Comuna:
        obj=Comuna(numero)
        cls.__listado_comunas.append(obj)
        return obj
    @classmethod
    def nuevo_barrio(cls,descripcion:str,comuna:Comuna)->Barrio:
        obj=Barrio(descripcion,comuna)
        cls.__listado_barrios.append(obj)
    @classmethod
    def nuevo_tipo_contratacion(cls,descripcion)->TipoContratacion:
        obj=TipoContratacion(descripcion)
        cls.__listado_tipos_contratacion.append(obj)
        return obj
    
    @classmethod
    def nueva_empresa(cls,descripcion:str)->Empresa:
        obj=Empresa(descripcion)
        cls.__listado_empresas.append(obj)
    
    @classmethod
    def nueva_fuente_financiamiento(cls,descripcion:str)->FuenteFinanciamiento:
        obj=FuenteFinanciamiento(descripcion)
        cls.__listado_fuentes_financiamiento.append(obj)
        return obj
