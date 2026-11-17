
# 🎵 Spotify Music Analysis & Machine Learning

Análisis exploratorio de canciones de Spotify, identificación de patrones musicales mediante **Mood Clusters** y desarrollo de modelos de Machine Learning para estudiar la popularidad de las canciones.

---

## 📌 Descripción del proyecto

Este proyecto tiene como objetivo analizar un conjunto de datos de canciones de Spotify para estudiar sus características musicales, identificar patrones y explorar qué factores pueden estar relacionados con la popularidad de las canciones.

A través de técnicas de análisis exploratorio de datos, visualización y Machine Learning, se estudian las relaciones entre diferentes atributos musicales y se desarrollan modelos predictivos.

## 🎯 Objetivos

- Realizar un análisis exploratorio del conjunto de datos.
- Estudiar la distribución de las principales características musicales.
- Analizar las relaciones entre atributos como *danceability*, *loudness*, *tempo* e *instrumentalness*.
- Explorar los patrones musicales mediante agrupaciones (*Mood Clusters*).
- Estudiar la relación entre las características de las canciones y su popularidad.
- Entrenar y comparar diferentes modelos de Machine Learning.
- Optimizar los hiperparámetros de los modelos.
- Registrar y realizar un seguimiento de los experimentos mediante MLflow.

## 📊 Dataset

El conjunto de datos contiene información sobre canciones y sus características musicales.

Entre las principales variables encontramos:

| Variable | Descripción |
|---|---|
| `performer` | Artista o intérprete |
| `spotify_genre` | Género musical |
| `spotify_track_duration_ms` | Duración de la canción |
| `spotify_track_explicit` | Indica si contiene contenido explícito |
| `danceability` | Facilidad para bailar |
| `loudness` | Nivel de volumen |
| `speechiness` | Presencia de palabras habladas |
| `instrumentalness` | Probabilidad de que sea instrumental |
| `tempo` | Velocidad de la canción |
| `acoustic_mood_cluster` | Agrupación según características musicales |
| `top30` | Variable relacionada con la popularidad |

## 🔍 Análisis exploratorio de datos (EDA)

Se realiza un análisis exploratorio para comprender la estructura del dataset, estudiar sus variables y detectar patrones relevantes.

Se utilizan diferentes técnicas de visualización:

- Histogramas para analizar la distribución de las variables numéricas.
- Gráficos de barras para estudiar variables categóricas.
- Diagramas de dispersión para identificar relaciones entre características musicales.
- Boxplots para comparar las características entre diferentes *Mood Clusters*.
- Mapas de calor para visualizar perfiles medios y correlaciones.

### Visualizaciones

**Distribución de características musicales**

![Distribución de variables](imagenes/distribucion_variables.png)

**Relación entre características musicales y Mood Clusters**

![Mood Clusters](imagenes/mood_clusters.png)

**Comparación de Danceability entre Mood Clusters**

![Danceability por Mood Cluster](imagenes/danceability_mood_clusters.png)

## 🤖 Machine Learning

Se desarrolla una fase de aprendizaje automático para estudiar la capacidad predictiva de las características musicales.

Se prueban diferentes algoritmos de clasificación y se comparan sus resultados para seleccionar los modelos con mejor rendimiento.

### Modelos utilizados

- K-Nearest Neighbors (KNN).
- Random Forest.
- XGBoost.

### Optimización y evaluación

Se realizan pruebas con diferentes combinaciones de hiperparámetros para mejorar el rendimiento de los modelos.

La evaluación se lleva a cabo utilizando conjuntos de entrenamiento, validación y prueba, empleando principalmente la métrica **F1-score** para comparar los resultados.

### Seguimiento de experimentos con MLflow

Se utiliza MLflow para registrar y organizar los experimentos de Machine Learning.

Se almacenan parámetros, métricas y resultados de los modelos, facilitando la comparación entre diferentes configuraciones y el seguimiento del proceso de entrenamiento.

## 📈 Resultados

En esta sección se presentan las principales conclusiones obtenidas durante el análisis exploratorio y la evaluación de los modelos.

Se incluyen comparaciones entre algoritmos, resultados de las métricas y visualizaciones que permiten interpretar los patrones identificados en los datos.

![Resultados de los modelos](imagenes/resultados_modelos.png)

## 🛠️ Tecnologías y herramientas

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,anaconda,vscode,git,github" />
</p>

**Librerías y herramientas de análisis:**

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- MLflow

<p align="center">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Seaborn-4c72b0?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/XGBoost-EC6B23?style=for-the-badge" />
  <img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white" />
</p>

## 👩‍💻 Autores

- Alicia Martinez
- Xabier Garcia

---

*Proyecto desarrollado como parte de la especialización en Inteligencia Artificial y Big Data.*
