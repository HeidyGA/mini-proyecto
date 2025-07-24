
def cargar_datos_como_diccionarios(ruta_archivo):
    encuestados = {}
    temas = {}
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        lineas = [line.strip() for line in f if line.strip()]

    tema_actual = ""
    for linea in lineas:
        if linea.startswith("Encuestados:"):
            continue
        elif linea.startswith("Tema"):
            _, tema_nombre = linea.split()
            temas[tema_nombre] = {}
            tema_actual = tema_nombre
        elif linea.startswith("Pregunta"):
            pregunta_id, ids = linea.split(":")
            pregunta_id = pregunta_id.split()[1]
            temas[tema_actual][pregunta_id] = list(map(int, ids.strip().split()))
        elif "," in linea:
            id_str, nombre, experticia, opinion = linea.split(",", 3)
            encuestados[int(id_str)] = {
                "nombre": nombre.strip(),
                "experticia": int(experticia),
                "opinion": int(opinion)
            }
    return encuestados, temas

def calcular_promedio(opiniones):
    return round(sum(opiniones) / len(opiniones), 2)

def calcular_mediana(opiniones):
    datos = sorted(opiniones)
    n = len(datos)
    mitad = n // 2
    if n % 2 == 0:
        return round((datos[mitad - 1] + datos[mitad]) / 2, 2)
    else:
        return datos[mitad]


def calcular_moda(opiniones):
    frecuencia = {}
    for valor in opiniones:
        frecuencia[valor] = frecuencia.get(valor, 0) + 1
    max_repe = max(frecuencia.values())
    modas = [k for k, v in frecuencia.items() if v == max_repe]
    if len(modas) == 1:
        return modas[0]
    else:
        return "No única"


def calcular_extremismo(opiniones):
    extremos = [op for op in opiniones if op == 0 or op == 10]
    return round((len(extremos) / len(opiniones)) * 100, 2)

def calcular_consenso(opiniones):
    moda = calcular_moda(opiniones)
    if moda == "No única":
        return 0.0
    repeticiones = opiniones.count(moda)
    return round((repeticiones / len(opiniones)) * 100, 2)

def main():
    encuestados, temas = cargar_datos_como_diccionarios("datos_ejemplo.txt")
    print("✅ Datos cargados como diccionarios\n")

    for tema, preguntas in temas.items():
        print(f"{tema}:")
        for pid, ids in preguntas.items():
            print(f"  {pid}: {ids}")
    print("\n📊 Resultados por pregunta:")

    resultados = []
    for tema, preguntas in temas.items():
        print(f"\n{tema}:")
        for pid, ids in preguntas.items():
            opiniones = [encuestados[id]["opinion"] for id in ids]
            prom = calcular_promedio(opiniones)
            mediana = calcular_mediana(opiniones)
            moda = calcular_moda(opiniones)
            extremismo = calcular_extremismo(opiniones)
            consenso = calcular_consenso(opiniones)

            resultados.append({
                "tema": tema,
                "pregunta": pid,
                "promedio": prom,
                "mediana": mediana,
                "moda": moda,
                "extremismo": extremismo,
                "consenso": consenso
            })

            print(f"  Pregunta {pid} ({ids}):")
            print(f"    - Opiniones: {opiniones}")
            print(f"    - Promedio: {prom}")
            print(f"    - Mediana: {mediana}")
            print(f"    - Moda: {moda}")
            print(f"    - Extremismo: {extremismo}%")
            print(f"    - Consenso: {consenso}%")

    # Mostrar preguntas destacadas
    def mostrar(destacado, clave, tipo="max"):
        if tipo == "max":
            valor = max(p[clave] for p in resultados if isinstance(p[clave], (int, float)))
        else:
            valor = min(p[clave] for p in resultados if isinstance(p[clave], (int, float)))
        for p in resultados:
            if p[clave] == valor:
                print(f"📌 {destacado}: Pregunta {p['pregunta']} ({p['tema']}) → {clave} = {valor}")

    print("\n🏅 Preguntas destacadas por métricas globales:\n")
    mostrar("Mayor promedio", "promedio")
    mostrar("Menor promedio", "promedio", "min")
    mostrar("Mayor mediana", "mediana")
    mostrar("Menor mediana", "mediana", "min")
    mostrar("Mayor extremismo", "extremismo")
    mostrar("Mayor consenso", "consenso")

if __name__ == "__main__":
    main()

