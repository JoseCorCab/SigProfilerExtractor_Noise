# config.py
import os

BASE = r"C:\Users\quiqu\OneDrive\Escritorio\UNIVERSIDAD\2º MIO\TFM\PYTHON_TFM"

PATHS = {
    "data": os.path.join(BASE, "data"),
    "resultados": os.path.join(BASE, "resultados"),
    "notebooks": os.path.join(BASE, "notebooks"),
}

# Archivos de datos
M_PATH = os.path.join(PATHS["data"], "WGS_PCAWG_96.csv")