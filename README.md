# 🚗 Análisis de Reseñas de Talleres Mecánicos – Pipeline de Datos

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Data Analysis](https://img.shields.io/badge/Data-Analytics-green)
![NLP](https://img.shields.io/badge/Text-Analysis-purple)
![PowerBI](https://img.shields.io/badge/Visualization-PowerBI-yellow)

Proyecto de **análisis de reseñas de Google Maps** aplicado a talleres mecánicos de CABA.

El objetivo es construir un **pipeline de datos completo** que permita:

- recolectar reseñas
- consolidar datasets
- clasificar comentarios por categorías
- limpiar datos
- generar datasets analíticos
- preparar información para dashboards

---

# 📊 Objetivo del proyecto

Analizar la percepción de clientes sobre talleres mecánicos utilizando **análisis de texto sobre reseñas reales**.

Las reseñas se clasifican en categorías como:

- rapidez
- calidad
- precio
- disponibilidad
- atención
- confianza

Esto permite detectar **fortalezas y debilidades de cada taller**.

---

# 🧠 Arquitectura del pipeline

```
Google Maps Reviews
        ↓
Scraping / Export CSV
        ↓
dataset1(n).csv
        ↓
append_incremental.py
        ↓
dataset_unificado.csv
        ↓
categorizar_resenas.py
        ↓
dataset_unificado_categorizado_palabras.csv
        ↓
limpiar_dataset.py
        ↓
dataset_limpio_final.csv
        ↓
Análisis / Power BI
```

---

# 📁 Estructura del proyecto

```
Pipeline/
│
├── dataset1 (1).csv
├── dataset1 (2).csv
├── dataset1 (3).csv
├── dataset1 (4).csv
├── dataset1 (5).csv
│
├── dataset_unificado.csv
├── dataset_unificado_categorizado_palabras.csv
├── dataset_limpio_final.csv
│
├── append_incremental.py
├── categorizar_resenas.py
├── limpiar_dataset.py
│
└── README.md
```

---

# 🗂 Dataset

Cada dataset contiene reseñas extraídas de Google Maps con campos como:

| Campo | Descripción |
|------|-------------|
| title | nombre del taller |
| name | usuario que realizó la reseña |
| text | comentario |
| stars | puntuación |
| reviewsCount | total de reseñas del taller |

---

# 🔗 Paso 1 – Unificación de datasets

Los datasets extraídos se consolidan con:

```
append_incremental.py
```

Este script:

- detecta todos los archivos `dataset1 (n).csv`
- los une en un único dataset
- evita reprocesar datasets ya agregados

### Ejecutar

```
python append_incremental.py
```

Salida:

```
dataset_unificado.csv
```

Este dataset representa la **capa RAW del pipeline**.

---

# 🔎 Paso 2 – Categorización de reseñas

Script:

```
categorizar_resenas.py
```

Utiliza un **diccionario de palabras clave** para detectar temas mencionados por los clientes.

Ejemplo:

| Categoría | Palabras clave |
|-----------|---------------|
| rapidez | rápido, enseguida, inmediato |
| calidad | excelente, profesional, impecable |
| precio | caro, barato, accesible |
| disponibilidad | turno, horario, abierto |
| atención | amable, atentos |
| confianza | confiable, recomendable |

Cada reseña puede pertenecer a **una o múltiples categorías**.

### Ejecutar

```
python categorizar_resenas.py
```

Salida:

```
dataset_unificado_categorizado_palabras.csv
```

Columnas agregadas:

```
cat_rapidez
cat_calidad
cat_precio
cat_disponibilidad
cat_atencion
cat_confianza
categorias_detectadas
```

---

# 🧹 Paso 3 – Limpieza de datos

Script:

```
limpiar_dataset.py
```

Procesos realizados:

- eliminación de duplicados
- normalización de valores vacíos
- limpieza de texto
- estandarización de nombres de talleres
- conversión de estrellas a formato numérico
- eliminación de reseñas vacías

### Ejecutar

```
python limpiar_dataset.py
```

Salida:

```
dataset_limpio_final.csv
```

Este es el **dataset final listo para análisis**.

---

# 📈 Ejemplos de análisis posibles

Con el dataset final se pueden construir métricas como:

### Reputación por taller

- promedio de estrellas
- volumen de reseñas
- distribución de categorías

### Percepción de clientes

- talleres asociados a rapidez
- talleres con mayor confianza
- talleres criticados por precio
- talleres con mejor atención

### Métricas adicionales

- porcentaje de reseñas positivas
- ranking de talleres
- análisis de categorías por taller

---

# 📊 Visualización

El dataset final puede ser utilizado en herramientas como:

- Power BI
- Tableau
- Python (Matplotlib / Seaborn)

Ejemplos de visualizaciones:

- ranking de talleres por reputación
- distribución de categorías
- percepción de clientes
- análisis de sentimiento

---

# 🔄 Cómo agregar nuevos datasets

Cuando se recolectan nuevas reseñas:

1️⃣ Guardar el archivo como:

```
dataset1 (n).csv
```

Ejemplo:

```
dataset1 (11).csv
```

2️⃣ Ejecutar nuevamente el pipeline:

```
python append_incremental.py
python categorizar_resenas.py
python limpiar_dataset.py
```

Esto actualizará automáticamente:

```
dataset_unificado.csv
dataset_unificado_categorizado_palabras.csv
dataset_limpio_final.csv
```

---

# 🛠 Tecnologías utilizadas

- Python
- Pandas
- Regex
- NLP básico
- Google Maps
- Apify
- Power BI

---

# 💡 Posibles mejoras

- análisis de sentimiento automático
- detección de temas emergentes
- clustering de talleres por reputación
- integración con PostgreSQL
- pipeline automatizado

---

# 👩‍💻 Autor

Proyecto desarrollado como práctica de **Data Analytics aplicado a análisis de reseñas de clientes**.