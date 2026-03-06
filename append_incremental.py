import os
import glob
import pandas as pd

ruta = r"C:\Users\Administrador\Desktop\Datos\Pipeline"
master_path = os.path.join(ruta, "dataset_unificado.csv")
checkpoint_path = os.path.join(ruta, "_procesados.txt")

# 1) Archivos dataset1 (n).csv detectados
archivos = glob.glob(os.path.join(ruta, "dataset1 (*.csv"))
# Si glob con paréntesis fallara en algún entorno, usar fallback:
if not archivos:
    archivos = glob.glob(os.path.join(ruta, "dataset1 *.csv"))

archivos = [os.path.abspath(a) for a in archivos]
bases_detectadas = sorted([os.path.basename(a) for a in archivos])

print("Detectados:", len(bases_detectadas))
for b in bases_detectadas:
    print(" -", b)

# 2) Cargar checkpoint
procesados = set()
if os.path.exists(checkpoint_path):
    with open(checkpoint_path, "r", encoding="utf-8") as f:
        procesados = set(line.strip() for line in f if line.strip())

print("\nProcesados (checkpoint):", len(procesados))
for p in sorted(procesados):
    print(" *", p)

# 3) Filtrar nuevos por nombre base
nuevos = [a for a in archivos if os.path.basename(a) not in procesados]

def extraer_num(path):
    base = os.path.basename(path)  # dataset1 (8).csv
    return int(base.split("(")[-1].split(")")[0])

# ordenar por número si se puede
try:
    nuevos = sorted(nuevos, key=extraer_num)
except Exception:
    nuevos = sorted(nuevos)

print("\nNuevos archivos:", len(nuevos))
for a in nuevos:
    print(" +", os.path.basename(a))

if not nuevos:
    print("\nNo hay nada nuevo para agregar. Fin.")
    raise SystemExit(0)

# 4) Cargar master (si existe)
if os.path.exists(master_path):
    df_master = pd.read_csv(master_path)
else:
    df_master = pd.DataFrame()

# 5) Leer nuevos y concatenar
dfs_nuevos = [pd.read_csv(a) for a in nuevos]
df_nuevos = pd.concat(dfs_nuevos, ignore_index=True)

df_final = pd.concat([df_master, df_nuevos], ignore_index=True)

# 6) Guardar master
df_final.to_csv(master_path, index=False)
print("\n✔ Master actualizado:", master_path)
print("Filas total:", len(df_final), "Columnas:", len(df_final.columns))

# 7) Actualizar checkpoint (agregar SOLO los nuevos)
with open(checkpoint_path, "a", encoding="utf-8") as f:
    for a in nuevos:
        f.write(os.path.basename(a) + "\n")

print("✔ Checkpoint actualizado:", checkpoint_path)