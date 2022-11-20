from model.tipoContratacion import TipoContratacion
from model.etapa import Etapa
from model.tipoObra import TipoObra
from model.barrio import Barrio
from model.area import Area
from model.empresa import Empresa
from model.fuenteFinanciamiento import FuenteFinanciamiento
from model.etapa import Etapa
from model.imagen import Imagen

class Obra():

    def __init__(self, entorno: str, nombre: str, etapa: Etapa, tipo_obra: TipoObra, area_responsable: Area, descripcion: str, monto_contrato: float, barrio: Barrio, direccion: str, fecha_inicio, fecha_fin_inicial, plazo_meses: int, porcentaje_avance: float, imagenes: Imagen, empresa: Empresa, licitacion_anio: int, tipo_contratacion: TipoContratacion, nro_contratacion: str, beneficiarios: str, mano_obra: int, destacada: bool, expediente_numero: str, fuente_financiamiento: FuenteFinanciamiento):
        self.entorno = entorno
        self.nombre = nombre
        self.etapa = etapa
        self.tipo_obra = tipo_obra
        self.area_responsable = area_responsable
        self.descripcion = descripcion
        self.monto_contrato = monto_contrato
        self.barrio = barrio
        self.direccion = direccion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_inicial = fecha_fin_inicial
        self.plazo_meses = plazo_meses
        self.porcentaje_avance = porcentaje_avance
        self.imagenes = imagenes
        self.empresa = empresa
        self.licitacion_anio = licitacion_anio
        self.tipo_contratacion = tipo_contratacion
        self.nro_contratacion = nro_contratacion
        self.beneficiarios = beneficiarios
        self.mano_obra = mano_obra
        self.destacada = destacada
        self.expediente_numero = expediente_numero
        self.fuente_financiamiento = fuente_financiamiento

        print("obra creada")

    @property
    def entorno(self):
        return self.__entorno

    @entorno.setter
    def entorno(self, value):
        self.__entorno = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def etapa(self):
        return self.__nombre

    @etapa.setter
    def etapa(self, value):
        self.__etapa = value

    @property
    def tipo_obra(self):
        return self.__nombre

    @tipo_obra.setter
    def tipo_obra(self, value):
        self.__tipo_obra = value

    @property
    def area_responsable(self):
        return self.__area_responsable

    @area_responsable.setter
    def area_responsable(self, value):
        self.__area_responsable = value

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value

    @property
    def monto_contrato(self):
        return self.__monto_contrato

    @monto_contrato.setter
    def monto_contrato(self, value):
        self.__monto_contrato = value

    @property
    def barrio(self):
        return self.__barrio

    @barrio.setter
    def barrio(self, value):
        self.__barrio = value

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def fecha_fin_inicial(self):
        return self.__fecha_fin_inicial

    @fecha_fin_inicial.setter
    def fecha_fin_inicial(self, value):
        self.__fecha_fin_inicial = value

    @property
    def plazo_meses(self):
        return self.__plazo_meses

    @plazo_meses.setter
    def plazo_meses(self, value):
        self.__plazo_meses = value

    @property
    def porcentaje_avance(self):
        return self.__plazo_meses

    @porcentaje_avance.setter
    def porcentaje_avance(self, value):
        self.__porcentaje_avance = value

    @property
    def imagenes(self):
        return self.__imagenes

    @imagenes.setter
    def imagenes(self, value):
        self.__imagenes = value

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, value):
        self.__empresa = value

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, value):
        self.__empresa = value

    @property
    def licitacion_anio(self):
        return self.__licitacion_anio

    @licitacion_anio.setter
    def licitacion_anio(self, value):
        self.__licitacion_anio = value

    @property
    def tipo_contratacion(self):
        return self.__tipo_contratacion

    @tipo_contratacion.setter
    def tipo_contratacion(self, value):
        self.__tipo_contratacion = value

    @property
    def nro_contratacion(self):
        return self.__nro_contratacion

    @nro_contratacion.setter
    def nro_contratacion(self, value):
        self.__nro_contratacion = value

    @property
    def beneficiarios(self):
        return self.__beneficiarios

    @beneficiarios.setter
    def beneficiarios(self, value):
        self.__beneficiarios = value

    @property
    def mano_obra(self):
        return self.__mano_obra

    @mano_obra.setter
    def mano_obra(self, value):
        self.__mano_obra = value

    @property
    def expediente_numero(self):
        return self.__expediente_numero

    @expediente_numero.setter
    def expediente_numero(self, value):
        self.__expediente_numero = value

    @property
    def destacada(self):
        return self.__destacada

    @destacada.setter
    def destacada(self, value):
        self.__destacada = value

    @property
    def fuente_financiamiento(self):
        return self.__fuente_financiamiento

    @fuente_financiamiento.setter
    def fuente_financiamiento(self, value):
        self.__fuente_financiamiento = value

    def __str__(self) -> str:

        if (self.destacada):
            res = 'está destacada'
        else:
            res = 'no está destada'

        return "el entorno es: " + self.entorno + "\n el nombre de la obra es: " + self.nombre + "\n esta en la etapa de: " + str(self.etapa) + "\n el tipo de obra es: " + str(self.tipo_obra) + "\n el area responsable es:" + str(self.area_responsable) + "\n la descripcion es: "+self.descripcion + "\n el monto del contrato es: " + str(self.monto_contrato) + "\nubicada  en el barrio de: " + str(self.barrio) + "\n la direccion es: " + self.direccion + "\n fecha de inicio" + str(self.fecha_inicio) + "\n la fecha prevista para la finalizacion es: " + str(self.fecha_fin_inicial) + "\n el plazo de meses estimado es de: " + str(self.plazo_meses) + "meses" + "\nel porcentaje de avance es de: " + str(self.porcentaje_avance) + "%" + "\nla empresa acargo es: " + str(self.empresa) + "\nla licitacion es del año: " + str(self.licitacion_anio) + "\nel tipo de contratacion es: " + str(self.tipo_contratacion) + "\nel numero de contratacion es: " + self.nro_contratacion + "\nlos beneficiarios son: " + self.beneficiarios + "\nla mano de obra esta compuesta por: " + str(self.mano_obra) + " empleados" + "\nel expediente es el numero: " + self.expediente_numero + " \n " + str(self.fuente_financiamiento) + "\n La obra " + res

    def iniciar_contratacion(self, tipo: TipoContratacion, nro_contratacion):
        pass
