def parsear_datos(lista: list):
    """Recibe una lista de diccionarios,
    parsea cada dato de esta,
    no devuelve nada

    Args:
        lista (list): La lista a modificar
    """
    for i in range(len(lista)):
        lista[i]["nombre"] = str(lista[i]["nombre"])
        lista[i]["identidad"] = str(lista[i]["identidad"])
        lista[i]["empresa"] = str(lista[i]["empresa"])
        lista[i]["altura"] = float(lista[i]["altura"])
        lista[i]["peso"] = float(lista[i]["peso"])
        lista[i]["genero"] = str(lista[i]["genero"])
        lista[i]["color_ojos"]= str(lista[i]["color_ojos"])
        lista[i]["color_pelo"]= str(lista[i]["color_pelo"])
        lista[i]["fuerza"] = float(lista[i]["fuerza"])
        lista[i]["inteligencia"] = str(lista[i]["inteligencia"])


def mostrar_nombres_superheroes(lista: list)-> None:
    """Recibe una lista, recorre la lista e 
    imprime los nombres de los personajes,
    no devuelve nada

    Args:
        lista (list): La lista a recorrer
    """
    for i in range(len(lista)):
        print(lista[i]["nombre"])


def mostrar_nombres_alturas(lista:list)-> None:
    """Recibe una lista, recorre la lista e 
    imprime los nombres de los personajes y sus alturas,
    no devuelve nada

    Args:
        lista (list): La lista a recorrer
    """
    for i in range(len(lista)):
        print(lista[i]["nombre"], lista[i]["altura"])



def superheroe_altura_max(lista: list):
    """Recibe una lista, la recorre y calcula 
    cual es el superheroe mas alto,
    devuelve su nombre y altura

    Args:
        lista (list): la lista de superheroes

    Returns:
        list: La lista con los resultados
    """
    lista2 = []
    nombre_max = ""
    altura_max = 0
    bandera = True
    for i in range(len(lista)):
        if lista[i]["altura"] > altura_max or bandera:
            bandera = False
            nombre_max = lista[i]["nombre"]
            altura_max = lista[i]["altura"] 

    lista2.append(nombre_max)
    lista2.append(altura_max)


    return lista2

def superheroe_altura_min(lista: list):
    """Recibe una lista, la recorre y calcula 
    cual es el superheroe mas bajo,
    devuelve su nombre y altura

    Args:
        lista (list): la lista de superheroes

    Returns:
        list: La lista con los resultados
    """
    lista2 = []
    nombre_min = ""
    altura_min = 0
    bandera = True
    for i in range(len(lista)):
        if lista[i]["altura"] < altura_min or bandera:
            bandera = False
            nombre_min = lista[i]["nombre"]
            altura_min = lista[i]["altura"] 
    lista2.append(nombre_min)
    lista2.append(altura_min)


    return lista2

def superheroes_altura_promedio(lista: list)-> float:
    """Recibe una lista, suma la altura de los
    superheroes y cuantos hay,
    devuelve la division de esos dos datos

    Args:
        lista (list): La lista con los datos a promediar

    Returns:
        float: La altura promedio
    """
    altura_total = 0
    total_supers = 0
    for i in range(len(lista)):
        altura_total += lista[i]["altura"]
        total_supers += 1


    return altura_total / total_supers


def superheroe_peso_min(lista: list):
    """Recibe una lista, la recorre y calcula 
    cual es el superheroe mas liviano,
    devuelve su nombre y altura

    Args:
        lista (list): la lista de superheroes

    Returns:
        list: Una lista con los resultados
    """
    lista2 = []
    nombre_min = ""
    peso_min = 0
    bandera = True
    for i in range(len(lista)):
        if lista[i]["peso"] < peso_min or bandera:
            bandera = False
            nombre_min = lista[i]["nombre"]
            peso_min = lista[i]["peso"] 

    lista2.append(nombre_min)
    lista2.append(peso_min)


    return lista2

def superheroe_peso_max(lista: list):
    """Recibe una lista, la recorre y calcula 
    cual es el superheroe mas gordo,
    devuelve su nombre y altura

    Args:
        lista (list): la lista de superheroes

    Returns:
        str: El nombre del superheroe
        float: El peso del superheroe
    """
    lista2 = []
    nombre_max = ""
    peso_max = 0
    bandera = True
    for i in range(len(lista)):
        if lista[i]["peso"] > peso_max or bandera:
            bandera = False
            nombre_max = lista[i]["nombre"]
            peso_max = lista[i]["peso"] 

    lista2.append(nombre_max)
    lista2.append(peso_max)


    return lista2


def filtrar_genero_map(lista: list, funcion, genero: str)-> list:
    """Recibe una lista, una funcion y un genero,
    retorna la funcion luego de parle los respectivos parametros
    devuelve una lista

    Args:
        lista (list): La lista de superheroes
        funcion (_type_): la funcion que se quiere usar
        genero (str): El genero que se quiere averiguar

    Returns:
        list: La lista con los resultados de la funcion
    """
    lista_mujeres = []
    lista_hombres = []
    
    for i in range(len(lista)):
        if lista[i]["genero"] == "M":
            lista_hombres.append(lista[i])
        else:
            lista_mujeres.append(lista[i])

    if genero == "M":
        return funcion(lista_hombres)
    else:
        return funcion(lista_mujeres)
    


def superheroes_color_pelos(lista: list):
    """Recibe una lista, crea un diccionario
    con cada tipo de color de pelos y suma,
    devuelve el diccionario

    Args:
        lista (list): La lista de diccionarios

    Returns:
        dict: El diccionario con los resultados
    """
    colores_pelos = {}
    colores_pelo = []

    for vuelta in range(len(lista)):
        colores_pelo.append(lista[vuelta]["color_pelo"])

    colores_pelo = set(colores_pelo)

    for pelo in colores_pelo:
        colores_pelos[pelo] = 0

    for vuelta in range(len(lista)):
        for pelo in colores_pelo:
            if lista[vuelta]["color_pelo"] == pelo:
                colores_pelos[pelo] += 1

    return colores_pelos

def superheroes_color_ojos(lista: list):
    """Recibe una lista, crea un diccionario
    con cada tipo de color de ojo y suma,
    devuelve el diccionario

    Args:
        lista (list): La lista de diccionarios

    Returns:
        dict: El diccionario con los resultados
    """
    colores_ojos = {}
    colores_ojo = []

    for vuelta in range(len(lista)):
        colores_ojo.append(lista[vuelta]["color_ojos"])

    colores_ojo = set(colores_ojo)

    for ojo in colores_ojo:
        colores_ojos[ojo] = 0

    for vuelta in range(len(lista)):
        for ojo in colores_ojo:
            if lista[vuelta]["color_ojos"] == ojo:
                colores_ojos[ojo] += 1

    return colores_ojos

def superheroes_inteligencias(lista: list):
    """Recibe una lista, crea un diccionario
    con cada tipo de inteligencia y suma,
    devuelve el diccionario

    Args:
        lista (list): La lista de diccionarios

    Returns:
        dict: El diccionario con los resultados
    """
    tipos_inteligencia = {}
    inteligencias = []

    for vuelta in range(len(lista)):
        inteligencias.append(lista[vuelta]["inteligencia"])

    inteligencias = set(inteligencias)

    for inteligencia in inteligencias:
        tipos_inteligencia[inteligencia] = 0

    for vuelta in range(len(lista)):
        for inteligencia in inteligencias:
            if lista[vuelta]["inteligencia"] == inteligencia:
                tipos_inteligencia[inteligencia] += 1

    tipos_inteligencia["No tiene"] = tipos_inteligencia[""]  

    del tipos_inteligencia[""]  


    return tipos_inteligencia

def ordenar_superheroes(lista: list, clave: str):
    """Recibe una lista y una clave,
    ordena la lista según la clave,
    no retorna nada

    Args:
        lista (list): La lista a ordenar
        clave (str): El valor a ordenar la lista
    """
    for i in range(len(lista) -1):
        for j in range(i + 1, len(lista)):
            if lista[i][clave] > lista[j][clave]:
                cambiar_superheroes(lista, i, j)


def cambiar_superheroes(lista, i, j):
    """Recibe una lista y dos superheroes,
    cambia de lugar los superheroes,
    no recibe nada
    Args:
        lista (_type_): La lista con los superheroes
        i (_type_): Primer super
        j (_type_): Segundo super
    """
    for clave, valor in lista[i].items():
        aux = lista[i][clave]
        lista[i][clave] = lista[j][clave]
        lista[j][clave] = aux