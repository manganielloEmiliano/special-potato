from util.gestionar_modelo import GestionarModelo


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
    print("Seleccione la comuna: ")
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
    opr15 = "15"
    opciones = [opt1, opt2, opt3, opt4, opt5, opt6, opt7,
                opt8, opt9, opt10, opt11, opt12, opt13, opt14, opr15]

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
            print('Ingrese un número del 1 al 15. Error: ', e)

    while True:
        if opcion_elegida > 0 and opcion_elegida < 16:
            try:
                obj_comuna = GestionarModelo.nueva_comuna(
                    opciones[opcion_elegida - 1])
                print("la comuna creada con éxito")

            except:
                print("Falló la creación de el objeto comuna")

            break
        else:
            print("Ingrese un número entre 1 y 15")
            opcion_elegida = int(input("Elija el número de opción: "))

    # retornamos el objeto

    return obj_comuna
