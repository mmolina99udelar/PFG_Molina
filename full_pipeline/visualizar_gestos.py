# -*- coding: utf-8 -*-

"""Importo librerías"""

import pickle
import matplotlib.pyplot as plt
import numpy as np

# ===== CONFIGURACIÓN =====
bd_to_use = "DB3"
gestos_seleccionados = [0, 5, 6, 7, 9, 10, 13, 14, 22, 26, 31]

# ===== ARCHIVO DE DATOS =====
if bd_to_use == "DB2":
    nombre_archivo_datos = "data/DB2/data_DB2_concatenado.pickle"
elif bd_to_use == "DB3":
    nombre_archivo_datos = "data/DB3/data_DB3_concatenado.pickle"

# ===== CARGO LOS DATOS =====
with open(nombre_archivo_datos, 'rb') as f:
    MyoArm_data = pickle.load(f)

# ===== ELIJO SUJETO Y GESTO =====
sujeto = 3
sujeto = str(bd_to_use) + "_s" + str(sujeto) # elijo el sujeto
gesto = gestos_seleccionados[1]  # elijo el gesto

# ===== PARÁMETROS =====
margen = 1000  # muestras antes y después para mostrar
canal = 3      # canal de EMG a graficar

# ===== EXTRACCIÓN =====
emg = MyoArm_data[sujeto]['emg']
label = MyoArm_data[sujeto]['label']

# Aplano label si tiene forma (N, 1)
if label.ndim > 1:
    label = label.squeeze()

# Encuentro los índices donde aparece el gesto
indices_gesto = np.where(label == gesto)[0]

if len(indices_gesto) == 0:
    print(f"No se encontraron repeticiones del gesto {gesto} para el sujeto {sujeto}.")
else:
    # Agrupar repeticiones consecutivas del mismo gesto
    cortes = np.split(indices_gesto, np.where(np.diff(indices_gesto) > 1)[0] + 1)
    
    for i, rep in enumerate(cortes):
        # comienzo y fin del gesto (con margen)
        start = max(rep[0] - margen, 0)
        end = min(rep[-1] + margen, len(emg))

        seg_emg = emg[start:end, canal]
        seg_label = label[start:end]
        t = np.arange(len(seg_emg))

        # escalo la label para graficarla sobre la señal
        label_scaled = (seg_label == gesto) * np.max(seg_emg) * 0.8

        # ===== GRAFICO CADA REPETICIÓN POR SEPARADO =====
        plt.figure(figsize=(12, 4))
        plt.plot(t, seg_emg, color='C0', label='EMG')
        plt.fill_between(t, label_scaled, 0, color='orange', alpha=0.3, label='Gesto activo')

        plt.title(f"Sujeto {sujeto} – Gesto {gesto} – Repetición {i+1}")
        plt.xlabel("Tiempo (muestras)")
        plt.ylabel("Amplitud EMG")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"gesto{gesto}_sujeto{sujeto}_rep{i+1}.png")
        plt.show()