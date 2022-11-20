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

        respuesta_area = preguntar_area()
        respuesta_tipo_obra = preguntar_tipo_obra()
        respuesta_comuna = preguntar_comuna()
        preguntar_barrio()
        respuesta_barrio = GestionarModelo.nuevo_barrio(input("Escriba el barrio: "), respuesta_comuna.numero)
        print(respuesta_barrio)