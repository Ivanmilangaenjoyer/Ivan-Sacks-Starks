from data_stark import *
from modulos_stark import *


parsear_datos(lista_personajes)

peso = False
altura_max = False
altura_min = False
altura_promedio = False
menu = True
menu_opciones = ("Que desea hacer?\n"
                "1: Imprimir el nombre de cada superheroe\n"
                "2: Imprimir el nombre y la altura de cada superheroe\n"
                "3: Calcular el superheroe más alto\n"
                "4: Calcular el superheroe más bajo\n"
                "5: Calcular altura promedio de los superheroes\n"
                "6: Calcular el superheroe más y menos gordo\n"
                "7: Informar resultados\n"
                "8: Salir\n")


while menu:
    
    opcion = input(menu_opciones)
    try:
        opcion = int(opcion)
    except:
        raise TypeError("Por favor, ingrese numeros solamente")
    
    while opcion < 1 or opcion > 8:
        raise ValueError("Por favor, ingrese un número del 1 al 8 ")

    match opcion:
        case 1:
            #B
            mostrar_nombres_superheroes(lista_personajes)
        case 2:
            #C
            mostrar_nombres_alturas(lista_personajes)
        case 3:
            #D
            altura_max = True
            lista_altura_max = superheroe_altura_max(lista_personajes)
        case 4: 
            #E
            altura_min = True
            lista_altura_min = superheroe_altura_min(lista_personajes)
        case 5:
            #F
            altura_promedio = True
            alturas_promedio = superheroes_altura_promedio(lista_personajes)
        case 6:
            #H
            peso = True
            lista_peso_max = superheroe_peso_max(lista_personajes)
            lista_peso_min = superheroe_peso_min(lista_personajes)
        case 7:
            if altura_promedio or altura_min or altura_max or peso:
                if altura_promedio:
                    print(f"La altura promedio de los superheroes es: {alturas_promedio} mts")
                if altura_min:
                    print(f"El superheroe más bajo es: {lista_altura_min[0]} ,con una altura de: {lista_altura_min[1]}mts")
                if altura_max:
                    print(f"El superheroe más alto es: {lista_altura_max[0]} ,con una altura de: {lista_altura_max[1]}mts")
                if peso:
                    print(f"El superheroe más gordo es: {lista_peso_max[0]} y pesa {lista_peso_max[1]}kg")
                    print(f"El superheroe más liviano es: {lista_peso_min[0]} y pesa {lista_peso_min[1]}kg")
            else:
                print("No hay resultados que informar")
        case 8:
            menu = False

        