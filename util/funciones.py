from util.gestionar_modelo import GestionarModelo
import sqlite3
import os


def preguntar_tipo_obra():
    print()
    print("Seleccione el tipo de obra que se va a desarrollar: ")
    print()

    opt1 = "Transporte"
    opt2 = "Hidráulica e Infraestructura"
    opt3 = "Arquitectura"
    opt4 = "Escuelas"
    opt5 = "Salud"
    opt6 = "Espacio Público"
    opt7 = "Vivienda Nueva"
    opt8 = "Hidráulica E Infraestructura"
    opt9 = "Vivienda"
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


def preguntar_barrio():
    print("Escriba el nombre del barrio: ")
    print()
    print("""
    "Monserrat"
    "San Nicolás"
    "Puerto Madero"
    "San Telmo"
    "Retiro"
    "Montserrat"
    "Constitución"
    "Constitucion"
    "San telmo"
    "Recoleta"
    "Balvanera"
    "San Cristóbal"
    "Parque Patricios"
    "Nueva Pompeya"
    "Barracas"
    "La Boca"
    "Boca"
    "Boedo"
    "Almagro"
    "Caballito"
    "Flores"
    "Parque Chacabuco"
    "Villa Soldati"
    "Villa Lugano"
    "Villa Riachuelo"
    "Villa 6 - Barrio Cildañez"
    "Parque Avellaneda"
    "Liniers"
    "Mataderos"
    "Villa Luro"
    "Floresta"
    "Versalles"
    "Monte Castro"
    "Villa Real"
    "Vélez Sarsfield"
    "Villa Gral. Mitre"
    "Villa Del Parque"
    "Villa Devoto"
    "Villa del Parque"
    "Villa Santa Rita"
    "Villa Urquiza"
    "Coghlan"
    "Saavedra"
    "Villa Pueyrredon"
    "NuÃ±ez"
    "Nuñez"
    "Belgrano"
    "Colegiales"
    "Palermo"
    "Chacarita"
    "Paternal"
    "Villa Crespo"
    "Parque Chas"
    "Agronomí­a"
    "Villa Ortuzar"    
    """)
    print()


def preguntar_tipo_contratacion():
    print("Escriba el tipo contratacion: ")
    print()
    print("""
    "Licitación Pública"
    "Contratación Directa"
    "Contratacion Menor"
    "Contratación Menor"
    "Licitación Privada"
    "Licitacion Privada"
    "Licitacion Pí¹blica"
    "Licitacion Pública"
    "Decreto 433"
    "Ad Mantenimiento"
    "Anexo contratación mantenimiento"
    "Adicional de Mantenimiento"
    "Licitación"
    "Ad mantenimiento"
    "Licitación Pública Nacional"
    "Licitacion Publica"
    "Obra Publica"
    "LicitaciÃ³n PÃºblica"
    "Contratacion Directa"
    "433/16 (Decr Necesidad y Urgencia)"
    "Licitacion publica"
    "433"
    "CONTRATACIí“N DIRECTA"
    "Decreto 433/16"
    "Licitación Publica"
    "Licitación Pública de Obra Mayor NÂ° 682/SIGAF/2020,"
    "Licitación Pública Internacional"
    "Licitación Privada de Obra Menor"
    "LICITACIÓN PUBLICA"
    "Contratación menor"
    """)
    print()


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


def obtener_tabla(nombre_tabla: str):

    # Crea un objeto de conexión a la base de datos SQLite
    con = sqlite3.connect(os.getcwd()+"/" + "obras_urbanas_caba.db")

    # Con la conexión, crea un objeto cursor
    cur = con.cursor()

    # El resultado de "cursor.execute" puede ser iterado por fila
    # punt 15 a) consultar todas las areas
    for row in cur.execute(f"SELECT * FROM {nombre_tabla}"):
        print(row)

    # No te olvides de cerrar la conexión
    con.close()


def obtener_obras_etapa():

    # Crea un objeto de conexión a la base de datos SQLite
    con = sqlite3.connect(os.getcwd()+"/" + "obras_urbanas_caba.db")

    # Con la conexión, crea un objeto cursor
    cur = con.cursor()

    # El resultado de "cursor.execute" puede ser iterado por fila
    # punt 15 a) consultar todas las areas
    for row in cur.execute("SELECT count(*), etapas.descripcion FROM obras LEFT JOIN etapas ON obras.id_etapa = etapas.id GROUP BY id_etapa"):
        print(row)

    # No te olvides de cerrar la conexión
    con.close()


def obtener_obras_tipoObra():

    # Crea un objeto de conexión a la base de datos SQLite
    con = sqlite3.connect(os.getcwd()+"/" + "obras_urbanas_caba.db")

    # Con la conexión, crea un objeto cursor
    cur = con.cursor()

    # El resultado de "cursor.execute" puede ser iterado por fila
    # punt 15 a) consultar todas las areas
    for row in cur.execute("SELECT count(*), tipos_obras.descripcion FROM obras LEFT JOIN tipos_obras ON obras.id_tipo_obra = tipos_obras.id GROUP BY id_tipo_obra"):

        print(row)

    # No te olvides de cerrar la conexión
    con.close()


def obtener_barrios_comunas():

    # Crea un objeto de conexión a la base de datos SQLite
    con = sqlite3.connect(os.getcwd()+"/" + "obras_urbanas_caba.db")

    # Con la conexión, crea un objeto cursor
    cur = con.cursor()

    # El resultado de "cursor.execute" puede ser iterado por fila
    # punt 15 a) consultar todas las areas
    for row in cur.execute("SELECT nombre, nro_comuna FROM barrios WHERE nro_comuna IN(1,2,3) ORDER BY nro_comuna"):

        print(row)

    # No te olvides de cerrar la conexión
    con.close()


def obtener_finalizadas():

    # Crea un objeto de conexión a la base de datos SQLite
    con = sqlite3.connect(os.getcwd()+"/" + "obras_urbanas_caba.db")

    # Con la conexión, crea un objeto cursor
    cur = con.cursor()

    # El resultado de "cursor.execute" puede ser iterado por fila
    # punt 15 a) consultar todas las areas
    for row in cur.execute("SELECT count(*) FROM obras WHERE id_etapa = 1 AND id_barrio BETWEEN 1 AND 9"):

        print(row)

    # No te olvides de cerrar la conexión
    con.close()

def obtener_finalizadas_meses():

    # Crea un objeto de conexión a la base de datos SQLite
    con = sqlite3.connect(os.getcwd()+"/" + "obras_urbanas_caba.db")

    # Con la conexión, crea un objeto cursor
    cur = con.cursor()

    # El resultado de "cursor.execute" puede ser iterado por fila
    # punt 15 a) consultar todas las areas
    for row in cur.execute("SELECT count(*) FROM obras WHERE id_etapa = 1 AND plazo_meses <= 24"):

        print(row)

    # No te olvides de cerrar la conexión
    con.close()

