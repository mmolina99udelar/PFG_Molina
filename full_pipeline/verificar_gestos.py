# -*- coding: utf-8 -*-

"""Importo librerías"""

import pickle
import matplotlib.pyplot as plt
import numpy as np

# Configuración
bd_to_use = "DB2"
gestos_seleccionados = [0, 5, 6, 7, 9, 10, 13, 14, 22, 26, 31]

# Selección de base de datos
if bd_to_use == "DB2":
    nombre_archivo_datos = "data/DB2/DB2_gestos_seleccionados.pickle"
elif bd_to_use == "DB3":
    nombre_archivo_datos = "data/DB3/DB3_gestos_seleccionados.pickle"

# Levanto los datos
with open(nombre_archivo_datos, 'rb') as file:
    MyoArm_data = pickle.load(file)

# Diccionario para guardar la cantidad de repeticiones por sujeto
repeticiones_todos = {}

# -------------------------------------------------------------------------
# Procesamiento por sujeto
# -------------------------------------------------------------------------
for x in MyoArm_data:
    label = MyoArm_data[x]['label'].copy().ravel()
    rep_por_gesto = {}

    for gesto in np.unique(label):
        if gesto == 0:
            continue  # excluyo gesto de reposo
        
        indices_gesto = np.where(label == gesto)[0]
        if len(indices_gesto) == 0:
            continue

        # Agrupar repeticiones consecutivas del mismo gesto
        cortes = np.split(indices_gesto, np.where(np.diff(indices_gesto) > 1)[0] + 1)
        rep_por_gesto[gesto] = len(cortes)
    
    repeticiones_todos[x] = rep_por_gesto

# -------------------------------------------------------------------------
# Figura comparativa: todos los sujetos
# -------------------------------------------------------------------------
n_sujetos = len(repeticiones_todos)

# Determinar todos los gestos posibles (eje X común)
todos_gestos = sorted(set().union(*[rep.keys() for rep in repeticiones_todos.values()]))

fig, axs = plt.subplots(n_sujetos, 1, figsize=(10, 3 * n_sujetos), constrained_layout=True)

if n_sujetos == 1:
    axs = [axs]  # para el caso de un solo sujeto

for ax, (sujeto, rep_por_gesto) in zip(axs, repeticiones_todos.items()):
    # Obtener las repeticiones para todos los gestos (0 si el gesto no está)
    repeticiones = [rep_por_gesto.get(g, 0) for g in todos_gestos]

    ax.bar(todos_gestos, repeticiones, color='cornflowerblue', edgecolor='black')
    ax.set_title(f"{sujeto}")
    ax.set_xlabel("Gesto")
    ax.set_ylabel("Repeticiones")
    ax.set_xticks(todos_gestos)
    ax.set_xlim(min(todos_gestos) - 0.5, max(todos_gestos) + 0.5)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.suptitle(f"Cantidad de repeticiones por gesto ({bd_to_use})", fontsize=14, y=1.02)

# Guardar solo la figura conjunta
plt.savefig(f"{bd_to_use}_repeticiones_todos.png", bbox_inches="tight")
plt.show()
