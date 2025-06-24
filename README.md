# PFG_Molina

Este repositorio contiene los códigos correspondientes al Proyecto de Fin de Grado titulado:

**“Técnicas de clasificación automática de gestos manuales para sujetos intactos y con amputación transradial”**

---

## Tabla de contenido

- [1. Pruebas preliminares](#1-pruebas-preliminares)
  - [1.1 Exploración de las señales](#11-exploración-de-las-señales)
  - [1.2 Acceso y preprocesamiento de datos](#12-acceso-y-preprocesamiento-de-datos)
  - [1.3 Línea base (Baseline)](#13-línea-base-baseline)
- [2. Arquitecturas alternativas a ventana aislada](#2-arquitecturas-alternativas-a-ventana-aislada)
- [3. Evaluación en sujetos con amputación](#3-evaluación-en-sujetos-con-amputación)
  - [3.1 Visualización general](#31-visualización-general)
  - [3.2 Preparación de los datos](#32-preparación-de-los-datos)
- [4. Implementación de RNN](#4-implementación-de-rnn)
- [5. Otros recursos](#5-otros-recursos)

---

## 1. Pruebas preliminares

### 1.1 Exploración de las señales

Para visualizar las señales por sujeto, gesto o canal, ejecutar:

- `pruebas_preliminares/exploracion_sigs.ipynb`

Este script genera las imágenes utilizadas en las figuras del informe.

### 1.2 Acceso y preprocesamiento de datos

Pasos a seguir:

1. Descargar los archivos `.zip` desde [NinaPro - DB5](https://ninapro.hevs.ch/).
2. Descomprimirlos en una misma carpeta. Se generan subcarpetas `S_i` (sujetos 1 a 10), cada una con 3 archivos `.mat`.
3. Ejecutar:
   - `pruebas_preliminares/acondicionamiento_datos/mat2pickle_exp1.ipynb` → genera `MyoArmband_data_exp1.pickle`.
   - `pruebas_preliminares/acondicionamiento_datos/labelsCorrection.ipynb` → genera `MyoArmband_data_exp1_cor.pickle`.
   - `featuresCalc.ipynb` → define ventanas y calcula características. Crea dos archivos `.joblib` (features y etiquetas).

### 1.3 Línea base (Baseline)

#### Visualización general

- `pruebas_preliminares/baseline/experimentsStats_baseline.ipynb`

#### Implementación de modelos

- GBM:  
  `pruebas_preliminares/baseline/implementacion_modelos/gbm_baseline_por_sujeto.ipynb`

- MLP:  
  `pruebas_preliminares/baseline/implementacion_modelos/mlp_baseline_por_sujeto.ipynb`

Los experimentos están en Comet bajo los nombres:
- `baseline_gbm_sep_sub<i>_test`
- `baseline_mlp_sep_sub<i>_test`

#### Generación de particiones

- Por sujeto: `pruebas_preliminares/particiones_datos/divisionXFolds_sujeto.ipynb`  
- Por repetición: `pruebas_preliminares/particiones_datos/divisionXFolds_repeticion.ipynb`

---

## 2. Arquitecturas alternativas a ventana aislada

### MLP

- `10_es_test_MLP.ipynb`: entrenamiento con early stopping.

### Otras arquitecturas

1. Ejecutar `10_gs_and_test_<arquitectura>.ipynb` (grid search).
2. Ejecutar `visualizacion_resultados_<arquitectura>.ipynb` para elegir hiperparámetros.
3. Volver al paso 1 y ejecutar entrenamiento con parámetros elegidos.
4. Visualizar resultados en `visualizacion_train_test.ipynb`.

---

## 3. Evaluación en sujetos con amputación

### 3.1 Visualización general

- `clasificacion_sujetos_amputacion/visualizar_resultados_estrategias.ipynb`

### 3.2 Preparación de los datos

#### Selección de gestos y submuestreo

- `seleccionar_gestos.ipynb`: reduce frecuencia de muestreo de 2000Hz a 200Hz. Entrada: `MyoArmband_data_exp1_cor.pickle`.

> Los datos ya procesados se encuentran en la carpeta `data`.

#### Generación de datasets

- `generar_datasets_DB2.ipynb`
- `generar_datasets_DB3.ipynb`

Ambos permiten normalizar o mantener los datos crudos, y elegir el tipo de partición.

---

## 4. Implementación de RNN

### Estrategia 1

1. `generar_datasets_DB3.ipynb` (por sujeto)  
2. `rnn_DB2.ipynb` (sin test)  
3. `rnn_DB3.ipynb` (test = todos los sujetos)  
4. Evaluar sobre test con modelo de DB2

### Estrategia 2

1. Igual que estrategia 1  
2. Igual que estrategia 1  
3. `rnn_DB3.ipynb` (con train/val/test)  
4. Evaluar sobre test

### Estrategia 3

1. `generar_datasets_DB3.ipynb` (por sujeto)  
2. `rnn_DB3.ipynb` (con test)

### Estrategia 4

1. `generar_datasets_DB3.ipynb` (por repetición)  
2. `rnn_DB3_est4.ipynb` (configurar `sujeto_part`, sin fine tuning)

### Estrategia 5

1. Igual que estrategia 4  
2. `rnn_DB3.ipynb` (configurar `sujeto_part`)  
3. Ejecutar fine tuning

---

## 5. Otros recursos

- **Diagrama de estructura del repositorio**:  
  [Ver en Miro](https://miro.com/app/board/uXjVOEfrqJw=/?share_link_id=598681296065)

---
