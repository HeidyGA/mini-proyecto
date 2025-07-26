# segunda_solucion.py

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
            pregunta_id, ids_str = linea.split(":")
            pregunta_id = pregunta_id.split()[1]
            temas[tema_actual][pregunta_id] = {int(id_val): True for id_val in ids_str.strip().split()}
        elif "," in linea:
            id_str, nombre, experticia, opinion = linea.split(",", 3)
            encuestados[int(id_str)] = {
                "nombre": nombre.strip(),
                "experticia": int(experticia),
                "opinion": int(opinion)
            }
    return encuestados, temas

def calcular_promedio(opiniones_vals):
    return round(sum(opiniones_vals) / len(opiniones_vals), 2)

def calcular_mediana(opiniones_vals):
    datos = sorted(opiniones_vals)
    n = len(datos)
    mitad = n // 2
    if n % 2 == 0:
        return round((datos[mitad - 1] + datos[mitad]) / 2, 2)
    else:
        return datos[mitad]

def calcular_moda_y_frecuencia(opiniones_vals):
    if not opiniones_vals:
        return "No única", 0
    frecuencia = {}
    for valor in opiniones_vals:
        frecuencia[valor] = frecuencia.get(valor, 0) + 1
    if not frecuencia:
        return "No única", 0
    max_repe = max(frecuencia.values())
    moda_encontrada = None
    conteo_de_modas = 0
    for k, v in frecuencia.items():
        if v == max_repe:
            moda_encontrada = k
            conteo_de_modas += 1
    if conteo_de_modas == 1:
        return moda_encontrada, max_repe
    else:
        return "No única", 0

def calcular_extremismo(opiniones_vals):
    if not opiniones_vals: return 0.0
    extremos_count = sum(1 for op in opiniones_vals if op == 0 or op == 10)
    return round((extremos_count / len(opiniones_vals)) * 100, 2)

def calcular_consenso(frecuencia_moda, total_opiniones):
    if total_opiniones == 0:
        return 0.0
    return round((frecuencia_moda / total_opiniones) * 100, 2)


def main():
    encuestados, temas = cargar_datos_como_diccionarios("datos_ejemplo.txt")
    print("✅ Datos cargados como diccionarios\n")

    # Esta parte de la salida detallada no cambia
    for tema, preguntas in temas.items():
        print(f"{tema}:")
        for pid, ids_dict in preguntas.items():
            print(f"  Pregunta{pid}: {list(ids_dict.keys())}")
    print("\n📊 Resultados por pregunta:")

    resultados = {}
    for tema, preguntas in temas.items():
        print(f"\n{tema}:")
        for pid, ids_dict in preguntas.items():
            opiniones_dict = {id_enc: encuestados[id_enc]["opinion"] for id_enc in ids_dict.keys()}
            opiniones_vals = list(opiniones_dict.values()) # Convertir a lista para usar en varias funciones
            num_opiniones = len(opiniones_vals)

            prom = calcular_promedio(opiniones_vals)
            mediana = calcular_mediana(opiniones_vals)
            extremismo = calcular_extremismo(opiniones_vals)
            moda, freq_moda = calcular_moda_y_frecuencia(opiniones_vals)
            consenso = calcular_consenso(freq_moda, num_opiniones)

            resultados[(tema, pid)] = {
                "tema": tema,
                "pregunta": pid,
                "promedio": prom,
                "mediana": mediana,
                "moda": moda,
                "extremismo": extremismo,
                "consenso": consenso
            }

            print(f"  Pregunta{pid} ({list(ids_dict.keys())}):")
            print(f"    - Opiniones: {opiniones_vals}")
            print(f"    - Promedio: {prom}")
            print(f"    - Mediana: {mediana}")
            print(f"    - Moda: {moda}")
            print(f"    - Extremismo: {extremismo}%")
            print(f"    - Consenso: {consenso}%")

    # =================================================================
    # CAMBIO PRINCIPAL: Nueva función `mostrar` para el formato exacto
    # =================================================================
    def mostrar(destacado, clave, tipo="max"):
        # Filtra solo los resultados que tienen un valor numérico para la clave
        resultados_validos = [p for p in resultados.values() if isinstance(p[clave], (int, float))]
        if not resultados_validos:
            return # No hacer nada si no hay resultados válidos (ej. todas las modas son "No única")

        # Determina el valor máximo o mínimo
        if tipo == "max":
            valor_objetivo = max(p[clave] for p in resultados_validos)
        else: # tipo == "min"
            valor_objetivo = min(p[clave] for p in resultados_validos)
        
        # Itera sobre todos los resultados válidos y imprime los que coincidan con el valor objetivo
        for p in resultados_validos:
            if p[clave] == valor_objetivo:
                # Se construye la cadena con el formato exacto solicitado
                print(f"📌 {destacado}: Pregunta{p['pregunta']} ({p['tema']}) → {clave.capitalize()} = {p[clave]}")

    print("\n🏅 Preguntas destacadas por métricas globales:\n")

    # --- Llamadas a la nueva función `mostrar` para generar la salida final ---
    mostrar("Mayor promedio", "promedio", "max")
    mostrar("Menor promedio", "promedio", "min")
    mostrar("Mayor mediana", "mediana", "max")
    mostrar("Menor mediana", "mediana", "min")
    mostrar("Mayor moda", "moda", "max")
    mostrar("Menor moda", "moda", "min")
    mostrar("Mayor extremismo", "extremismo", "max")
    mostrar("Mayor consenso", "consenso", "max")


if __name__ == "__main__":
    main()