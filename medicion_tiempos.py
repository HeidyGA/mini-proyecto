import time
import random
import matplotlib.pyplot as plt

from utilidades import (
    ordenar_encuestados_por_opinion_y_experticia,
    calcular_mediana,
    calcular_moda,
    calcular_extremismo,
    calcular_consenso
)

class Encuestado:
    def __init__(self, id, opinion, experticia):
        self.id = id
        self.opinion = opinion
        self.experticia = experticia

# Tamaños de entrada a probar
tamaños = [10, 50, 100, 200, 300, 400, 500]

# Diccionario para guardar tiempos por función
tiempos = {
    "ordenar_encuestados": [],
    "calcular_mediana": [],
    "calcular_moda": [],
    "calcular_extremismo": [],
    "calcular_consenso": []
}

for n in tamaños:
    # Generar lista de encuestados
    encuestados = [Encuestado(i, random.randint(0, 10), random.randint(0, 10)) for i in range(n)]
    opiniones = [e.opinion for e in encuestados]

    # Medir tiempo de ordenamiento
    inicio = time.perf_counter()
    ordenar_encuestados_por_opinion_y_experticia(encuestados.copy())
    fin = time.perf_counter()
    tiempos["ordenar_encuestados"].append(fin - inicio)

    # Medir tiempo de calcular mediana
    inicio = time.perf_counter()
    calcular_mediana(opiniones)
    fin = time.perf_counter()
    tiempos["calcular_mediana"].append(fin - inicio)

    # Medir tiempo de calcular moda
    inicio = time.perf_counter()
    calcular_moda(opiniones)
    fin = time.perf_counter()
    tiempos["calcular_moda"].append(fin - inicio)

    # Medir tiempo de calcular extremismo
    inicio = time.perf_counter()
    calcular_extremismo(opiniones)
    fin = time.perf_counter()
    tiempos["calcular_extremismo"].append(fin - inicio)

    # Medir tiempo de calcular consenso
    inicio = time.perf_counter()
    calcular_consenso(opiniones)
    fin = time.perf_counter()
    tiempos["calcular_consenso"].append(fin - inicio)

# 🔽 GRAFICAR
for key, valores in tiempos.items():
    plt.plot(tamaños, valores, label=key)

plt.title("Tamaño de entrada vs Tiempo de ejecución")
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
