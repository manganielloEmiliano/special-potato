from abc import ABC
from util.gestionar_dao import GestionarDAO
from util.gestionar_modelo import GestionarModelo
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
            obj_etapa=GestionarModelo.nueva_etapa("Proyecto")
            obj_dao_etapa =GestionarDAO.crear_objeto_dao("Etapa_DAO")
            GestionarDAO.insertar_registro(obj_dao_etapa,obj_etapa)
            print("etapa creada")
        except:
            print("fallo la creacion de etapa")
        
        #punto 4.b del enunciado, asignando valores

        #pedimos valor por input 

        print("seleccione el area que va a desarrollar la obra: ")

        opciones_area ="""
        1: Corporación Buenos Aires Sur
        2: Ministerio de Justicia y Seguridad
        3: Secretarí­a de Transporte y Obras Públicas
        4: Ministerio de Desarrollo Humano y Hábitat
        5: Ministerio de Educación
        6: Subsecretarí­a de Gestión Comunal
        7: Ministerio de Salud
        8: Ministerio de Espacio Público e Higiene Urbana
        9: Instituto de la Vivienda
        10: Ministerio de Cultura

        """
      