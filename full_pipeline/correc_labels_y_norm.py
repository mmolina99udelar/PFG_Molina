# -*- coding: utf-8 -*-
"""Importo librerías"""

import pickle
import matplotlib.pyplot as plt
import numpy as np
import os

""""Variables de entrada"""
# TODO explicar en algun lado la forma que tienen que tener estos datos de entrada
# nombre del archivo de datos
nombre_archivo_datos = "MyoArmband_data_DB2_40_E2.pickle"
# Numero de muestras de la correccion
correc = 2000

# me sitúo en el directorio que tiene los datos
os.chdir("data/")

# TODO que las claves sean una variable, ahora está hardcodeado para DB2

"""Levanto los datos y establezco la cantidad de muestras que voy a quitar de cada borde de cada repetición"""

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/drive/My Drive/repo_tesis/src/ronda_gestos_puntuales"

file = open(nombre_archivo_datos, 'rb')
MyoArm_data = pickle.load(file)
file.close()


# Iterar sobre las claves y los valores
for clave, valor in MyoArm_data.items():
    print(f"Clave: {clave}")

# """Procedo a hacer la corrección mencionada"""

# new_emg = []    # Creo una lista para guardar los datos de emg corregidos
# new_label = []  # Creo una lista para guardar las etiquetas corregidas

# for j in range(len(MyoArm_data)):
#     EMG = MyoArm_data['DB2_s'+str(j+1)]['emg']  # tengo 16 se;ales de emg aca
#     etiqueta = MyoArm_data['DB2_s'+str(j+1)]['label']
#     etiqueta = etiqueta[:, 0]
#     indices_ventanas = np.where(np.diff(etiqueta)!=0)[0]

#     # Ahora tengo que chequear la senal no comience o termine en la mitad de un gesto, en caso positivo lo tiro
#     # Chequeo el comienzo
#     if etiqueta[0] != 0:
#         etiqueta = etiqueta[(indices_ventanas[0]+1):]    # Recorto la señal hasta el indice donde termina la ventana que estoy tirando
#         EMG = EMG[(indices_ventanas[0]+1):, :]
#         indices_ventanas = np.where(np.diff(etiqueta)!=0)[0]

#     # Chequeo el fin
#     if etiqueta[-1] != 0:
#         etiqueta = etiqueta[:(indices_ventanas[-1])]    # Recorto la señal hasta el indice donde termina la ventana que estoy tirando
#         EMG = EMG[:(indices_ventanas[-1]), :]
#         indices_ventanas = indices_ventanas[:-1]

#     # Procedo a hacer la correccion
#     for i in range(int(len(indices_ventanas)/2)):     # El largo/2 da la cantidad de ventanas
#         etiqueta[indices_ventanas[2*i]: (indices_ventanas[2*i]+correc)] = 0            # indices_ventanas[2*i] se para en cada lugar que arranca una ventana (indices pares)
#         etiqueta[((indices_ventanas[2*i+1])-correc+1):(indices_ventanas[2*i+1])+1] = 0     # indices_ventanas[2*i+1] se para en los finales de cada ventana.

#     # Procedo a hacer la normalizacion
#     # Normalizacion con distribucion normal. Lo voy a hacer por columna
#     for i in range(EMG.shape[1]):
#         EMG[:, i] = (EMG[:, i] - np.mean(EMG[:, i]))/np.std(EMG[:, i])

#     # Modifico el archivo de datos
#     MyoArm_data['DB2_s'+str(j+1)]['emg'] = EMG
#     MyoArm_data['DB2_s'+str(j+1)]['label'] = etiqueta

# # Aquí podría incluir una visualización rápida de alguna de las señales y sus respectivo vector de labels

# # Guardo los datos
# with open("MyoArmband_data_DB2_40_E2_cor.pickle", "wb") as f:
#     pickle.dump(MyoArm_data, f)