class Encuestado:
    def __init__(self, id, nombre, experticia, opinion):
        self.id = id
        self.nombre = nombre
        self.experticia = experticia
        self.opinion = opinion

class Pregunta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.encuestados = []

    def agregar_encuestado(self, encuestado):
        self.encuestados.append(encuestado)

    def calcular_promedio_opinion(self):
        total = sum(e.opinion for e in self.encuestados)
        return round(total / len(self.encuestados), 2)

    def calcular_promedio_experticia(self):
        total = sum(e.experticia for e in self.encuestados)
        return round(total / len(self.encuestados), 2)

    def obtener_ids_encuestados(self):
        return [e.id for e in self.encuestados]
    
    def obtener_opiniones(self):
        return [e.opinion for e in self.encuestados]


# Mediana, moda, extremismo, consenso

class Tema:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def calcular_promedio_general_opinion(self):
        total = sum(p.calcular_promedio_opinion() for p in self.preguntas)
        return round(total / len(self.preguntas), 2)

    def promedio_experticia_general(self):
        total = sum(p.calcular_promedio_experticia() for p in self.preguntas)
        return round(total / len(self.preguntas), 2)

    def total_encuestados(self):
        return sum(len(p.encuestados) for p in self.preguntas)
