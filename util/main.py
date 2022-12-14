from abc import ABC
from util.gestionar_dao import GestionarDAO
from util.gestionar_modelo import GestionarModelo
from util.funciones import *



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
            GestionarDAO.insertar_registro_general(obj_dao_etapa, obj_etapa)
            print("Etapa guardada con éxito en la BD")
        except:
            print("Falló la creación de etapa")

        # Creación de 3 obras (punto 2)

        i = 0
        obj_obra = 0
        k = 3
        while i < k:

            # punto 4.b del enunciado, asignando valores
            respuesta_comuna = preguntar_comuna()

            # preguntar_tipo_contratacion()
            #respuesta_tipo_contratacion=GestionarModelo.nuevo_tipo_contratacion(input("esciba el tipo de contratacion: "))

            # creamos Obra
            try:
                print(f"se va a crear la obra ")
                obj_obra = GestionarModelo.nueva_obra(str(input("ingrese el entorno: ")), str(input("ingrese el nombre de la obra: ")), obj_etapa, preguntar_tipo_obra(), preguntar_area(), str(input("ingrese una descripcion: ")), float(
                    input("ingrese el monto del contrato: ")), preguntar_barrio(respuesta_comuna), str(input("ingrese la direcccion: ")), int(input("ingrese el plazo en meses: ")), str(input("ingrese a los beneficiarios: ")))
                print(f"Obra {i+1} creada con éxito ")
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
            while True:
                try:
                    obj_obra.iniciar_contratacion(preguntar_tipo_contratacion(), input(
                        "ingrese el numero de contratacion: "))
                    break
                except ValueError as e:
                    print('Ingrese numeros: ', e)

            # vamos a adjudicar la obra a una empresa (punto 6)
            obj_obra.adjudicar_obra(GestionarModelo.nueva_empresa(input("ingrese cuit de la empresa: "), input("ingrese la razon social: ")), input(
                "ingrese el numero de expediente: "))

            # vamos a iniciar obra (punto 7)
            obra_destacada = obj_obra.es_destacada()
            while True:
                try:
                    mano_obra =int(input("ingrese la cantidad de mano de obra: "))
                    break
                except ValueError as e:
                    print('Ingrese numeros: ', e)
            obj_obra.iniciar_obra(obra_destacada, input("ingrese la fecha de inicio: "), input(
                "ingrese la fecha de finalizacion: "), preguntar_fuente_financiamiento(), mano_obra)

            # actualizamos el porcentaje de avance (punto 8)
            while True:
                try:
                    obj_obra.actualizar_porcentaje_avance(
                        int(input("ingrese el porcentaje de avance: ")))
                    break
                except ValueError as e:
                    print('Ingrese numeros: ', e)

            # incrementamos el plazo de meses (punto 9)
            while True:
                try:
                    obj_obra.incrementar_plazo(
                    int(input("ingrese en cuantos meses incrementara el plazo: ")))
                    break
                except ValueError as e:
                    print('Ingrese numeros: ', e)
            # agregamos imagenes (punto 10)
            obj_obra.agregar_imagenes()

            # incrementamo mano de obra en cantidad de empleados (punto 11)
            while True:
                try:
                    obj_obra.incrementar_mano_obra(
                        int(input("Ingrese la cantidad de nuevos empleados que se agregará: ")))
                    break
                except ValueError as e:
                    print('Ingrese numeros: ', e)

            # Punto 2 de la consiga: crear 2 obras en etapa finalizada y una en rescindida

            if i == 0 or i == 1:
                # finalizamos una obra (etapa finalizada)
                obj_obra.finalizar_obra(obj_etapa_fin)
            elif i == 2:
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
            # punto 14 ,persistir las obras en la bd
            listaid = []
            id_et = obtener_id_etapa(obj_obra)
            listaid.append(id_et)
            id_em = obtener_id_empresa(obj_obra)
            listaid.append(id_em)
            id_t_obra = obtener_id_tipoObra(obj_obra)
            listaid.append(id_t_obra)
            id_ar = obtener_id_area(obj_obra)
            listaid.append(id_ar)
            id_ba = obtener_id_barrio(obj_obra)
            listaid.append(id_ba)
            id_t_contra = obtener_id_tipo_contratacion(obj_obra)
            listaid.append(id_t_contra)
            id_ff = obtener_id_ff(obj_obra)
            listaid.append(id_ff)
            obj_dao_obra = GestionarDAO.crear_objeto_dao("Obra_DAO")
            GestionarDAO.insertar_registro(obj_dao_obra, obj_obra, listaid)
            print("la obra se guardo en la base de datos")
            if i >= 3:
                print("######################################")
                continuar = input("si desea continuar ingrese s: ")
                print("######################################")
                if continuar == "s" :
                    k = k + 1

        print("######################################")
        print("tipos de area")
        GestionarDAO.SQL_obtener_tabla("areas")
        print("######################################")
        print("tipos de obras")
        GestionarDAO.SQL_obtener_tabla("tipos_obras")
        print("######################################")

        print("obtener cantidad de obras por etapa")
        GestionarDAO.SQL_obtener_obras_etapa()
        print("######################################")

        print("obtener cantidad de obras por tipo de obra")
        GestionarDAO.SQL_obtener_obras_tipoObra()
        print("######################################")

        print("obtener barrios de las comunas 1,2 y 3")
        GestionarDAO.SQL_obtener_barrios_comunas()
        print("######################################")

        print("obtener obras finalizadas de la comuna 1")
        GestionarDAO.SQL_obtener_finalizadas()
        print("######################################")

        print("obtener obras finalizadas con un plazo menor o igual a 24 meses")
        GestionarDAO.SQL_obtener_finalizadas_meses()
        print("######################################")
