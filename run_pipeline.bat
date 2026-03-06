@echo off
cd /d "C:\Users\Administrador\Desktop\Datos\Pipeline"

echo ==== %date% %time% ==== >> pipeline_log.txt

"C:\Users\Administrador\anaconda3\python.exe" "C:\Users\Administrador\Desktop\Datos\Pipeline\append_incremental.py" >> pipeline_log.txt 2>&1
"C:\Users\Administrador\anaconda3\python.exe" "C:\Users\Administrador\Desktop\Datos\Pipeline\load_to_postgres_min.py" >> pipeline_log.txt 2>&1

echo. >> pipeline_log.txt