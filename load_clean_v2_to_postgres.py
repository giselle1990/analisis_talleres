import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

RUTA = r"C:\Users\Administrador\Desktop\Datos\Pipeline"
ARCHIVO = os.path.join(RUTA, "dataset_clean_v2.csv")

DB = dict(
    host="localhost",
    port=5432,
    dbname="talleres",
    user="data",
    password="data"
)

def safe_int(x):
    try:
        if pd.isna(x):
            return None
        return int(float(x))
    except Exception:
        return None

def safe_date(x):
    try:
        if pd.isna(x):
            return None
        return pd.to_datetime(x, errors="coerce").date()
    except Exception:
        return None

def to_none(x):
    return None if pd.isna(x) else x

def main():
    if not os.path.exists(ARCHIVO):
        print("No existe dataset_clean_v2.csv")
        return

    df = pd.read_csv(ARCHIVO)

    df["stars"] = df["stars"].apply(safe_int)
    df["comentario"] = df["comentario"].apply(to_none)
    df["usuario"] = df["usuario"].apply(to_none)
    df["taller"] = df["taller"].apply(to_none)
    df["fecha_resena"] = df["fecha_reseña"].apply(safe_date)

    df = df.dropna(subset=["stars", "comentario", "taller", "fecha_resena"])

    rows = list(
        df[["stars", "comentario", "usuario", "taller", "fecha_resena"]]
        .itertuples(index=False, name=None)
    )

    print("Filas a insertar:", len(rows))

    conn = psycopg2.connect(**DB)
    cur = conn.cursor()

    cur.execute("TRUNCATE TABLE raw.reviews_clean_v2;")

    sql = """
    INSERT INTO raw.reviews_clean_v2 (stars, comentario, usuario, taller, fecha_resena)
    VALUES %s;
    """

    execute_values(cur, sql, rows, page_size=2000)
    conn.commit()

    cur.close()
    conn.close()

    print("✔ Carga completada en raw.reviews_clean_v2")

if __name__ == "__main__":
    main()