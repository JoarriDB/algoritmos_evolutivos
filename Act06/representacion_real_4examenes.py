import random
import numpy as np
import pandas as pd

df = pd.read_csv('./Lab08/notas_1u.csv')
alumnos = df['Alumno'].tolist()
notas = df['Nota'].tolist()

examenes = ['A', 'B', 'C', 'D']
cupo = {'A': 10, 'B': 10, 'C': 10, 'D': 9}

def crear_cromosoma():
    cromosoma = []
    for _ in range(39):
        pesos = [random.random() for _ in range(4)]
        suma = sum(pesos)
        pesos_norm = [p/suma for p in pesos]
        cromosoma.extend(pesos_norm)
    return cromosoma

def decodificar_cromosoma(cromosoma):
    asignaciones = {ex: [] for ex in examenes}
    contadores = {ex: 0 for ex in examenes}
    alumnos_disponibles = list(range(39))

    while alumnos_disponibles:
        mejor_alumno = None
        mejor_examen = None
        mejor_valor = -1

        for alumno in alumnos_disponibles:
            idx = alumno * 4
            for i, examen in enumerate(examenes):
                if contadores[examen] < cupo[examen]:
                    valor = cromosoma[idx + i]
                    if valor > mejor_valor:
                        mejor_valor = valor
                        mejor_alumno = alumno
                        mejor_examen = examen

        if mejor_alumno is not None:
            asignaciones[mejor_examen].append(mejor_alumno)
            contadores[mejor_examen] += 1
            alumnos_disponibles.remove(mejor_alumno)

    return asignaciones

def calcular_fitness(cromosoma):
    asignaciones = decodificar_cromosoma(cromosoma)
    promedios = {}
    varianzas = {}

    for examen in examenes:
        indices = asignaciones[examen]
        notas_examen = [notas[i] for i in indices]
        promedios[examen] = np.mean(notas_examen)
        varianzas[examen] = np.var(notas_examen)

    desv_promedios = np.std(list(promedios.values()))
    promedio_varianzas = np.mean(list(varianzas.values()))
    fitness = -desv_promedios - 0.1 * promedio_varianzas
    return fitness

def cruce(padre1, padre2):
    hijo = []
    for i in range(39):
        idx = i * 4
        if random.random() < 0.5:
            genes = padre1[idx:idx+4]
        else:
            genes = padre2[idx:idx+4]

        genes = [g + random.gauss(0, 0.1) for g in genes]
        genes = [max(0, g) for g in genes]
        suma = sum(genes)
        if suma > 0:
            genes = [g/suma for g in genes]
        else:
            genes = [1/4]*4

        hijo.extend(genes)
    return hijo

def mutacion(cromosoma):
    cromosoma_mutado = cromosoma.copy()
    for i in range(39):
        if random.random() < 0.1:
            idx = i * 4
            nuevos_pesos = [random.random() for _ in range(4)]
            suma = sum(nuevos_pesos)
            cromosoma_mutado[idx:idx+4] = [p/suma for p in nuevos_pesos]
    return cromosoma_mutado

def algoritmo_genetico(generaciones=150, tam_poblacion=100):
    poblacion = [crear_cromosoma() for _ in range(tam_poblacion)]
    mejor_global_fitness = float('-inf')
    mejor_global_cromosoma = None

    for gen in range(generaciones):
        fitness_scores = [(crom, calcular_fitness(crom)) for crom in poblacion]
        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        if fitness_scores[0][1] > mejor_global_fitness:
            mejor_global_fitness = fitness_scores[0][1]
            mejor_global_cromosoma = fitness_scores[0][0].copy()

        nueva_poblacion = []
        elite = int(tam_poblacion * 0.1)
        for i in range(elite):
            nueva_poblacion.append(fitness_scores[i][0])

        while len(nueva_poblacion) < tam_poblacion:
            padre1 = random.choice(poblacion[:tam_poblacion//4])
            padre2 = random.choice(poblacion[:tam_poblacion//4])
            hijo = cruce(padre1, padre2)
            hijo = mutacion(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

        if gen % 30 == 0:
            print(f"Generación {gen}: Mejor fitness = {fitness_scores[0][1]:.4f}")

    return mejor_global_cromosoma

# ----------------------------
# EJECUCIÓN PRINCIPAL
# ----------------------------

print("REPRESENTACIÓN REAL - 4 EXÁMENES")
print("Distribuyendo 39 alumnos en A, B, C, D")
print("Cromosoma: 156 valores reales (39 × 4 pesos normalizados)\n")

mejor_solucion = algoritmo_genetico()
asignaciones_finales = decodificar_cromosoma(mejor_solucion)

print("\nDistribución optimizada:")
for examen in examenes:
    indices = asignaciones_finales[examen]
    notas_examen = [notas[i] for i in indices]
    promedio = np.mean(notas_examen)
    varianza = np.var(notas_examen)
    print(f"Examen {examen}: {len(indices)} alumnos")
    print(f"  Promedio: {promedio:.2f}, Varianza: {varianza:.2f}")
    print(f"  Rango de notas: [{min(notas_examen)} - {max(notas_examen)}]")

print("\nAnálisis de equilibrio:")
promedios = []
for examen in examenes:
    indices = asignaciones_finales[examen]
    notas_examen = [notas[i] for i in indices]
    promedios.append(np.mean(notas_examen))

print(f"Promedios por examen: {', '.join(f'{examen}={prom:.2f}' for examen, prom in zip(examenes, promedios))}")
print(f"Desviación estándar entre promedios: {np.std(promedios):.4f}")
print(f"Diferencia máxima entre promedios: {max(promedios) - min(promedios):.2f}")

# Guardar las notas en CSV para visualización
notas_A = [notas[i] for i in asignaciones_finales['A']]
notas_B = [notas[i] for i in asignaciones_finales['B']]
notas_C = [notas[i] for i in asignaciones_finales['C']]
notas_D = [notas[i] for i in asignaciones_finales['D']]

df_4 = pd.DataFrame({
    'Examen': ['A']*10 + ['B']*10 + ['C']*10 + ['D']*9,
    'Nota': notas_A + notas_B + notas_C + notas_D
})
df_4.to_csv("notas_4examenes.csv", index=False)
