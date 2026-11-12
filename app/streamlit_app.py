
import streamlit as st
import pandas as pd
import joblib
from src import reglas
from src import motor

@st.cache_data
def cargar_datos():
    df = pd.read_csv("../data/raw/billboard_processed.csv")
    return df

# Lo ideal es guardar un Pipeline completo que incluya el procesamiento y el modelo.
# @st.cache_resource
# def cargar_modelo():
#     # Carga tu modelo entrenado (Random Forest u otro)
#     # Asegúrate de haber guardado tu modelo como 'modelo_hit.pkl' o cámbialo por tu nombre
#     return joblib.load("modelo_hit.pkl")

df = cargar_datos()
#modelo = cargar_modelo()

st.title("HitPredict AI")
st.subheader("Introduce las características de tu canción")

# Nombre del artista
performer = st.text_input("Nombre artístico", value="Artista Desconocido")

email = st.text_input("Correo electrónico de contacto", value="")

cancion = st.text_input("Nombre de la canción", value="")

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
    "Time signature",
    [3, 4, 5, 6, 7]
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
    cancion = {
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

    try:
        
        # 2. Aquí validaremos los datos y ejecutaremos el modelo
        # probabilidad = ...
        
        # if probabilidad is None:
        #     st.info(
        #         "El modelo todavía no está conectado. "
        #         "Introduce una probabilidad de prueba para "
        #         "comprobar el funcionamiento de las reglas."
        #     )

        # 3. Añadir la probabilidad al caso
        #cancion["p"] = probabilidad

        # 4. Ejecutar el motor de reglas
        resultado = motor(cancion, reglas)

        # 5. Mostrar la decisión
        st.success(resultado["decision"])
        st.write("Reglas aplicadas:", resultado["usadas"])
        st.write("Explicación:", resultado["porque"]) 
        
        
    except Exception as e:
        st.error(f"Se ha producido un error al procesar la canción: {e}")
