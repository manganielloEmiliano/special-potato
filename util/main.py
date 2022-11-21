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
        # importar dataset .csv a la base de datos
        archivo_csv = "observatorio-de-obras-urbanas.csv"
        #archivo_csv = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/secretaria-general-y-relaciones-internacionales/ba-obras/observatorio-de-obras-urbanas.csv"
        GestionarDAO.importar_csv(archivo_csv)

        # agregar aquí su código para completar las funcionalidades del TP

        # punto 4.a del enunciado, creamos etapa "proyecto"

        try:
            obj_etapa = GestionarModelo.nueva_etapa("Proyecto")
            obj_dao_etapa = GestionarDAO.crear_objeto_dao("Etapa_DAO")
            GestionarDAO.insertar_registro(obj_dao_etapa, obj_etapa)
            print("Etapa guardada con éxito en la BD")
        except:
            print("Falló la creación de etapa")

        # Creación de 3 obras (punto 2)
        i = 0
        obj_obra1 = 0
        obj_obra2 = 0
        obj_obra3 = 0
        while i < 1:

            # punto 4.b del enunciado, asignando valores
            respuesta_comuna = preguntar_comuna()
            preguntar_barrio()
            respuesta_barrio = GestionarModelo.nuevo_barrio(
                input("escriba el nombre del barrio: "), respuesta_comuna)
            # preguntar_tipo_contratacion()
            #respuesta_tipo_contratacion=GestionarModelo.nuevo_tipo_contratacion(input("esciba el tipo de contratacion: "))

            # creamos Obra
            try:
               
                print("se va a crear la obra 1")
                obj_obra1 = GestionarModelo.nueva_obra(str(input("ingrese el entorno: ")), str(input("ingrese el nombre de la obra: ")), obj_etapa, preguntar_tipo_obra(), preguntar_area(), str(input("ingrese una descripcion: ")), float(
                    input("ingrese el monto del contrato: ")), respuesta_barrio, str(input("ingrese la direcccion: ")), int(input("ingrese el plazo en meses: ")), str(input("ingrese a los beneficiarios: ")))
                print("Obra 1 creada con éxito ")
                i = i +1   
                print(obj_obra1)
            except:
                print("Falló la creación de obra")
               
            print("va a ingresar el tipo de contratacion y el nrm de la misma\n")
            
            # a continuacion mostramos los tipos de obra para que el usuario pueda ingresarla por teclado
            preguntar_tipo_contratacion()
            # inicia contratacion
            obj_obra1.iniciar_contratacion(input("ingrese el tipo de contratacion: "), input(
                "ingrese el numero de contratacion: "))
            # vamos a adjudicar la obra a una empresa
            obj_obra1.adjudicar_obra(GestionarModelo.nueva_empresa(input("ingrese cuit de la empresa: "),input("ingrese la razon social: ")), input(
                "ingrese el numero de expediente: "))
            #vamos a iniciar obra
            obj_obra1.iniciar_obra(bool(input("¿esta obra es destacada?(1/0): ")),input("ingrese la fecha de inicio: "),input("ingrese la fecha de finalizacion: "),preguntar_fuente_financiamiento(),int(input("ingrese la cantidad de mano de obra: ")))
             
            print(obj_obra1)


        # print(obra1)
        # rta_listado_obras = GestionarModelo.__listado_obras
        # print(rta_listado_obras)
