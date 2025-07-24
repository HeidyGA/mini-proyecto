def ordenar_encuestados(encuestados):
    # Orden por opinión DESC, luego experticia DESC
    for i in range(len(encuestados)):
        for j in range(i + 1, len(encuestados)):
            e1, e2 = encuestados[i], encuestados[j]
            if (e1.opinion < e2.opinion) or \
               (e1.opinion == e2.opinion and e1.experticia < e2.experticia):
                encuestados[i], encuestados[j] = encuestados[j], encuestados[i]
    return encuestados

def ordenar_encuestados_por_opinion_y_experticia(lista_encuestados):
    n = len(lista_encuestados)
    for i in range(n):
        for j in range(i + 1, n):
            e1 = lista_encuestados[i]
            e2 = lista_encuestados[j]
            if (e1.opinion < e2.opinion) or (
                e1.opinion == e2.opinion and e1.experticia < e2.experticia
            ):
                lista_encuestados[i], lista_encuestados[j] = lista_encuestados[j], lista_encuestados[i]
    return lista_encuestados

def ordenar_temas_por_criterios(temas):
    n = len(temas)
    for i in range(n):
        for j in range(i + 1, n):
            t1 = temas[i]
            t2 = temas[j]

            prom1 = t1.calcular_promedio_general_opinion()
            prom2 = t2.calcular_promedio_general_opinion()

            if (prom1 < prom2 or
                (prom1 == prom2 and t1.promedio_experticia_general() < t2.promedio_experticia_general()) or
                (prom1 == prom2 and t1.promedio_experticia_general() == t2.promedio_experticia_general() and
                 t1.total_encuestados() < t2.total_encuestados())):
                temas[i], temas[j] = temas[j], temas[i]
    return temas

def ordenar_encuestados_por_experticia_y_id(encuestados):
    n = len(encuestados)
    for i in range(n):
        for j in range(i + 1, n):
            e1 = encuestados[i]
            e2 = encuestados[j]
            if (e1.experticia < e2.experticia) or (
                e1.experticia == e2.experticia and e1.id < e2.id
            ):
                encuestados[i], encuestados[j] = encuestados[j], encuestados[i]
    return encuestados

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def calcular_mediana(lista):
    lista_ordenada = bubble_sort(lista.copy())
    n = len(lista_ordenada)
    if n % 2 == 0:
        return (lista_ordenada[n//2 - 1] + lista_ordenada[n//2]) / 2
    else:
        return lista_ordenada[n//2]

def calcular_moda(lista):
    frecuencias = {}
    for valor in lista:
        frecuencias[valor] = frecuencias.get(valor, 0) + 1
    max_frec = max(frecuencias.values())
    modas = [valor for valor, frec in frecuencias.items() if frec == max_frec]
    return min(modas)  # en caso de empate, se elige el menor

def calcular_extremismo(lista):
    extremos = [op for op in lista if op == 0 or op == 10]
    return round(100 * len(extremos) / len(lista), 2)

def calcular_consenso(lista):
    moda = calcular_moda(lista)
    cantidad = lista.count(moda)
    return round(100 * cantidad / len(lista), 2)

