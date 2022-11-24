from util.gestionar_modelo import GestionarModelo
from util.gestionar_dao import GestionarDAO
from dao.tipo_obra_dao import TipoObra_DAO
from dao.etapa_dao import Etapa_DAO
from dao.empresa_dao import Empresa_DAO
from dao.area_dao import Area_DAO
from dao.barrio_dao import Barrio_DAO
from dao.tipo_contratacion_dao import TipoContratacion_DAO
from dao.fuente_financiamiento_dao import FuenteFinanciamiento_DAO
import sqlite3
import os


def preguntar_tipo_obra():
    print()
    print("Seleccione el tipo de obra que se va a desarrollar: ")
    print()

    opt1 = "Espacio Público"
    opt2 = "Arquitectura"
    opt3 = "Escuelas"
    opt4 = "Hidráulica E Infraestructura"
    opt5 = "Salud"
    opt6 = "Hidráulica e Infraestructura"
    opt7 = "Transporte"
    opt8 = "Vivienda"
    opt9 = "Vivienda Nueva"
    opt10 = "Infraestructura"

    opciones = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9, opt10]

    # mostramos opciones de tipo de obra

    i = 1

    for o in opciones:
        print(i, " ", o)
        i = i + 1

    print()

    while True:
        try:
            opcion_elegida = int(input("Elija el número de opción: "))
            break
        except ValueError as e:
            print('Ingrese un número del 1 al 10. Error: ', e)

    while True:
        if opcion_elegida > 0 and opcion_elegida < 11:
            try:
                obj_tipo_obra = GestionarModelo.nuevo_tipo_obra(
                    opciones[opcion_elegida - 1])
                print("Tipo de obra creada con éxito")

            except:
                print("Falló la creación de tipo de obra")

            break
        else:
            print("Ingrese un número entre 1 y 10")
            opcion_elegida = int(input("Elija el número de opción: "))

    # retornamos el objeto

    return obj_tipo_obra


def preguntar_area():
    print()
    print("Seleccione el área que va a desarrollar la obra: ")
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

    # mostramos opciones de area

    i = 1

    for o in opciones:
        print(i, " ", o)
        i = i + 1

    print()

    # creamos objeto del tipo area

    while True:
        try:
            opcion_elegida = int(input("Elija el número de opción: "))
            break
        except ValueError as e:
            print('Ingrese un número del 1 al 10. Error: ', e)

    while True:
        if opcion_elegida > 0 and opcion_elegida < 11:
            try:
                obj_area = GestionarModelo.nueva_area(
                    opciones[opcion_elegida - 1])
                print("Área creada con éxito")

            except:
                print("Falló la creación de área")

            break
        else:
            print("Ingrese un número entre 1 y 10")
            opcion_elegida = int(input("Elija el número de opción: "))

    # retornamos el objeto
    return obj_area


def preguntar_comuna():
    print()
    print("Seleccione la comuna (número entre 1 y 15): ")
    print()

    opt1 = "1"
    opt2 = "2"
    opt3 = "3"
    opt4 = "4"
    opt5 = "5"
    opt6 = "6"
    opt7 = "7"
    opt8 = "8"
    opt9 = "9"
    opt10 = "10"
    opt11 = "11"
    opt12 = "12"
    opt13 = "13"
    opt14 = "14"
    opt15 = "15"
    opciones = [opt1, opt2, opt3, opt4, opt5, opt6, opt7,
                opt8, opt9, opt10, opt11, opt12, opt13, opt14, opt15]

    # mostramos opciones de tipo de obra

    while True:
        try:
            opcion_elegida = int(input("Elija el número de opción: "))
            break
        except ValueError as e:
            print('Ingrese un número del 1 al 15. Error: ', e)

    while True:
        if opcion_elegida > 0 and opcion_elegida < 16:
            try:
                obj_comuna = GestionarModelo.nueva_comuna(
                    opciones[opcion_elegida - 1])
                print(f"la comuna {obj_comuna} fue creada con éxito")

            except:
                print("Falló la creación de el objeto comuna")

            break
        else:
            print("Ingrese un número entre 1 y 15")
            opcion_elegida = int(input("Elija el número de opción: "))

    # retornamos el objeto

    return obj_comuna


def preguntar_barrio(comuna):
    print("Escriba el nombre del barrio: ")
    print()

    opt1 = "Monserrat"
    opt2 = "San Nicolás"
    opt3 = "Puerto Madero"
    opt4 = "San Telmo"
    opt5 = "Retiro"
    opt6 = "Montserrat"
    opt7 = "Constitución"
    opt8 = "Constitucion"
    opt9 = "San telmo"
    opt10 = "Recoleta"
    opt11 = "Balvanera"
    opt12 = "San Cristóbal"
    opt13 = "Parque Patricios"
    opt14 = "Nueva Pompeya"
    opt15 = "Barracas"
    opt16 = "La Boca"
    opt17 = "Boca"
    opt18 = "Boedo"
    opt19 = "Almagro"
    opt20 = "Caballito"
    opt21 = "Flores"
    opt22 = "Parque Chacabuco"
    opt23 = "Villa Soldati"
    opt24 = "Villa Lugano"
    opt25 = "Villa Riachuelo"
    opt26 = "Villa 6 - Barrio Cildañez"
    opt27 = "Parque Avellaneda"
    opt28 = "Liniers"
    opt29 = "Mataderos"
    opt30 = "Villa Luro"
    opt31 = "Floresta"
    opt32 = "Versalles"
    opt33 = "Monte Castro"
    opt34 = "Villa Real"
    opt35 = "Vélez Sarsfield"
    opt36 = "Villa Gral. Mitre"
    opt37 = "Villa Del Parque"
    opt38 = "Villa Devoto"
    opt39 = "Villa del Parque"
    opt40 = "Villa Santa Rita"
    opt41 = "Villa Urquiza"
    opt42 = "Coghlan"
    opt43 = "Saavedra"
    opt44 = "Villa Pueyrredon"
    opt45 = "NuÃ±ez"
    opt46 = "Nuñez"
    opt47 = "Belgrano"
    opt48 = "Colegiales"
    opt49 = "Palermo"
    opt50 = "Chacarita"
    opt51 = "Paternal"
    opt52 = "Villa Crespo"
    opt53 = "Parque Chas"
    opt54 = "Agronomí­a"
    opt55 = "Villa Ortuzar"

    opciones = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9, opt10, opt11, opt12, opt13, opt14, opt15, opt16, opt17, opt18, opt19, opt20, opt21, opt22, opt23, opt24, opt25, opt26, opt27,
                opt28, opt29, opt30, opt31, opt32, opt33, opt34, opt35, opt36, opt37, opt38, opt39, opt40, opt41, opt42, opt43, opt44, opt45, opt46, opt47, opt48, opt49, opt50, opt51, opt52, opt53, opt54]

    # mostramos opciones de barrio

    i = 1

    for o in opciones:
        print(i, " ", o)
        i = i + 1

    print()

    # creamos objeto del tipo barrio

    while True:
        try:
            opcion_elegida = int(input("Elija el número de opción: "))
            break
        except ValueError as e:
            print('Ingrese un número del 1 al 54. Error: ', e)

    while True:
        if opcion_elegida > 0 and opcion_elegida < 55:
            try:
                obj_barrio = GestionarModelo.nuevo_barrio(
                    opciones[opcion_elegida - 1], comuna)
                print("barrio creado con éxito")

            except:
                print("Falló la creación de barrio")

            break
        else:
            print("Ingrese un número entre 1 y 54")
            opcion_elegida = int(input("Elija el número de opción: "))
    return obj_barrio


def preguntar_tipo_contratacion():
    print("Escriba el tipo contratacion: ")
    print()

    opt1 = "Licitación Pública"
    opt2 = "Contratación Directa"
    opt3 = "Contratacion Menor"
    opt4 = "Contratación Menor"
    opt5 = "Licitación Privada"
    opt6 = "Licitacion Privada"
    opt7 = "Licitacion Pí¹blica"
    opt8 = "Licitacion Pública"
    opt9 = "Decreto 433"
    opt10 = "Ad Mantenimiento"
    opt11 = "Anexo contratación mantenimiento"
    opt12 = "Adicional de Mantenimiento"
    opt13 = "Licitación"
    opt14 = "Ad mantenimiento"
    opt15 = "Licitación Pública Nacional"
    opt16 = "Licitacion Publica"
    opt17 = "Obra Publica"
    opt18 = "LicitaciÃ³n PÃºblica"
    opt19 = "Contratacion Directa"
    opt20 = "433/16 (Decr Necesidad y Urgencia)"
    opt21 = "Licitacion publica"
    opt22 = "433"
    opt23 = "CONTRATACIí“N DIRECTA"
    opt24 = "Decreto 433/16"
    opt25 = "Licitación Publica"
    opt26 = "Licitación Pública de Obra Mayor NÂ° 682/SIGAF/2020,"
    opt27 = "Licitación Pública Internacional"
    opt28 = "Licitación Privada de Obra Menor"
    opt29 = "LICITACIÓN PUBLICA"
    opt30 = "Contratación menor"
    opciones = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9, opt10, opt11, opt12, opt13, opt14, opt15,
                opt16, opt17, opt18, opt19, opt20, opt21, opt22, opt23, opt24, opt25, opt26, opt27, opt28, opt29, opt30]
    i = 1

    for o in opciones:
        print(i, " ", o)
        i = i + 1

    print()

    # creamos objeto del tipo contratacion

    while True:
        try:
            opcion_elegida = int(input("Elija el número de opción: "))
            break
        except ValueError as e:
            print('Ingrese un número del 1 al 30. Error: ', e)

    while True:
        if opcion_elegida > 0 and opcion_elegida < 31:
            try:
                obj_tipo_contratacion = GestionarModelo.nuevo_tipo_contratacion(
                    opciones[opcion_elegida - 1])
                print("tipo contratacion creado con éxito")

            except:
                print("Falló la creación de tipo contratacion")

            break
        else:
            print("Ingrese un número entre 1 y 30")
            opcion_elegida = int(input("Elija el número de opción: "))
    return obj_tipo_contratacion


def preguntar_fuente_financiamiento():
    print()
    print("Seleccione la fuente de financiamiento de la obra: ")
    print()

    opt1 = "Nación-GCBA"
    opt2 = "PPI"
    opt3 = "F11"
    opt4 = "Nación"
    opt5 = "Préstamo BIRF 8706-AR"
    opt6 = "Préstamo BID AR-L1260"
    opt7 = "CAF-Nación-GCBA"

    opciones = [opt1, opt2, opt3, opt4, opt5, opt6, opt7]

    # mostramos opciones de area

    i = 1

    for o in opciones:
        print(i, " ", o)
        i = i + 1

    print()

    # creamos objeto del tipo area

    while True:
        try:
            opcion_elegida = int(input("Elija el número de opción: "))
            break
        except ValueError as e:
            print('Ingrese un número del 1 al 7. Error: ', e)

    while True:
        if opcion_elegida > 0 and opcion_elegida < 8:
            try:
                obj_ff = GestionarModelo.nueva_fuente_financiamiento(
                    opciones[opcion_elegida - 1])
                print("FF creada con éxito")

            except:
                print("Falló la creación de FF")

            break
        else:
            print("Ingrese un número entre 1 y 7")
            opcion_elegida = int(input("Elija el número de opción: "))

    # retornamos el objeto
    return obj_ff


def obtener_id_tipoObra(objeto):
    while True:
        obj_dao_tipoObra = TipoObra_DAO()
        desc_tipo_obra = str(objeto.tipo_obra)
        id_tipo_obra = 0
        for tipo in obj_dao_tipoObra.obtener_registros():
            if (tipo[1] == desc_tipo_obra):
                id_tipo_obra = int(tipo[0])
                break
        if id_tipo_obra > 0:
            obj_tipo_obra_model = GestionarModelo.nuevo_tipo_obra(
                desc_tipo_obra)
            break
        else:
            print("El tipo de obra ingresado no existe en la BD")
            break

    return id_tipo_obra


def obtener_id_etapa(objeto):
    while True:
        obj_dao_etapa = Etapa_DAO()
        desc_etapa = str(objeto.etapa)
        id_desc_etapa = 0

        for tipo in obj_dao_etapa.obtener_registros():
            if (tipo[1] == desc_etapa):
                id_desc_etapa = int(tipo[0])
                break
        if id_desc_etapa > 0:
            obj_tipo_obra_model = GestionarModelo.nueva_etapa(
                desc_etapa)
            break
        else:
            print("El tipo de etapa ingresado no existe en la BD")
            break
    return id_desc_etapa


def obtener_id_empresa(objeto):
    while True:
        obj_dao_empresa = Empresa_DAO()
        raz_empresa = str(objeto.empresa.razon_social)
        cuit_empresa =str(objeto.empresa.cuit)
        id_raz_empresa = 0

        for tipo in obj_dao_empresa.obtener_registros():
            if (tipo[2] == raz_empresa):
                id_raz_empresa = int(tipo[0])
                break
        if id_raz_empresa == 0:
          
            obj_empresa = GestionarModelo.nueva_empresa(cuit_empresa,raz_empresa)
            GestionarDAO.insertar_registro_general(obj_dao_empresa,obj_empresa)
            print("la empresa no estaba ingresado en la BD")
            print("empresa ingresada de la base de datos")
        else:
            
            break
    return id_raz_empresa


def obtener_id_area(objeto):
    while True:
        obj_dao_area = Area_DAO()
        desc_area = str(objeto.area_responsable)
        id_tipo_area = 0
        for tipo in obj_dao_area.obtener_registros():
            if (tipo[1] == desc_area):
                id_tipo_area = int(tipo[0])
                break
        if id_tipo_area > 0:
            obj_area_model = GestionarModelo.nueva_area(
                desc_area)
            break
        else:
            print("El tipo de area ingresado no existe en la BD")
            break

    return id_tipo_area


def obtener_id_barrio(objeto):
    while True:
        obj_dao_barrio = Barrio_DAO()
        nombre_barrio = str(objeto.barrio.nombre)
        id_barrio = 0

        for tipo in obj_dao_barrio.obtener_registros():
            if (tipo[1] == nombre_barrio):
                id_barrio = int(tipo[0])
                break
        if id_barrio > 0:
            #obj_tipo_empresa = GestionarModelo.nueva_empresa(raz_empresa)
            break
        else:
            print("El tipo de barrio  ingresado no existe en la BD")
            break
    return id_barrio


def obtener_id_tipo_contratacion(objeto):
    while True:
        obj_dao_tipo_contratacion = TipoContratacion_DAO()
        desc_etapa_tipo_contratacion = str(objeto.tipo_contratacion)
        id_tipo_contratacion = 0

        for tipo in obj_dao_tipo_contratacion.obtener_registros():
            if (tipo[1] == desc_etapa_tipo_contratacion):
                id_tipo_contratacion = int(tipo[0])
                break
        if id_tipo_contratacion > 0:
            obj_tipo_tipo_contratacion = GestionarModelo.nuevo_tipo_contratacion(
                desc_etapa_tipo_contratacion)
            break
        else:
            print("El tipo de contratacion ingresado no existe en la BD")
            break
    return id_tipo_contratacion


def obtener_id_ff(objeto):
    while True:
        obj_dao_ff= FuenteFinanciamiento_DAO()
        desc_ff = str(objeto.fuente_financiamiento.nombre)
        id_tipo_ff = 0

        for tipo in obj_dao_ff.obtener_registros():
            if (tipo[1] == desc_ff):
                id_tipo_ff = int(tipo[0])
                break
        if id_tipo_ff > 0:
            #obj_tipo_ff = GestionarModelo.nueva_fuente_financiamiento(
             #   desc_ff)
            break
        else:
            print("El tipo ff ingresado no existe en la BD")
            break
    return id_tipo_ff
