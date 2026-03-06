import pandas as pd
import os

ruta = r"C:\Users\Administrador\Desktop\Datos\Pipeline"

archivo_entrada = os.path.join(ruta, "dataset_unificado_categorizado_palabras.csv")
archivo_salida = os.path.join(ruta, "dataset_limpio_final.csv")

df = pd.read_csv(archivo_entrada)

print("Filas originales:", len(df))

# -----------------------
# 1 Normalizar vacíos
# -----------------------
df = df.replace(r'^\s*$', pd.NA, regex=True)

# -----------------------
# 2 Eliminar duplicados
# -----------------------
df = df.drop_duplicates(subset=["title","name","text"])

# -----------------------
# 3 Limpiar texto
# -----------------------
df["text"] = (
    df["text"]
    .astype(str)
    .str.replace("\n"," ")
    .str.replace("\r"," ")
    .str.strip()
)

# -----------------------
# 4 Limpiar nombre taller
# -----------------------
df["title"] = df["title"].astype(str).str.strip()

# -----------------------
# 5 Convertir estrellas
# -----------------------
df["stars"] = pd.to_numeric(df["stars"], errors="coerce")

# -----------------------
# 6 Eliminar reseñas vacías
# -----------------------
df = df.dropna(subset=["text"])

# -----------------------
# 7 Ordenar dataset
# -----------------------
df = df.sort_values(by=["title","stars"], ascending=[True, False])

print("Filas después de limpieza:", len(df))

# -----------------------
# 8 Guardar dataset limpio
# -----------------------
df.to_csv(archivo_salida, index=False, encoding="utf-8-sig")

print("\nDataset limpio guardado en:")
print(archivo_salida)