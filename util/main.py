from abc import ABC
from util.gestionar_dao import GestionarDAO
from util.gestionar_modelo import GestionarModelo
from util.funciones import *
from dao.area_dao import Area_DAO
from dao.etapa_dao import Etapa_DAO
from model.area import Area
from model.barrio import Barrio
from model.comuna import Comuna
from model.empresa import Empresa

class Main(ABC):
    
    @classmethod
    def main(cls):
        #importar dataset .csv a la base de datos
        archivo_csv = "observatorio-de-obras-urbanas.csv"
        #archivo_csv = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/secretaria-general-y-relaciones-internacionales/ba-obras/observatorio-de-obras-urbanas.csv"
        GestionarDAO.importar_csv(archivo_csv)

        #agregar aquí su código para completar las funcionalidades del TP
        
        #punto 4.a del enunciado, creamos etapa "proyecto"

        try:
            obj_etapa = GestionarModelo.nueva_etapa("Proyecto")
            obj_dao_etapa = GestionarDAO.crear_objeto_dao("Etapa_DAO")
            GestionarDAO.insertar_registro(obj_dao_etapa,obj_etapa)
            print("Etapa creada con éxito")
        except:
            print("Falló la creación de etapa")
        
        #punto 4.b del enunciado, asignando valores

        #respuesta_area = preguntar_area()
        #respuesta_tipo_obra = preguntar_tipo_obra()
        respuesta_comuna = preguntar_comuna()
        preguntar_barrio()
        respuesta_barrio = GestionarModelo.nuevo_barrio(input("escriba el nombre del barrio: "),respuesta_comuna)
        preguntar_tipo_contratacion()
        respuesta_tipo_contratacion=GestionarModelo.nuevo_tipo_contratacion(input("esciba el tipo de contratacion: "))
        #print(respuesta_tipo_contratacion)
        #respuesta_empresa=GestionarModelo.nueva_empresa(input("ingese el cuit de la empresa: "),input("ingrese razon social de la empresa: "))
        #respuesta_fuente_financiamiento=preguntar_fuente_financiamiento()
        #respuesta_imagen=GestionarModelo.nueva_imagen(input("ingrese la descripcion de la imagen: "))
        #print(respuesta_imagen)
        obra1=GestionarModelo.nueva_obra(input("ingrese entorno: "),input("ingrese nombre: "),obj_etapa,preguntar_tipo_obra(),preguntar_area(),input("ingrese la descripcion: "),float(input("ingrese el monto del contrato: ")),respuesta_barrio,input("ingrese la direccion: "),input("ingrese la fecha de inicio: "),input("ingrese la fecha de fin: "),int(input("ingrese el plazo de meses: ")),float(input("ingrese el porcentaje de avance: ")),GestionarModelo.nueva_imagen(input("ingrese la descripcion de la imagen: ")),GestionarModelo.nueva_empresa(input("ingese el cuit de la empresa: "),input("ingrese razon social de la empresa: ")),int(input("ingrese el anio de licitacion: ")),respuesta_tipo_contratacion,input("ingrese el numero de contratacion: "),input("ingrese los beneficiarios: "),int(input("ingrese la mano de obra: ")),True,input("\ningrese el numero de expediente: "),preguntar_fuente_financiamiento())
        print(obra1)
        print(GestionarModelo.__listado_obras)

