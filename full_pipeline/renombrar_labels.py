# -*- coding: utf-8 -*-

"""Renombrar etiquetas de gestos seleccionados en MyoArm_data"""

import pickle
import matplotlib.pyplot as plt
import numpy as np
import os

# Configuración
bd_to_use = "DB2"
gestos_seleccionados = [0, 5, 6, 7, 9, 10, 13, 14, 22, 26, 31]

# Mapeo de gestos seleccionados → nuevos índices consecutivos
nuevos_gestos = np.arange(len(gestos_seleccionados))

# selecciono archivo de datos
if bd_to_use == "DB2":
    nombre_archivo_datos = "data/DB2/DB2_gestos_seleccionados.pickle"
    nombre_archivo_salida = "data/DB2/DB2_gestos_renombrados.pickle"
elif bd_to_use == "DB3":
    nombre_archivo_datos = "data/DB3/DB3_gestos_seleccionados.pickle"
    nombre_archivo_salida = "data/DB3/DB3_gestos_renombrados.pickle"

else:
    raise ValueError(f"Base de datos no reconocida: {bd_to_use}")

# cargo de datos
if not os.path.exists(nombre_archivo_datos):
    raise FileNotFoundError(f"No se encontró el archivo: {nombre_archivo_datos}")

with open(nombre_archivo_datos, 'rb') as file:
    MyoArm_data = pickle.load(file)

# renombro de etiquetas
for sujeto, datos in MyoArm_data.items():
    labels = datos['label']
    for original, nuevo in zip(gestos_seleccionados, nuevos_gestos):
        labels[labels == original] = nuevo
    MyoArm_data[sujeto]['label'] = labels
    
with open(nombre_archivo_salida, "wb") as f:
    pickle.dump(MyoArm_data, f)

# # Gráfico
# plt.figure(figsize=(10, 4))
# plt.plot(MyoArm_data[bd_to_use + '_s2']['label'])
# plt.title("Etiquetas renombradas del sujeto DB3_s2")
# plt.xlabel("Muestras")
# plt.ylabel("Etiqueta")
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('renombrar_label.png', dpi=300)
# plt.show()