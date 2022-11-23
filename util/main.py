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
            obj_etapa_fin = GestionarModelo.nueva_etapa("Finalizada")
            obj_etapa_resc = GestionarModelo.nueva_etapa("Rescindida")
            obj_dao_etapa = GestionarDAO.crear_objeto_dao("Etapa_DAO")
            GestionarDAO.insertar_registro(obj_dao_etapa, obj_etapa)
            print("Etapa guardada con éxito en la BD")
        except:
            print("Falló la creación de etapa")

        # Creación de 3 obras (punto 2)
        
        i = 0
        obj_obra = 0

        while i < 3:

            # punto 4.b del enunciado, asignando valores
            respuesta_comuna = preguntar_comuna()
            
            
            # preguntar_tipo_contratacion()
            #respuesta_tipo_contratacion=GestionarModelo.nuevo_tipo_contratacion(input("esciba el tipo de contratacion: "))

            # creamos Obra
            try:               
                print(f"se va a crear la obra {i}")
                obj_obra = GestionarModelo.nueva_obra(str(input("ingrese el entorno: ")), str(input("ingrese el nombre de la obra: ")), obj_etapa, preguntar_tipo_obra(), preguntar_area(), str(input("ingrese una descripcion: ")), float(
                    input("ingrese el monto del contrato: ")),preguntar_barrio(respuesta_comuna), str(input("ingrese la direcccion: ")), int(input("ingrese el plazo en meses: ")), str(input("ingrese a los beneficiarios: ")))
                print("Obra 1 creada con éxito ")
                i = i + 1
            except:
                print("Falló la creación de obra")

            # Mostramos los valores iniciales sin modificar

            print()   
            print("######################################")
            print(f"La obra nro {i} con sus valores inciales es: ")
            print("######################################")
            print()
            print(obj_obra)
            print()
            print("######################################")

            # Empezamos a usar los métodos de Obra            

            print("va a ingresar el tipo de contratacion y el num de la misma\n")            
            # a continuacion mostramos los tipos de obra para que el usuario pueda ingresarla por teclado
            

            # inicia contratacion (punto 5)
            obj_obra.iniciar_contratacion(preguntar_tipo_contratacion(), input(
                "ingrese el numero de contratacion: "))

            # vamos a adjudicar la obra a una empresa (punto 6)
            obj_obra.adjudicar_obra(GestionarModelo.nueva_empresa(input("ingrese cuit de la empresa: "),input("ingrese la razon social: ")), input(
                "ingrese el numero de expediente: "))
            
            #vamos a iniciar obra (punto 7)
            obra_destacada = obj_obra.es_destacada()
            obj_obra.iniciar_obra(obra_destacada, input("ingrese la fecha de inicio: "), input("ingrese la fecha de finalizacion: "), preguntar_fuente_financiamiento(), int(input("ingrese la cantidad de mano de obra: ")))
            
            #actualizamos el porcentaje de avance (punto 8)
            obj_obra.actualizar_porcentaje_avance(int(input("ingrese el porcentaje de avance: ")))
            
            #incrementamos el plazo de meses (punto 9)
            obj_obra.incrementar_plazo(int(input("ingrese en cuantos meses incrementara el plazo: ")))
            
            #agregamos imagenes (punto 10)
            obj_obra.agregar_imagenes()

            # incrementamo mano de obra en cantidad de empleados (punto 11)
            obj_obra.incrementar_mano_obra(int(input("Ingrese la cantidad de nuevos empleados que se agregará: "))) 
            
            # Punto 2 de la consiga: crear 2 obras en etapa finalizada y una en rescindida

            if i == 1 or i == 2:
                # finalizamos una obra (etapa finalizada)
                obj_obra.finalizar_obra(obj_etapa_fin)
            elif i == 3:                   
                # rescindimos una obra (etapa rescindida)
                obj_obra.rescindir_obra(obj_etapa_resc)

            print()   
            print("######################################")
            print(f"La obra nro {i} con sus valores modificados es: ")
            print("######################################")
            print()
            print(obj_obra)
            print()
            print("######################################")
        
        print("######################################")
        print("tipos de area")
        obtener_tabla("areas")
        print("######################################")
        print("tipos de obras")
        obtener_tabla("tipos_obras")
        print("######################################")
        
        print("obtener cantidad de obras por etapa")
        obtener_obras_etapa()
        print("######################################")

        print("obtener cantidad de obras por tipo de obra")
        obtener_obras_tipoObra()
        print("######################################")
        
        print("obtener barrios de las comunas 1,2 y 3")
        obtener_barrios_comunas()
        print("######################################")

        print("obtener obras finalizadas de la comuna 1")
        obtener_finalizadas()
        print("######################################")

        print("obtener obras finalizadas con un plazo menor o igual a 24 meses")
        obtener_finalizadas_meses()
        print("######################################")
    
        #obj_dao_obra = GestionarDAO.crear_objeto_dao("Obra_DAO")
         #obj_dao_obra.seleccionar_todos_registros()