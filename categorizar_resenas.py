import pandas as pd
import os
import re
import unicodedata

ruta = r"C:\Users\Administrador\Desktop\Datos\Pipeline"
archivo_entrada = os.path.join(ruta, "dataset_unificado.csv")
archivo_salida = os.path.join(ruta, "dataset_unificado_categorizado_palabras.csv")
archivo_resumen = os.path.join(ruta, "resumen_categorias_taller.csv")

df = pd.read_csv(archivo_entrada)

# Nos quedamos con lo importante
df = df[["title", "name", "text", "stars"]].copy()

# Normalizar texto
def normalizar_texto(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).lower()
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("utf-8")
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

df["texto_normalizado"] = df["text"].apply(normalizar_texto)

# Diccionario de categorías
diccionario = {
    "rapidez": [
        "rapido", "rapida", "rapidez", "enseguida", "inmediato", "inmediata",
        "al toque", "veloz"
    ],
    "calidad": [
        "calidad", "excelente", "impecable", "profesional", "perfecto",
        "prolijo", "eficiente", "buen trabajo", "muy bueno"
    ],
    "precio": [
        "precio", "barato", "caro", "accesible", "economico", "economica",
        "presupuesto", "cobran", "costoso"
    ],
    "disponibilidad": [
        "disponibilidad", "turno", "horario", "horarios", "abierto",
        "atienden", "atendieron", "atencion inmediata", "cuando fui"
    ],
    "atencion": [
        "atencion", "amable", "amables", "atentos", "cordial", "trato",
        "buena onda", "simpatico", "respondieron", "asesoraron"
    ],
    "confianza": [
        "confianza", "confiable", "honesto", "honesta", "recomendable",
        "recomendables", "serio", "responsable", "responsables", "seguridad"
    ]
}

# Detectar categorías
for categoria, palabras in diccionario.items():
    df[f"cat_{categoria}"] = df["texto_normalizado"].apply(
        lambda x: 1 if any(p in x for p in palabras) else 0
    )

# Columna con categorías detectadas
def unir_categorias(row):
    cats = []
    for categoria in diccionario.keys():
        if row[f"cat_{categoria}"] == 1:
            cats.append(categoria)
    return ", ".join(cats) if cats else "sin categoria"

df["categorias_detectadas"] = df.apply(unir_categorias, axis=1)

# Guardar dataset enriquecido
df.to_csv(archivo_salida, index=False, encoding="utf-8-sig")

# Resumen por taller
resumen = df.groupby("title").agg(
    total_resenas=("text", "count"),
    rapidez=("cat_rapidez", "sum"),
    calidad=("cat_calidad", "sum"),
    precio=("cat_precio", "sum"),
    disponibilidad=("cat_disponibilidad", "sum"),
    atencion=("cat_atencion", "sum"),
    confianza=("cat_confianza", "sum"),
    promedio_estrellas=("stars", "mean")
).reset_index()

resumen["promedio_estrellas"] = resumen["promedio_estrellas"].round(2)

resumen.to_csv(archivo_resumen, index=False, encoding="utf-8-sig")

print("✔ Archivo generado:", archivo_salida)
print("✔ Resumen generado:", archivo_resumen)

print("\nCantidad total de reseñas por categoría:\n")
for categoria in diccionario.keys():
    print(f"{categoria}: {df[f'cat_{categoria}'].sum()}")

print("\nPrimeras filas categorizadas:\n")
print(df[["title", "name", "text", "categorias_detectadas"]].head(10))