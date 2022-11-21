from abc import ABC
from model.etapa import Etapa
from model.tipoObra import TipoObra
from model.area import Area
from model.comuna import Comuna
from model.barrio import Barrio
from model.tipoContratacion import TipoContratacion
from model.empresa import Empresa
from model.fuenteFinanciamiento import FuenteFinanciamiento
from model.imagen import Imagen
from model.obra import Obra


class GestionarModelo(ABC):
    __listado_obras = []
    __listado_etapas = []
    __listado_tipos_obras = []
    __listado_areas = []
    __listado_comunas = []
    __listado_barrios = []
    __listado_tipos_contratacion = []
    __listado_empresas = []
    __listado_fuentes_financiamiento = []
    __listado_imagenes = []

    @classmethod
    def nueva_etapa(cls, nombre) -> Etapa:
        obj = Etapa(nombre)
        cls.__listado_etapas.append(obj)
        return obj

    @classmethod
    def nuevo_tipo_obra(cls, descripcion) -> TipoObra:
        obj = TipoObra(descripcion)
        cls.__listado_tipos_obras.append(obj)
        return obj

    @classmethod
    def nueva_area(cls, descripcion: str) -> Area:
        obj = Area(descripcion)
        cls.__listado_areas.append(obj)
        return obj

    @classmethod
    def nueva_comuna(cls, numero: int) -> Comuna:
        obj = Comuna(numero)
        cls.__listado_comunas.append(obj)
        return obj

    @classmethod
    def nuevo_barrio(cls, descripcion: str, comuna: Comuna) -> Barrio:
        obj = Barrio(descripcion, comuna)
        cls.__listado_barrios.append(obj)
        return obj

    @classmethod
    def nuevo_tipo_contratacion(cls, descripcion) -> TipoContratacion:
        obj = TipoContratacion(descripcion)
        cls.__listado_tipos_contratacion.append(obj)
        return obj

    @classmethod
    def nueva_empresa(cls, cuit: str, razon_social: str) -> Empresa:
        obj = Empresa(cuit, razon_social)
        cls.__listado_empresas.append(obj)
        return obj

    @classmethod
    def nueva_fuente_financiamiento(cls, descripcion: str) -> FuenteFinanciamiento:
        obj = FuenteFinanciamiento(descripcion)
        cls.__listado_fuentes_financiamiento.append(obj)
        return obj

    @classmethod
    def nueva_imagen(cls, nombre) -> Imagen:
        obj = Imagen(nombre)
        cls.__listado_imagenes.append(obj)
        return obj

    # def __str__(cls):
    #     return 'El listado de obras es: ' + cls.__listado_obras
    
    @classmethod
    def nueva_obra(cls, entorno: str, nombre: str, etapa: Etapa, tipo_obra: TipoObra, area_responsable: Area, descripcion: str, monto_contrato: float, barrio: Barrio, direccion: str,  plazo_meses: int, beneficiarios: str, ) -> Obra:
        obj = Obra( entorno, nombre, etapa, tipo_obra, area_responsable, descripcion, monto_contrato, barrio, direccion, plazo_meses, beneficiarios)
        cls.__listado_obras.append(obj)
        #print(cls.__listado_obras[0])
        return obj

    @classmethod
    def mostrar_listado_obras(cls):
        i = 0
        while i < len(cls.__listado_obras):
            print(cls.__listado_obras[i])
            i = i + 1

    @classmethod
    def obtener_listado_obras(cls):
        return cls.__listado_obras