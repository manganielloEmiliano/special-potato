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

    @classmethod
    def nueva_obra(cls, entorno: str, nombre: str, etapa: Etapa, tipo_obra: TipoObra, area_responsable: Area, descripcion: str, monto_contrato: float, barrio: Barrio, direccion: str, fecha_inicio, fecha_fin_inicial, plazo_meses: int, porcentaje_avance: float, imagenes: Imagen, empresa: Empresa, licitacion_anio: int, tipo_contratacion: TipoContratacion, nro_contratacion: str, beneficiarios: str, mano_obra: int, destacada: bool, expediente_numero: str, fuente_financiamiento: FuenteFinanciamiento) -> Obra:
        obj = Obra( entorno, nombre, etapa, tipo_obra, area_responsable, descripcion, monto_contrato, barrio, direccion, fecha_inicio, fecha_fin_inicial, plazo_meses, porcentaje_avance, imagenes, empresa, licitacion_anio, tipo_contratacion, nro_contratacion, beneficiarios, mano_obra, destacada, expediente_numero, fuente_financiamiento)
        cls.__listado_obras.append(obj)
        return obj
        

    """@classmethod
    def nueva_obra(cls,nombre,barrio,empresa)->Obra:
        obj=Obra("""

