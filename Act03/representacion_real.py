import random
import numpy as np
import pandas as pd

df = pd.read_csv('./Lab08/notas_1u.csv')
alumnos = df['Alumno'].tolist()
notas = df['Nota'].tolist()

def crear_cromosoma():
    cromosoma = []
    for i in range(39):
        pesos = [random.random() for _ in range(3)]
        suma = sum(pesos)
        pesos_norm = [p/suma for p in pesos]
        cromosoma.extend(pesos_norm)
    return cromosoma

def decodificar_cromosoma(cromosoma):
    asignaciones = {'A': [], 'B': [], 'C': []}
    examenes = ['A', 'B', 'C']
    
    alumnos_disponibles = list(range(39))
    contadores = {'A': 0, 'B': 0, 'C': 0}
    
    while alumnos_disponibles:
        mejor_alumno = None
        mejor_examen = None
        mejor_valor = -1
        
        for alumno in alumnos_disponibles:
            idx = alumno * 3
            for i, examen in enumerate(examenes):
                if contadores[examen] < 13:
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
    
    for examen in ['A', 'B', 'C']:
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
        idx = i * 3
        if random.random() < 0.5:
            genes = padre1[idx:idx+3]
        else:
            genes = padre2[idx:idx+3]
        
        genes = [g + random.gauss(0, 0.1) for g in genes]
        genes = [max(0, g) for g in genes]
        suma = sum(genes)
        if suma > 0:
            genes = [g/suma for g in genes]
        else:
            genes = [1/3, 1/3, 1/3]
        
        hijo.extend(genes)
    
    return hijo

def mutacion(cromosoma):
    cromosoma_mutado = cromosoma.copy()
    
    for i in range(39):
        if random.random() < 0.1:
            idx = i * 3
            nuevos_pesos = [random.random() for _ in range(3)]
            suma = sum(nuevos_pesos)
            cromosoma_mutado[idx:idx+3] = [p/suma for p in nuevos_pesos]
    
    return cromosoma_mutado

def mutacion_gaussiana(cromosoma, sigma=0.1):
    cromosoma_mutado = []
    for i in range(0, len(cromosoma), 3):
        grupo = np.array(cromosoma[i:i+3])
        ruido = np.random.normal(0, sigma, 3)
        grupo_mutado = grupo + ruido

        grupo_mutado = np.clip(grupo_mutado, 0, None)

        if grupo_mutado.sum() == 0:
            grupo_mutado = np.array([1/3, 1/3, 1/3])
        else:
            grupo_mutado = grupo_mutado / grupo_mutado.sum()

        cromosoma_mutado.extend(grupo_mutado.tolist())
    return cromosoma_mutado

def algoritmo_genetico(generaciones=150, tam_poblacion=100, usar_gaussiana=False, sigma=0.1):
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

            if usar_gaussiana:
                hijo = mutacion_gaussiana(hijo, sigma=sigma)
            else:
                hijo = mutacion(hijo)

            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    return mejor_global_cromosoma, mejor_global_fitness

# PRUEBAS CON VARIOS SIGMA
valores_sigma = [0.01, 0.05, 0.1, 0.2, 0.5]

print("REPRESENTACIÓN REAL")
print("Comparación de operadores de mutación gaussiana con distintos valores de sigma\n")

for sigma in valores_sigma:
    print(f"===== Prueba con sigma = {sigma} =====")
    mejor_solucion, fitness = algoritmo_genetico(usar_gaussiana=True, sigma=sigma)
    asignaciones_finales = decodificar_cromosoma(mejor_solucion)

    print(f"Mejor fitness alcanzado: {fitness:.4f}\nDistribución optimizada:")

    promedios = []
    for examen in ['A', 'B', 'C']:
        indices = asignaciones_finales[examen]
        notas_examen = [notas[i] for i in indices]
        promedio = np.mean(notas_examen)
        varianza = np.var(notas_examen)
        rango = max(notas_examen) - min(notas_examen)
        promedios.append(promedio)
        print(f"  Examen {examen}: {len(indices)} alumnos")
        print(f"    Promedio: {promedio:.2f}, Varianza: {varianza:.2f}, Rango: {rango:.2f}")

    print(f"\n  Desviación estándar entre promedios: {np.std(promedios):.4f}")
    print(f"  Diferencia máxima entre promedios: {max(promedios) - min(promedios):.2f}\n")
