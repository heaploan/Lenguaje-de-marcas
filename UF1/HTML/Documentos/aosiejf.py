modulos = {}
opciones = int(input("***** Expedient Academic *****\n1) Alta de un modulo\n2) Alta nota de una unidad\n3) Ver datos de un modulo\n4) Porcentaje de UF aprobadas\n5) Salir\nIntroduce una opcion:  "))
while opciones != 5:
    if opciones == 1:
        modulo = input("Introduce el nombre del modulo: ")
        if modulo in modulos:
            print("ERROR: El modulo ya esta registrado.")
        else:
            modulos[modulo] = {}
            print("Modulo registrado correctamente")
    if opciones == 2:
        if modulos == {}:
            print("ERROR: No hay ningun modulo registrado")
        else:
            nombreModulo = input("Introduce el modulo al que quieres agregar notas: ")
            if nombreModulo in modulos:
                nombreUf = input("Introduce el nombre de la UF: ")
                if nombreUf in 
    opciones = int(input("***** Expedient Academic *****\n1) Alta de un modulo\n2) Alta nota de una unidad\n3) Ver datos de un modulo\n4) Porcentaje de UF aprobadas\n5) Salir\nIntroduce una opcion:  "))
