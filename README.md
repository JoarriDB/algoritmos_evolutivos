# Algoritmos Evolutivos - Semana 9
## Operadores de Selección y Cruce en Algoritmos Genéticos

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
Esta práctica grupal evalúa la comprensión de operadores fundamentales en algoritmos genéticos para crear nuevas generaciones:

1. **Operadores de Selección:** Métodos para elegir individuos que serán padres de la siguiente generación
2. **Operadores de Cruce:** Técnicas para combinar padres y generar descendencia

### 📚 Contenido de la Práctica

#### Actividad 1: Selección por Torneo (8 puntos)
- Implementación de torneos de tamaño 2 para selección de padres
- Análisis de probabilidades de selección basadas en fitness
- Comparación con métodos de selección elitista
- Evaluación de ventajas para mantener diversidad genética

#### Actividad 2: Cruce PMX para Permutaciones (8 puntos)
- Aplicación del operador PMX (Partially-Mapped Crossover)
- Construcción de mapeos entre segmentos intercambiados
- Generación de descendencia válida en representaciones permutacionales
- Mantenimiento de la integridad de las permutaciones

#### Actividad 3: Análisis Comparativo (4 puntos)
- Comparación entre selección por ruleta vs torneo
- Aplicación práctica al Problema del Viajante (TSP)
- Justificación de elección de operadores según el problema

### 🔑 Conceptos Clave Evaluados

- **Selección por Torneo:** Método robusto que mantiene diversidad genética
- **PMX (Partially-Mapped Crossover):** Operador especializado para permutaciones
- **Presión Selectiva:** Control de la intensidad de selección de individuos aptos
- **Representación Permutacional:** Codificación sin repetición de elementos

### 📊 Resultados Principales

#### Población Inicial (Generación 0)
| Individuo | Fitness | Descripción |
|-----------|---------|-------------|
| A | 85 | Muy buena distribución |
| B | 45 | Distribución regular |
| C | 70 | Buena distribución |
| D | 20 | Distribución deficiente |
| E | 60 | Distribución aceptable |
| F | 90 | Excelente distribución |

#### Resultados de Selección por Torneo
- **Torneo 1:** C vs F → Ganador: F (fitness 90)
- **Torneo 2:** A vs D → Ganador: A (fitness 85)
- **Torneo 3:** B vs E → Ganador: E (fitness 60)

#### Cruce PMX Implementado
- **Padres:** [1,2,3,4,5,6,7,8] y [8,7,6,5,4,3,2,1]
- **Puntos de cruce:** Posiciones 3-6
- **Hijo generado:** [1,7,6,5,4,3,2,8]
- **Mapeo aplicado:** 4↔5, 5↔4, 6↔3, 7↔2

### 📁 Estructura del Repositorio
```
algoritmos-evolutivos/
├── main
├── s9_lab/
│   └── practica_semana9_algoritmos_evolutivos.pdf
└── s10_lab/
    └── practica_semana10_algoritmos_evolutivos.pdf
```

### 🌿 Información de la Rama
- **Rama principal:** `main`
- **Rama Semana 9:** `s9_lab` - Operadores de Selección y Cruce

### 🎓 Aprendizajes Clave
1. La selección por torneo mantiene diversidad genética mejor que métodos elitistas
2. PMX es esencial para problemas con representación permutacional
3. La presión selectiva puede controlarse ajustando el tamaño del torneo
4. Los operadores deben adaptarse al tipo de representación cromosómica
5. El equilibrio entre exploración y explotación es crucial en algoritmos genéticos

### 📈 Aplicaciones Prácticas
- **Problema del Viajante (TSP):** Representación permutacional + PMX
- **Distribución de Estudiantes:** Optimización con múltiples restricciones
- **Asignación de Recursos:** Minimización de costos y tiempos

### 📝 Notas Importantes
- Esta práctica forma parte de la evaluación continua del curso
- Los operadores de selección y cruce son fundamentales para la evolución artificial
- La comprensión de estos conceptos es base para algoritmos genéticos avanzados