import requests
from app import stramlit_app as st
from src import reglas
from src import motor

datos = {
    "canción": st.cancion,
    "artista": st.performer,
    "email": st.email,
    "probabilidad_top30": 0.70,
    #"decision": motor.motor(caso, reglas)['decision'],
    "modelo": "Random Forest",
}

respuesta = requests.post(
    "http://localhost:5678/webhook-test/empresa/decision",
    json=datos
)

print(respuesta.status_code)
print(respuesta.text)