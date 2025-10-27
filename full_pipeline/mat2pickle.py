# -*- coding: utf-8 -*-
"""Importo librerías"""
import scipy.io
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt

bd_to_use = "DB3"

if bd_to_use == "DB2":
    """Para DB2"""
    """Defino los datos de qué sujeto voy a usar"""
    # directorio de los datos
    data_dir = "data/DB2/"
    os.chdir(data_dir)

    # Número de sujetos
    nSubjects = 40

    # nombre carpeta
    nombre_folder = "DB2_s"

    # nombre archivo salida
    nombre_archivo_salida = "data_DB2_concatenado.pickle"

    # Lista [DB2_s1, DB2_s2, ..., DB2_s42]
    files = [nombre_folder + str(x) for x in range(1, nSubjects+1)]
    data = dict()

    # Recorro los sujetos
    for i, file in enumerate(files, start=1):
        # Cargo los tres experimentos
        E1 = scipy.io.loadmat(f"{file}/{file}/S{i}_E1_A1.mat")
        E2 = scipy.io.loadmat(f"{file}/{file}/S{i}_E2_A1.mat")
        E3 = scipy.io.loadmat(f"{file}/{file}/S{i}_E3_A1.mat")

        # Concateno las señales EMG y las etiquetas
        emg_concat = np.concatenate([E1["emg"], E2["emg"], E3["emg"]])
        label_concat = np.concatenate([E1["restimulus"], E2["restimulus"], E3["restimulus"]])
        
        # Guardo todo en un diccionario
        data[file] = {
            'emg': emg_concat,
            'label': label_concat,
            'description': "Contiene datos de EMG concatenados de los ejercicios E1, E2 y E3 del sujeto."
        }

    # Guardo el archivo con los datos originales de todos los experimentos
    with open(nombre_archivo_salida, "wb") as f:
        pickle.dump(data, f)

elif bd_to_use == "DB3":    # Defino los datos de qué sujeto voy a usar
    """Para DB3"""
    # directorio de los datos
    data_dir = "data/DB3/"
    os.chdir(data_dir)

    # Número de sujetos
    nSubjects = 11

    # nombre carpeta
    nombre_folder = "DB3_s"

    # nombre archivo salida
    nombre_archivo_salida = "data_DB3_concatenado.pickle"

    # Lista
    files = [nombre_folder + str(x) for x in range(2, nSubjects+1)]
    data = dict()

    # Recorro los sujetos
    
    for i, file in enumerate(files, start=1):
        # Cargo los tres experimentos
        E1 = scipy.io.loadmat(f"{file}/S{i+1}_E1_A1.mat")
        E2 = scipy.io.loadmat(f"{file}/S{i+1}_E2_A1.mat")
        E3 = scipy.io.loadmat(f"{file}/S{i+1}_E3_A1.mat")

        # Concateno las señales EMG
        emg_concat = np.concatenate([E1["emg"], E2["emg"], E3["emg"]])

        # Concateno todas las etiquetas
        label_concat = np.concatenate([E1["restimulus"], E2["restimulus"], E3["restimulus"]])

        # Guardo todo en un diccionario
        data[file] = {
            'emg': emg_concat,
            'label': label_concat,
            'description': "Contiene datos de EMG concatenados de los ejercicios E1, E2 y E3 del sujeto. Datos correspondientes a DB3."
        }
    # Guardo el archivo con los datos originales de todos los experimentos
    with open(nombre_archivo_salida, "wb") as f:
        pickle.dump(data, f)
        
# # Lista [DB2_s1, DB2_s2, ..., DB2_s42]
# files = [nombre_folder + str(x) for x in range(1, nSubjects+1)]
# data = dict()
# print(files)
# # """"Visualizacion en sujeto 1"""
# i = 0
# for file in files:
#     i += 1
#     E1 = scipy.io.loadmat("s"+str(i)+"_0" + '/' + file + '/' + 'S' + str(i) + '_E1_A1.mat') # Ejercicio 1
#     for x in E1:    # miro los key del diccionario que tiene los datos
#         print(x)    
#     if i == 1:
#         break
# pre visualizacion de EMG
# print(E1["emg"].shape)

# plt.figure()
# plt.plot(E1["emg"][:, 0])
# plt.savefig("emg_0.png")
# plt.show()

# # pre visualizacion de acc
# print(E1["acc"].shape)
# plt.figure()
# plt.plot(E1["acc"][:, 0])
# plt.savefig("acc_0.png")
# plt.show()

# # pre visualizacion de stimulus
# print(E1["stimulus"].shape)
# plt.figure()
# plt.plot(E1["stimulus"][:, 0])
# plt.savefig("stimulus_0.png")
# plt.show()

# # pre visualizacion de glove
# print(E1["glove"].shape)
# plt.figure()
# plt.plot(E1["glove"][:, 0])
# plt.savefig("glove_0.png")
# plt.show()

# # pre visualizacion de inclin
# print(E1["inclin"].shape)
# plt.figure()
# plt.plot(E1["inclin"][:, 0])
# plt.plot(E1["inclin"][:, 1])
# plt.savefig("inclin_0.png")
# plt.show()

# # pre visualizacion de subject
# print(E1["subject"])

# # pre visualizacion de exercise
# print(E1["exercise"].shape)

# # pre visualizacion de repetition
# print(E1["repetition"].shape)

# plt.figure()
# plt.plot(E1["repetition"][:, 0])
# plt.savefig("repetition_0.png")
# plt.show()

# # pre visualizacion de repetition
# print(E1["restimulus"].shape)

# plt.figure()
# plt.plot(E1["restimulus"][:, 0])
# plt.savefig("restimulus_0.png")
# plt.show()

# # pre visualizacion de repetition
# print(E1["rerepetition"].shape)

# plt.figure()
# plt.plot(E1["rerepetition"][:, 0])
# plt.savefig("rerepetition_0.png")
# plt.show()

"""comparacion entre etiquetas y etiquetas modificadas"""

# # pre visualizacion de repetition
# print(E1["repetition"].shape)

# plt.figure()
# plt.plot(E1["stimulus"][300000:500000, 0])
# plt.plot(E1["restimulus"][300000:500000, 0])
# plt.legend(['stimulus', 're'])

# plt.savefig("sti_vs_resti.png")
# plt.show()








