import pandas as pd
import os

ruta = r"C:\Users\Administrador\Desktop\Datos\Pipeline"

archivo_entrada = os.path.join(ruta, "dataset_unificado.csv")
archivo_salida = os.path.join(ruta, "dataset_clean_v2.csv")

df = pd.read_csv(archivo_entrada)

# title = taller
# name = usuario que comenta
# text = comentario
# stars = puntuación
# publishedAtDate = fecha de la reseña

df_clean = pd.DataFrame({
    "stars": df["stars"],
    "comentario": df["text"],
    "usuario": df["name"],
    "taller": df["title"],
    "fecha_reseña": df["publishedAtDate"]
})

# eliminar filas sin lo mínimo necesario
df_clean = df_clean.dropna(subset=["stars", "comentario", "taller", "fecha_reseña"])

# guardar
df_clean.to_csv(archivo_salida, index=False, encoding="utf-8-sig")

print("✔ dataset_clean_v2.csv creado")
print("Filas:", len(df_clean))
print("Columnas:", list(df_clean.columns))