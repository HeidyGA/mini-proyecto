import time
import random
import matplotlib.pyplot as plt
from utilidades import (
    ordenar_encuestados_por_opinion_y_experticia,
    calcular_mediana, calcular_moda, calcular_extremismo, calcular_consenso
)
from segunda_solucion import cargar_datos_como_diccionarios, calcular_promedio as calc_prom2, calcular_mediana as med2, calcular_moda as moda2, calcular_extremismo as ext2, calcular_consenso as cons2

# Generar datos aleatorios de expertos y opiniones
def generar_encuestados(n):
    return [type("E",(object,), {"id":i, "opinion":random.randint(0,10), "experticia":random.randint(0,10)})() for i in range(n)]

tamaños = [50, 100, 200, 300, 400, 500]
tiempos1 = []
tiempos2 = []

for n in tamaños:
    encs = generar_encuestados(n)
    opiniones = [e.opinion for e in encs]

    # Tiempo estrategia 1 (OOP)
    t0 = time.perf_counter()
    ordenar_encuestados_por_opinion_y_experticia(encs.copy())
    calcular_mediana(opiniones)
    calcular_moda(opiniones)
    calcular_extremismo(opiniones)
    calcular_consenso(opiniones)
    t1 = time.perf_counter()
    tiempos1.append(t1 - t0)

    # Generar datos para estrategia 2 en estructura de diccionarios
    encs2 = {e.id: {"opinion": e.opinion, "experticia": e.experticia} for e in encs}
    temas2 = {"T": {"1":[e.id for e in encs]}}
    opiniones2 = [encs2[i]["opinion"] for i in temas2["T"]["1"]]

    t0 = time.perf_counter()
    # procesar métricas con estrategia 2
    calc_prom2(opiniones2)
    med2(opiniones2)
    moda2(opiniones2)
    ext2(opiniones2)
    cons2(opiniones2)
    t2 = time.perf_counter()
    tiempos2.append(t2 - t0)

plt.plot(tamaños, tiempos1, label="Estrategia OOP (clases)")
plt.plot(tamaños, tiempos2, label="Estrategia Diccionarios")
plt.title("Comparación de tiempos: clases vs diccionarios")
plt.xlabel("Tamaño entrada (n)")
plt.ylabel("Tiempo ejecución (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("comparativa_estrategias.png")
plt.show()
