
import pandas as pd
import numpy as np


def preparar_cancion(cancion, paquete):

    encoder = paquete["encoder"]
    texto = paquete["columnas_categoricas"]
    columnas_modelo = paquete["columnas_modelo"]

    X = pd.DataFrame([cancion])

    if X.isnull().any().any():
        raise ValueError("La canción contiene datos ausentes.")

    nombres = encoder.get_feature_names_out(texto)

    codificadas = encoder.transform(X[texto])

    if hasattr(codificadas, "toarray"):
        codificadas = codificadas.toarray()

    cat = pd.DataFrame(
        codificadas,
        columns=nombres,
        index=X.index
    )

    X = pd.concat(
        [X.drop(columns=texto), cat],
        axis=1
    )

    X = X[columnas_modelo]

    X = X.astype(np.float32)

    return X


def predecir_cancion(cancion, paquete):

    X = preparar_cancion(cancion, paquete)

    modelo = paquete["modelo"]

    prediccion = modelo.predict(X, verbose=0)
    probabilidad = float(np.asarray(prediccion).reshape(-1)[0])

    return float(probabilidad)

