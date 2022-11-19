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

        print()
        print("seleccione el area que va a desarrollar la obra: ")
        print()

        opt1 = "Corporación Buenos Aires Sur"
        opt2 = "Ministerio de Justicia y Seguridad"
        opt3 = "Secretarí­a de Transporte y Obras Públicas"
        opt4 = "Ministerio de Desarrollo Humano y Hábitat"
        opt5 = "Ministerio de Educación"
        opt6 = "Subsecretarí­a de Gestión Comunal"
        opt7 = "Ministerio de Salud"
        opt8 = "Ministerio de Espacio Público e Higiene Urbana"
        opt9 = "Instituto de la Vivienda"
        opt10 = "Ministerio de Cultura"

        opciones = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9, opt10]

        #mostramos opciones de area

        i = 1

        for o in opciones:
            print(i, " " , o)
            i = i + 1

        print()
        opcion_elegida = int(input("Elija el número de opción: "))

        #print(opciones[opcion_elegida - 1])

        #creamos objeto del tipo area

        try:
            obj_area=GestionarModelo.nueva_area(opciones[opcion_elegida - 1])
            print("area creada")
        except:
            print("fallo la creacion de area")

        print(obj_area.descripcion)
        
        

        
        
      