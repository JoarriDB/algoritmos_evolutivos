# Práctica S08 – Representaciones Cromosómicas en Algoritmos Genéticos

Este repositorio contiene la solución individual a la práctica S08 del curso de **Algoritmos Evolutivos**, basada en el repositorio original:  
[https://github.com/GxJohan/algoritmos_evolutivos/tree/s8_lab]

## 📚 Descripción del Problema

Se implementaron tres representaciones cromosómicas clásicas (Binaria, Real y Permutacional) en algoritmos genéticos para distribuir equitativamente a **39 estudiantes** en **3 exámenes (A, B y C)**, con **13 estudiantes por examen**, buscando equilibrio en el rendimiento académico.

Además, se realizó una extensión del problema original para distribuir a los estudiantes en **4 exámenes (A, B, C y D)**.

---

## 📋 Actividades Realizadas

### Actividad 1: Análisis Comparativo
Se ejecutaron las tres representaciones (binaria, real, permutacional) y se compararon resultados. La permutacional mostró una convergencia más rápida y un equilibrio muy alto desde el inicio. La real tuvo también buenos resultados pero con más variabilidad inicial. La binaria mostró problemas estructurales, ya que no cumplía fácilmente con la restricción exacta de alumnos por grupo.

### Actividad 2: Modificación del Fitness (Binaria)
Se ajustó la función de fitness para penalizar fuertemente la alta varianza interna y premiar la diversidad del rendimiento académico. Tras la modificación, el fitness pasó de valores constantes de -1000 a valores más aceptables (~-2.5), mejorando el equilibrio entre grupos.

### Actividad 3: Mutación Gaussiana (Real)
Se implementó un nuevo operador genético de mutación gaussiana para la representación real, probando distintos valores de sigma (0.01, 0.05, 0.1, 0.2 y 0.5). Se determinó que el valor sigma=0.1 ofrecía el mejor equilibrio entre estabilidad de soluciones y exploración del espacio de búsqueda.

### Actividad 4: Restricción Adicional (Permutacional)
Se añadió la restricción de que los alumnos con nota menor a 11 no podían estar todos en el mismo examen. Tras implementar esta restricción en la función de fitness, se mantuvo un fitness alto (0.2637), mostrando que la representación permutacional gestionaba eficazmente restricciones adicionales.

### Actividad 5: Visualización Avanzada
Se realizaron visualizaciones de la evolución del fitness, histogramas y distribuciones de notas usando matplotlib y seaborn. Esto permitió confirmar visualmente que la permutacional y la real mostraron los mejores equilibrios, mientras que la binaria mejoró tras ajustes, pero seguía siendo inferior.

### Actividad 6: Problema Extendido (4 exámenes)
Se extendió la representación real para manejar cuatro exámenes. El cromosoma pasó a tener 156 valores reales normalizados (4 por alumno). La adaptación logró resultados altamente equilibrados, con promedios casi idénticos entre los cuatro grupos (desviación estándar de apenas 0.0192), mostrando una excelente escalabilidad del método.

---

## 📌 Conclusiones

- **Representación Permutacional:** Ideal para situaciones donde se requiere una distribución estricta, mostró rápida convergencia, gran facilidad para incorporar restricciones adicionales y generó grupos perfectamente equilibrados desde las primeras generaciones.

- **Representación Real:** Muy flexible y efectiva para problemas con variables continuas o probabilísticas, alcanzando gran equilibrio y permitiendo ajustes finos mediante operadores avanzados como la mutación gaussiana.

- **Representación Binaria:** Adecuada solo para problemas sencillos con decisiones binarias discretas. En escenarios de restricciones estrictas mostró limitaciones importantes que requieren modificaciones considerables en la función de fitness.

La elección adecuada de la representación cromosómica, junto con la selección apropiada de operadores genéticos y ajustes en los parámetros del algoritmo, es crucial para alcanzar resultados óptimos de forma eficiente.

---

## 🔗 Referencia Original

Repositorio base proporcionado:  
[https://github.com/GxJohan/algoritmos_evolutivos/tree/s8_lab]

---

## 👨‍💻 Autor

Dueñas Blas, Joseph
Universidad Nacional del Santa  
Curso: Algoritmos Evolutivos – 2024
