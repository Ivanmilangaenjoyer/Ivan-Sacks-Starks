from data_stark import *
from modulos_stark import *

# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
# utilizando un menú que permita acceder a cada uno de los puntos por separado.
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia

parsear_datos(lista_personajes)







peso = False
altura_max = False
altura_min = False
altura_max_m = False
altura_promedio = False
altura_max_f = False
menu = True
altura_min_m = False
altura_min_f = False
altura_promedio_f = False
altura_promedio_m = False
color_ojo = False
color_pelo = False
inteligencia = False

menu_opciones = ("Que desea hacer?\n"
                "1: Imprimir el nombre de cada superheroe\n"
                "2: Imprimir el nombre y la altura de cada superheroe\n"
                "3: Calcular el superheroe más alto\n"
                "4: Calcular el superheroe más bajo\n"
                "5: Calcular altura promedio de los superheroes\n"
                "6: Calcular el superheroe más y menos gordo\n"
                "8: Imprimir el nombre de cada superheroe masculino\n"
                "9: Imprimir el nombre de cada superheroe femenino\n"
                "10: Calcular el superheroe más alto masculino\n"
                "11: Calcular el superheroe más alto femenino\n"
                "12: Calcular el superheroe más bajo masculino\n"
                "13: Calcular el superheroe más bajo femenino\n"
                "14: Calcular altura promedio de los superheroes masculinos\n"
                "15: Calcular altura promedio de los superheroes femeninos\n"
                "16: Calcular superheroes con cada tipo de color de ojos\n"
                "17: Calcular superheroes con cada tipo de color de pelo\n"
                "18: Calcular superheroes con cada tipo de inteligencia\n"
                "19: Listar todos los superhéroes agrupados por color de ojos\n"
                "20: Listar todos los superhéroes agrupados por color de pelo\n"
                "21: Listar todos los superhéroes agrupados por inteligencia\n"
                "22: Informar resultados\n"
                "23: Salir\n")

while menu:
    
    opcion = input(menu_opciones)
    try:
        opcion = int(opcion)
    except:
        raise TypeError("Por favor, ingrese numeros solamente")
    
    while opcion < 1 or opcion > 23:
        raise ValueError("Por favor, ingrese un número del 1 al 23 ")

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
            print("Error: 2763242")
        case 8:
        #A 
            filtrar_genero_map(lista_personajes, mostrar_nombres_superheroes, "M")
        case 9:
        #B
            filtrar_genero_map(lista_personajes, mostrar_nombres_superheroes, "F")
        case 10:
            #C
            altura_max_m = True
            lista_altura_max_m = filtrar_genero_map(lista_personajes, superheroe_altura_max, "M")
        case 11:
            #D
            altura_max_f = True
            lista_altura_max_f = filtrar_genero_map(lista_personajes, superheroe_altura_max, "F")       
        case 12:
            #E
            altura_min_m = True
            lista_altura_min_m = filtrar_genero_map(lista_personajes, superheroe_altura_min, "M")
        case 13:
            #F
            altura_min_f = True
            lista_altura_min_f = filtrar_genero_map(lista_personajes, superheroe_altura_min, "F")
        case 14:
            #G
            altura_promedio_m = True
            lista_altura_promedio_m = filtrar_genero_map(lista_personajes, superheroes_altura_promedio, "M")
        case 15:   
            #H
            altura_promedio_f = True
            lista_altura_promedio_f = filtrar_genero_map(lista_personajes, superheroes_altura_promedio, "F")
        case 16:           
            #J
            color_ojo = True
            color_ojos = superheroes_color_pelos(lista_personajes)
        case 17:
            #K
            color_pelo = True
            colores_pelo = superheroes_color_ojos(lista_personajes)
        case 18:
            #L
            inteligencia = True
            inteligencias = superheroes_inteligencias(lista_personajes)
        case 19:
            #M
            ordenar_superheroes(lista_personajes, "color_ojos")
        case 20:
            #N
            ordenar_superheroes(lista_personajes, "color_pelo")
        case 21:
            #O
            ordenar_superheroes(lista_personajes, "inteligencia")
        case 22:
            if (altura_promedio or altura_min or altura_max or peso or altura_max_m or altura_max_f or altura_min_f or 
            altura_min_m or altura_promedio_m or altura_promedio_f or color_ojo or color_pelo or inteligencia):
                if altura_promedio:
                    print(f"La altura promedio de los superheroes es: {alturas_promedio} mts")
                if altura_min:
                    print(f"El superheroe más bajo es: {lista_altura_min[0]} ,con una altura de: {lista_altura_min[1]}mts")
                if altura_max:
                    print(f"El superheroe más alto es: {lista_altura_max[0]} ,con una altura de: {lista_altura_max[1]}mts")
                if peso:
                    print(f"El superheroe más gordo es: {lista_peso_max[0]} y pesa {lista_peso_max[1]}kg")
                    print(f"El superheroe más liviano es: {lista_peso_min[0]} y pesa {lista_peso_min[1]}kg")
                if altura_max_m:
                    print(f"El nombre del superheroe masculino más alto es: {lista_altura_max_m[0]}")
                if altura_max_f:
                    print(f"El nombre del superheroe femenino más alto es: {lista_altura_max_f[0]}")
                if altura_min_m:
                    print(f"El nombre del superheroe masculino más bajo es: {lista_altura_min_m[0]}")
                if altura_min_f:
                    print(f"El nombre del superheroe femenino más bajo es: {lista_altura_min_f[0]}")
                if altura_promedio_m:
                    print(f"La altura promedio de los superheroes masculinos es: {lista_altura_promedio_m}")
                if altura_promedio_f:
                    print(f"La altura promedio de los superheroes femeninos es: {lista_altura_promedio_f}")
                if color_ojo:
                    print(f"Los tipos colores de ojos de cada superheroe son: {color_ojos}")
                if color_pelo:
                    print(f"Los tipos colores de pelo de cada superheroe son: {colores_pelo}")
                if inteligencia:
                    print(f"Los tipos de inteligencias de cada superheroe son: {inteligencias}")
            else:
                print("No hay resultados que informar")
        case 23:
            menu = False