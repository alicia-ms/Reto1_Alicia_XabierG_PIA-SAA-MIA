
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

import streamlit as st
import pandas as pd
import joblib
from mia.enviar import enviar_decision
from mia import reglas
from mia import motor
from mia.prediccion import predecir_cancion

@st.cache_data
def cargar_datos():
    df = pd.read_csv("../data/raw/billboard_processed.csv")
    return df

@st.cache_resource
def cargar_modelo():
    return joblib.load("../model/RedNeuronal_completo.joblib")

df = cargar_datos()
modelo = cargar_modelo()

st.title("HitPredict AI")
st.subheader("Introduce las características de tu canción")

# Nombre del artista
performer = st.text_input("Nombre artístico", value="Artista Desconocido")

email = st.text_input("Correo electrónico de contacto", value="email@example.com")

cancion = st.text_input("Nombre de la canción", value="loquesea")

# Duración
duracion = st.slider(
    "Duración de la canción (segundos)",
    min_value=30,
    max_value=600,
    value=210
)

spotify_track_duration_ms = duracion * 1000

# Contenido explícito
explicit_opcion = st.radio(
    "¿Contiene contenido explícito?",
    ["Sí", "No"],
    horizontal=True
)
spotify_track_explicit = explicit_opcion == "Sí"

# Género
generos = sorted(
    df["spotify_genre"].dropna().unique().tolist()
)

spotify_genre = st.selectbox(
    "Género musical",
    generos
)

# Características acústicas
danceability = st.slider(
    "Danceability",
    0.0, 1.0, 0.5, 0.01
)

notas = {
    "Do": 0,
    "Do♯ / Re♭": 1,
    "Re": 2,
    "Re♯ / Mi♭": 3,
    "Mi": 4,
    "Fa": 5,
    "Fa♯ / Sol♭": 6,
    "Sol": 7,
    "Sol♯ / La♭": 8,
    "La": 9,
    "La♯ / Si♭": 10,
    "Si": 11
}

nota_seleccionada = st.selectbox(
    "Tonalidad de la canción",
    list(notas.keys())
)

key = notas[nota_seleccionada]

loudness = st.slider(
    "Loudness (dB)",
    -60.0, 0.0, -12.0, 0.1
)

mode_opcion = st.radio(
    "Tonalidad",
    ["Mayor", "Menor"],
    horizontal=True
)
mode = 1 if mode_opcion == "Mayor" else 0

speechiness = st.slider(
    "Speechiness",
    0.0, 1.0, 0.1, 0.01
)

instrumentalness = st.slider(
    "Instrumentalness",
    0.0, 1.0, 0.0, 0.01
)

tempo = st.slider(
    "Tempo (BPM)",
    40, 240, 120
)

time_signature = st.selectbox(
    "Compás musical",
    [3, 4, 5, 6, 7],
    format_func=lambda x: f"{x}/4"
)

acoustic_mood_cluster = st.selectbox(
    "Perfil acústico",
    [
        "balanced_acoustic_pop",
        "chill_downtempo_groove",
        "high_energy_euphoric",
        "intense_aggressive_drive",
        "moody_melancholic"
    ]
)

if st.button("Predecir éxito de la canción"):
    datos_cancion = {
        "performer": performer,
        "spotify_track_duration_ms": spotify_track_duration_ms,
        "spotify_track_explicit": spotify_track_explicit,
        "spotify_genre": spotify_genre,
        "danceability": danceability,
        "key": key,
        "loudness": loudness,
        "mode": mode,
        "speechiness": speechiness,
        "instrumentalness": instrumentalness,
        "tempo": tempo,
        "time_signature": time_signature,
        "acoustic_mood_cluster": acoustic_mood_cluster
    }
    
    if reglas.si_R2(datos_cancion):

        st.error("Faltan datos obligatorios.")
        st.stop()

    if not cancion.strip() or not email.strip():

        st.error("Introduce el nombre de la canción y tu correo.")
        st.stop()

    try:
                           
        probabilidad = predecir_cancion(datos_cancion, modelo)
        
        datos_cancion["p"] = float(probabilidad)

        resultado = motor.motor(datos_cancion, reglas.reglas)
        
        datos_n8n = {
        "cancion": cancion,
        "performer": performer,
        "email": email,
        "probabilidad": probabilidad,
        "decision": resultado["decision"],
        "reglas_aplicadas": resultado["usadas"],
        "explicacion": resultado["porque"],
        "modelo": "Red neuronal"
        }

        enviar_decision(datos_n8n)
        
        st.write(
            f"Probabilidad de entrar en el Top 30: "
            f"{probabilidad:.2%}"
        )

        # st.success(resultado["decision"])
        # st.write("Reglas aplicadas:", resultado["usadas"])
        # st.write("Explicación:", resultado["porque"]) 
        
        
    except Exception as e:
        st.error(f"Se ha producido un error al procesar la canción: {e}")
