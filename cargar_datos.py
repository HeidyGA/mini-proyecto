from modelos import Encuestado, Pregunta, Tema

def cargar_datos_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        lineas = [line.strip() for line in f if line.strip() != '']

    # Variables para almacenar los datos
    encuestados = {}
    temas = []
    tema_actual = None

    i = 0
    while i < len(lineas):
        linea = lineas[i]

        if linea.startswith('K'):
            K = int(linea.split()[1])
        elif linea.startswith('M'):
            M = int(linea.split()[1])
        elif linea.startswith('Nmin'):
            Nmin = int(linea.split()[1])
        elif linea.startswith('Nmax'):
            Nmax = int(linea.split()[1])

        elif linea.startswith('Encuestados:'):
            i += 1
            while i < len(lineas) and not lineas[i].startswith('Tema'):
                id_str, nombre, experticia, opinion = lineas[i].split(',', 3)
                id = int(id_str)
                experticia = int(experticia)
                opinion = int(opinion)
                encuestados[id] = Encuestado(id, nombre.strip(), experticia, opinion)
                i += 1
            i -= 1  # retroceder para procesar el Tema
        elif linea.startswith('Tema'):
            _, nombre_tema = linea.split()
            tema_actual = Tema(nombre_tema)
            temas.append(tema_actual)

        elif linea.startswith('Pregunta'):
            partes = linea.split(':')
            nombre_pregunta = partes[0].split()[1]
            ids = list(map(int, partes[1].strip().split()))
            pregunta = Pregunta(nombre_pregunta)
            for id in ids:
                pregunta.agregar_encuestado(encuestados[id])
            tema_actual.agregar_pregunta(pregunta)

        i += 1

    return temas, list(encuestados.values()), K, M, Nmin, Nmax
