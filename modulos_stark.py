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
        str: El nombre del superheroe
        float: La altura del superheroe
    """
    nombre_max = ""
    altura_max = 0
    bandera = True
    for i in range(len(lista)):
        if lista[i]["altura"] > altura_max or bandera:
            bandera = False
            nombre_max = lista[i]["nombre"]
            altura_max = lista[i]["altura"] 


    return nombre_max, altura_max

def superheroe_altura_min(lista: list):
    """Recibe una lista, la recorre y calcula 
    cual es el superheroe mas bajo,
    devuelve su nombre y altura

    Args:
        lista (list): la lista de superheroes

    Returns:
        str: El nombre del superheroe
        float: La altura del superheroe
    """
    nombre_min = ""
    altura_min = 0
    bandera = True
    for i in range(len(lista)):
        if lista[i]["altura"] < altura_min or bandera:
            bandera = False
            nombre_min = lista[i]["nombre"]
            altura_min = lista[i]["altura"] 

    return nombre_min, altura_min

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
        str: El nombre del superheroe
        float: El peso del superheroe
    """
    nombre_min = ""
    peso_min = 0
    bandera = True
    for i in range(len(lista)):
        if lista[i]["peso"] < peso_min or bandera:
            bandera = False
            nombre_min = lista[i]["nombre"]
            peso_min = lista[i]["peso"] 

    return nombre_min, peso_min

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
    nombre_max = ""
    peso_max = 0
    bandera = True
    for i in range(len(lista)):
        if lista[i]["peso"] < peso_max or bandera:
            bandera = False
            nombre_max = lista[i]["nombre"]
            peso_max = lista[i]["peso"] 

    return nombre_max, peso_max