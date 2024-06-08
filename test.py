def superheroes_inteligencia(lista: list):
    tipos_inteligencia = {}
    inteligencia = []

    for vuelta in range(len(lista)):
        inteligencia.append(lista[vuelta]["inteligencia"])

    inteligencia = set(inteligencia)

    for inteligencia in inteligencia:
        tipos_inteligencia[inteligencia] = 0

    for vuelta in range(len(lista)):
        for inteligencia in inteligencia:
            if lista[vuelta]["inteligencia"] == inteligencia:
                tipos_inteligencia[inteligencia] += 1

    return tipos_inteligencia