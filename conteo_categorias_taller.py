import pandas as pd

ruta = r"C:\Users\Administrador\Desktop\Datos\Pipeline\dataset_unificado_categorizado_palabras.csv"

df = pd.read_csv(ruta)

# talleres únicos por categoría
resultado = {
    "rapidez": df[df["cat_rapidez"] == 1]["title"].nunique(),
    "calidad": df[df["cat_calidad"] == 1]["title"].nunique(),
    "precio": df[df["cat_precio"] == 1]["title"].nunique(),
    "disponibilidad": df[df["cat_disponibilidad"] == 1]["title"].nunique(),
    "atencion": df[df["cat_atencion"] == 1]["title"].nunique(),
    "confianza": df[df["cat_confianza"] == 1]["title"].nunique()
}

print("\nCantidad de talleres por categoría:\n")

for k,v in resultado.items():
    print(f"{k}: {v} talleres")