# -*- coding: utf-8 -*-

"""Importo librerías"""

import pickle
import matplotlib.pyplot as plt
import numpy as np

bd_to_use = "DB2"

gestos_seleccionados = [0, 5, 6, 7, 9, 10, 13, 14, 22, 26, 31]

if bd_to_use == "DB2":
    """Entradas"""
    # nombre de archivo de entrada
    nombre_archivo_datos = "data/DB2/data_DB2_concatenado.pickle"
    
    nombre_archivo_salida = "data/DB2/DB2_gestos_seleccionados.pickle"
    
if bd_to_use == "DB3":
    """Entradas"""
    # nombre de archivo de entrada
    nombre_archivo_datos = "data/DB3/data_DB3_concatenado.pickle"
    
    nombre_archivo_salida = "data/DB3/DB3_gestos_seleccionados.pickle"

# Levanto los datos
file = open(nombre_archivo_datos, 'rb')

MyoArm_data = pickle.load(file)
file.close()

for x in MyoArm_data:   # recorro los sujetos
    label_sujeto = MyoArm_data[x]['label'].copy()
    emg_sujeto = MyoArm_data[x]['emg'].copy()
    indices = np.where(np.isin(label_sujeto, gestos_seleccionados))[0]
    MyoArm_data[x]['label'] = label_sujeto[indices]
    MyoArm_data[x]['emg'] = emg_sujeto[indices]
    
with open(nombre_archivo_salida, "wb") as f:
    pickle.dump(MyoArm_data, f)
    
    
    
# """Visualizar cantidad de gestos por sujeto"""
    # cantidad_gestos = []
    # for x in MyoArm_data:   # miro los key del diccionario que tiene los datos
    #     print(x)
    #     etiquetas_unicas = np.unique(MyoArm_data[x]['label'])
    #     cantidad_gestos.append(len(etiquetas_unicas))
    #     print(etiquetas_unicas)
    
    
    # """Visualizar cantidad de gestos por sujeto"""
    # cantidad_gestos = []
    # for x in MyoArm_data:   # miro los key del diccionario que tiene los datos
    #     print(x)
    #     etiquetas_unicas = np.unique(MyoArm_data[x]['label'])
    #     cantidad_gestos.append(len(etiquetas_unicas))
    #     print(etiquetas_unicas)
    
    
        
    # plt.figure()
    # plt.plot(np.arange(1, len(cantidad_gestos)+1), np.array(cantidad_gestos), '-*')
    # plt.xlabel('Sujeto')
    # plt.ylabel('Cantidad de gestos')
    # plt.savefig("cantidad_gestos.png")


# nOfSubjects = 40 # N° of Subjects [1,...,10]- cantidad de sujetos con lo que voy a trabajar
# nChannels = 12 # N° of Channels- numero de canales con los que quiero trabajar- el maximo es MyoArm_data['S1']['emg'].shape[1]+1

# data_list = []  # en cada elemento de la lista guardo los datos de un sujeto, luego los concateno
# label_list = [] # lo mismo que para la anterior
# subject_list = []   # aqui se indica a que sujeto pertenece la senal a lo largo del tiempo

# for i in range(1, nOfSubjects+1):

#     label_list_i = MyoArm_data['DB2_s'+str(i)]['label'] # podria submuestrear acá
#     # Usar np.where para encontrar los índices donde el valor sea 5, 6, 13 o 14
#     indices = np.where((label_list_i == 5) | (label_list_i == 6)  | (label_list_i == 7)  | (label_list_i == 9) | (label_list_i == 10) | (label_list_i == 13) | (label_list_i == 14)| (label_list_i == 0))[0]
#     indices = indices[::10]
#     data_list.extend((MyoArm_data['DB2_s'+str(i)]['emg'])[indices])
#     label_list.extend(label_list_i[indices])
#     subject_list.extend(label_list_i[indices]*0 + i)

# print(len(subject_list))

# # Agrego los gestos del otro experimento
# file = open('MyoArmband_data_DB2_40_E2_cor.pickle', 'rb')
# # file = open('MyoArmband_data_exp2_40_cor.pickle', 'rb')

# MyoArm_data = pickle.load(file)
# file.close()

# for i in range(1, nOfSubjects+1):

#     label_list_i = MyoArm_data['DB2_s'+str(i)]['label'] # podria submuestrear acá
#     # Usar np.where para encontrar los índices donde el valor sea 5, 6, 13 o 14
#     indices = np.where((label_list_i == 17+5) | (label_list_i == 17+9) | (label_list_i == 17+14) | (label_list_i == 0))[0]  # 22, 26, 31
#     indices = indices[::10]
#     data_list.extend((MyoArm_data['DB2_s'+str(i)]['emg'])[indices])
#     label_list.extend(label_list_i[indices])
#     subject_list.extend(label_list_i[indices]*0 + i)

# np.unique(MyoArm_data['DB2_s'+str(i)]['label'])

# plt.figure()
# plt.plot(MyoArm_data['DB3_s'+str(i)]['label'])

# data = np.array(data_list)
# label = np.array(label_list)
# subject = np.array(subject_list)

# MyoArm_data = {
#     'data': data,
#     'label': label,
#     'subject': subject
# }

# plt.figure()
# plt.plot(subject)

# """Procedo a hacer la corrección mencionada"""

# # Aquí podría incluir una visualización rápida de alguna de las señales y sus respectivo vector de labels

# # Guardo los datos
# with open("data_gestos_puntuales_fs200_DB2.pickle", "wb") as f:
#     pickle.dump(MyoArm_data, f)