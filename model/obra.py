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

    def __init__(self, entorno: str, nombre: str, etapa: Etapa, tipo_obra: TipoObra, area_responsable: Area, descripcion: str, monto_contrato: float, barrio: Barrio, direccion: str,  plazo_meses: int, beneficiarios: str, tipo_contratacion="0", nro_contratacion="0", mano_obra="0", destacada=0, expediente_numero="0", fuente_financiamiento ="0", fecha_inicio="0", fecha_fin_inicial="0", porcentaje_avance = 0, imagenes = 0, empresa="0", licitacion_anio="0"):
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
        return self.__etapa

    @etapa.setter
    def etapa(self, value):
        self.__etapa = value

    @property
    def tipo_obra(self):
        return self.__tipo_obra

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
        return self.__porcentaje_avance

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
        
        if(self.destacada):
            res = 'est?? destacada'
        else:
            res = 'no est?? destacada'

        return "el entorno es: " + str(self.entorno) + "\nEl nombre de la obra es: " + str(self.nombre) + "\nEst?? en la etapa de: " + str(self.etapa) + "\nEl tipo de obra es: " + str(self.tipo_obra) + "\nEl ??rea responsable es: " + str(self.area_responsable) + "\nLa descripci??n es: " + str(self.descripcion) + "\nEl monto del contrato es: " + str(self.monto_contrato) + "\nUbicada en el barrio de: " + str(self.barrio) + "\nLa direcci??n es: " + str(self.direccion) + "\nFecha de inicio: " + str(self.fecha_inicio) + "\nLa fecha prevista para la finalizacion es: " + str(self.fecha_fin_inicial) + "\nEl plazo de meses estimado es de: " + str(self.plazo_meses) + " meses" + "\nEl porcentaje de avance es de: " + str(self.porcentaje_avance) + "%" + "\nLa empresa a cargo es: " + str(self.empresa) + "\nLa licitaci??n es del a??o: " + str(self.licitacion_anio) + "\nEl tipo de contrataci??n es: " + str(self.tipo_contratacion) + "\nEl n??mero de contrataci??n es: " + str(self.nro_contratacion) + "\nLos beneficiarios son: " + str(self.beneficiarios) + "\nLa mano de obra est?? compuesta por: " + str(self.mano_obra) + " empleados" + "\nEl expediente es el n??mero: " + str(self.expediente_numero) + " \n " + str(self.fuente_financiamiento) + "\nLa obra " + res + "\nLas im??genes son: " + str(self.imagenes)

    def iniciar_contratacion(self, tipo: TipoContratacion, nro_contratacion):

        self.tipo_contratacion = tipo
        self.nro_contratacion = nro_contratacion
    
    def adjudicar_obra(self, empresa:Empresa, expediente_numero:str):

        self.empresa = empresa
        self.expediente_numero = expediente_numero
    
    def es_destacada(self):
        while True:
            try:
                es_destacada = int(input("Esta obra es destacada? [1 para s??, 0 para no]: "))
                if es_destacada == 0:
                    return False
                    break
                else:
                    return True
                    break
            except:
                print("ingrese numeros: ")

    
    def iniciar_obra(self,destacada:bool,fecha_inicio:str,fecha_fin_inicial,fuente_financiamiento:FuenteFinanciamiento,mano_obra:int):
        self.destacada = destacada
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_inicial = fecha_fin_inicial
        self.fuente_financiamiento = fuente_financiamiento
        self.mano_obra = mano_obra

    def actualizar_porcentaje_avance(self,porc_incremento:int):
        self.porcentaje_avance =self.porcentaje_avance + porc_incremento
    
    def incrementar_plazo(self,meses:int):
        self.plazo_meses =self.plazo_meses + meses
    
    def agregar_imagenes(self):
        
        self.imagenes = []
        
        cond = True
        while(cond):

            imagen=Imagen(input("ingrese el nombre de la imagen: "))
            self.imagenes.append(imagen.nombre)
            response = input('Desea agregar m??s im??genes? [s/n]: ')
            
            while(response != "n" and response != "N" and response != "s" and response != "S"):
                print('(!) error: Responda s?? o no')
                response = input('Desea agregar m??s im??genes? [s/n]: ')

            # Si el usuario ingresa N cambiamos la condici??n a False y salimos del bucle
            if(response == 'n' or response == 'N'):
                cond = False

    def incrementar_mano_obra(self, cantidad:int):
        self.mano_obra = self.mano_obra + cantidad

    def finalizar_obra(self, obj_etapa_fin):
        self.porcentaje_avance = 100
        self.etapa = obj_etapa_fin

    def rescindir_obra(self, obj_etapa_resc):
        self.etapa = obj_etapa_resc 