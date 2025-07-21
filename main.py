from cargar_datos import cargar_datos_desde_archivo
from utilidades import (
    calcular_mediana, calcular_moda, calcular_extremismo, calcular_consenso,
    ordenar_encuestados_por_opinion_y_experticia, ordenar_temas_por_criterios,
    ordenar_encuestados_por_experticia_y_id
)


def main():
    # Paso 1: Cargar datos desde archivo
    temas, encuestados, K, M, Nmin, Nmax = cargar_datos_desde_archivo('datos_ejemplo.txt')

    print(f"\n✅ Se cargaron {len(encuestados)} encuestados y {len(temas)} temas.\n")

    for tema in temas:
        print(f"{tema.nombre}:")
        for pregunta in tema.preguntas:
            ids = [e.id for e in pregunta.encuestados]
            print(f"  {pregunta.nombre}: {ids}")

    # Paso 2: Ordenar encuestados dentro de cada pregunta
    print("\n🔽 Ordenando encuestados en cada pregunta...")
    for tema in temas:
        for pregunta in tema.preguntas:
            ordenar_encuestados_por_opinion_y_experticia(pregunta.encuestados)

    # Verificación: mostrar preguntas con encuestados ordenados
    print("\n✅ Preguntas con encuestados ordenados:")
    for tema in temas:
        print(f"\n{tema.nombre}:")
        for pregunta in tema.preguntas:
            ids = [e.id for e in pregunta.encuestados]
            opiniones = [e.opinion for e in pregunta.encuestados]
            print(f"  {pregunta.nombre} (opiniones): {opiniones} → {ids}")

    # Paso 3: Mostrar resultados finales con promedios por tema y pregunta
    print("\n📊 Resultado final con promedios por tema y pregunta:\n")

    temas_ordenados = ordenar_temas_por_criterios(temas)

    for tema in temas_ordenados:
        promedio_tema = tema.calcular_promedio_general_opinion()
        print(f"[{promedio_tema:.2f}] {tema.nombre}:")

        for pregunta in tema.preguntas:
            promedio_pregunta = pregunta.calcular_promedio_opinion()
            ids_ordenados = pregunta.obtener_ids_encuestados()
            print(f"  [{promedio_pregunta:.2f}] {pregunta.nombre}: {tuple(ids_ordenados)}")

    # Paso 4: Métricas estadísticas por pregunta
    print("\n📈 Métricas por pregunta:\n")

    for tema in temas:
        print(f"{tema.nombre}:")
        for pregunta in tema.preguntas:
            opiniones = pregunta.obtener_opiniones()
            mediana = calcular_mediana(opiniones)
            moda = calcular_moda(opiniones)
            extremismo = calcular_extremismo(opiniones)
            consenso = calcular_consenso(opiniones)

            print(f"  {pregunta.nombre}:")
            print(f"    - Mediana: {mediana}")
            print(f"    - Moda: {moda}")
            print(f"    - Extremismo: {extremismo}%")
            print(f"    - Consenso: {consenso}%")

    # Paso 5: Buscar preguntas destacadas por métricas
    print("\n🏅 Preguntas destacadas por métricas globales:\n")

    todas_las_preguntas = []
    for tema in temas:
        for pregunta in tema.preguntas:
            opiniones = pregunta.obtener_opiniones()
            datos = {
                "tema": tema.nombre,
                "pregunta": pregunta.nombre,
                "promedio": pregunta.calcular_promedio_opinion(),
                "mediana": calcular_mediana(opiniones),
                "moda": calcular_moda(opiniones),
                "extremismo": calcular_extremismo(opiniones),
                "consenso": calcular_consenso(opiniones)
            }
            todas_las_preguntas.append(datos)

    # Función auxiliar para mostrar
    def mostrar_pregunta(msg, key, tipo="max"):
        if tipo == "max":
            valor = max(p[key] for p in todas_las_preguntas)
        else:
            valor = min(p[key] for p in todas_las_preguntas)
        preguntas = [p for p in todas_las_preguntas if p[key] == valor]
        for p in preguntas:
            print(f"{msg}: {p['pregunta']} ({p['tema']}) → {key.capitalize()} = {p[key]}")

    mostrar_pregunta("📌 Mayor promedio", "promedio", "max")
    mostrar_pregunta("📌 Menor promedio", "promedio", "min")
    mostrar_pregunta("📌 Mayor mediana", "mediana", "max")
    mostrar_pregunta("📌 Menor mediana", "mediana", "min")
    mostrar_pregunta("📌 Mayor moda", "moda", "max")
    mostrar_pregunta("📌 Menor moda", "moda", "min")
    mostrar_pregunta("📌 Mayor extremismo", "extremismo", "max")
    mostrar_pregunta("📌 Mayor consenso", "consenso", "max")

    # Paso 6: Mostrar lista de encuestados ordenada por experticia y ID
    print("\n🧑‍💻 Lista de encuestados ordenada por experticia (y ID descendente si empatan):\n")

    encuestados_ordenados = ordenar_encuestados_por_experticia_y_id(encuestados)
    lista_ids = [e.id for e in encuestados_ordenados]
    print(f"{lista_ids}")



if __name__ == "__main__":
    main()
