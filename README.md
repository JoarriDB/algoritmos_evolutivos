# Algoritmos Evolutivos - Semana 10
## Aplicaciones Clásicas: TSP y Asignación de Recursos

### 📋 Información General
- **Universidad:** Universidad Nacional del Santa (UNS)
- **Facultad:** Ingeniería
- **Carrera:** Ingeniería de Sistemas e Informática
- **Curso:** Algoritmos Evolutivos de Aprendizaje
- **Código:** 1411-2278
- **Docente:** Ms. Ing. Johan Max Alexander López Heredia
- **Semestre:** 2025-I
- **Estudiante:** Dueñas Blas, Joseph
- **Código:** 0202114029

### 🎯 Descripción
Esta práctica individual evalúa la comprensión de dos problemas fundamentales de optimización resueltos con algoritmos genéticos:

1. **TSP (Traveling Salesperson Problem):** Encontrar la ruta más corta que visite todas las ciudades exactamente una vez
2. **Asignación de Recursos:** Asignar tareas a recursos minimizando costos o tiempos

### 📚 Contenido de la Práctica

#### Ejercicio 1: Análisis del TSP (4 puntos)
- Identificación de componentes del problema para modelado con algoritmos genéticos
- Representación cromosómica permutacional
- Definición de variables de decisión, función objetivo y restricciones

#### Ejercicio 2: Representación Cromosómica para Asignación (4 puntos)
- Interpretación de cromosomas en problemas de asignación
- Mapeo de trabajos a máquinas
- Validación de representaciones permutacionales

#### Ejercicio 3: Función de Aptitud en TSP (4 puntos)
- Cálculo de distancias totales para rutas específicas
- Evaluación y comparación de fitness entre soluciones
- Aplicación práctica de matriz de distancias

#### Ejercicio 4: Operadores Genéticos en TSP (4 puntos)
- Mutación por intercambio (swap)
- Análisis de limitaciones del cruce simple en problemas permutacionales
- Problemas de validez en representaciones TSP

#### Ejercicio 5: Problema de Asignación Completo (4 puntos)
- Cálculo de tiempos totales para asignaciones específicas
- Optimización de asignación empleado-proyecto
- Evaluación comparativa de soluciones

### 🔑 Conceptos Clave Evaluados

- **Representación Permutacional:** Codificación donde la solución es un ordenamiento específico sin repetición
- **Función de Aptitud:** Evaluación numérica de la calidad de una solución
- **Operadores Genéticos Especializados:** Adaptaciones necesarias para problemas permutacionales
- **Restricciones de Validez:** Condiciones que debe cumplir toda solución válida

### 📊 Resultados Principales

#### TSP - Análisis de Rutas
- **Ruta 1 [A,B,C,D]:** Distancia total = 63 km
- **Ruta 2 [A,D,C,B]:** Distancia total = 63 km
- **Conclusión:** Ambas rutas son igualmente óptimas

#### Asignación de Recursos
- **Asignación [2,3,1]:** Tiempo total = 23 horas
- **Asignación optimizada [1,2,3]:** Tiempo total = 17 horas
- **Mejora:** 26% de reducción en tiempo total

### 🛠️ Metodología
- **Modalidad:** Trabajo individual presencial
- **Duración:** 35 minutos
- **Evaluación:** Sin uso de calculadora o laptop
- **Puntuación:** 0-20 puntos

### 📁 Estructura del Repositorio
```
algoritmos-evolutivos/
├── main
└── s10_lab/
    └── practica_semana10_algoritmos_evolutivos.pdf
```

### 🌿 Información de la Rama
- **Rama principal:** `main`
- **Rama de la práctica:** `s10_lab`
- **Archivo:** `practica_semana10_algoritmos_evolutivos.pdf`

### 🎓 Aprendizajes Clave
1. Los problemas TSP y asignación requieren representación permutacional
2. Los operadores genéticos clásicos deben adaptarse para mantener validez
3. La función de aptitud debe reflejar adecuadamente el objetivo de optimización
4. Las restricciones del problema determinan la validez de las soluciones

### 📝 Notas Importantes
- Esta práctica forma parte de la evaluación continua del curso
- Los problemas clásicos de optimización son base para desafíos reales más complejos
- La comprensión de estos conceptos es fundamental para aplicaciones avanzadas de algoritmos evolutivos