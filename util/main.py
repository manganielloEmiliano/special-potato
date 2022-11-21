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
            print("Etapa guardada con éxito en la BD")
        except:
            print("Falló la creación de etapa")

        # Creación de 3 obras (punto 2)
        i = 0
        while i < 1:

            #punto 4.b del enunciado, asignando valores
            respuesta_comuna = preguntar_comuna()
            preguntar_barrio()
            respuesta_barrio = GestionarModelo.nuevo_barrio(input("escriba el nombre del barrio: "),respuesta_comuna)
            preguntar_tipo_contratacion()
            respuesta_tipo_contratacion=GestionarModelo.nuevo_tipo_contratacion(input("esciba el tipo de contratacion: "))
            
            #creamos Obra
            try:
                obj_obra = GestionarModelo.nueva_obra(str(input("ingrese el entorno: ")),str(input("ingrese el nombre de la obra: ")),obj_etapa,preguntar_tipo_obra(),preguntar_area(),str(input("ingrese una descripcion: ")),float(input("ingrese el monto del contrato: ")),respuesta_barrio,str(input("ingrese la direcccion: ")),int(input("ingrese el plazo en meses: ")),str(input("ingrese a los beneficiarios: ")))                                   
                
                i = i + 1
                GestionarModelo.mostrar_listado_obras()
                print("Obra creada con éxito ")
            except:
                print("Falló la creación de obra")

        GestionarModelo.mostrar_listado_obras()
        #print(obra1)
        # rta_listado_obras = GestionarModelo.__listado_obras
        # print(rta_listado_obras)

