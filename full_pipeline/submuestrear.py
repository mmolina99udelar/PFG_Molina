# -*- coding: utf-8 -*-

"""Renombrar etiquetas de gestos seleccionados en MyoArm_data"""

import pickle
import matplotlib.pyplot as plt
import numpy as np
import os

# Configuración
bd_to_use = "DB2"

# selecciono archivo de datos
if bd_to_use == "DB2":
    nombre_archivo_datos = "data/DB2/DB2_gestos_seleccionados.pickle"
    nombre_archivo_salida = "data/DB2/DB2_submuestreado.pickle"
elif bd_to_use == "DB3":
    nombre_archivo_datos = "data/DB3/DB3_gestos_seleccionados.pickle"
    nombre_archivo_salida = "data/DB3/DB3_submuestreado.pickle"

else:
    raise ValueError(f"Base de datos no reconocida: {bd_to_use}")

# cargo de datos
if not os.path.exists(nombre_archivo_datos):
    raise FileNotFoundError(f"No se encontró el archivo: {nombre_archivo_datos}")

with open(nombre_archivo_datos, 'rb') as file:
    MyoArm_data = pickle.load(file)

# submuestreo
for sujeto, datos in MyoArm_data.items():
    MyoArm_data[sujeto]['label'] = MyoArm_data[sujeto]['label'][::10]
    MyoArm_data[sujeto]['emg'] = MyoArm_data[sujeto]['emg'][::10]
    
with open(nombre_archivo_salida, "wb") as f:
    pickle.dump(MyoArm_data, f)
    
