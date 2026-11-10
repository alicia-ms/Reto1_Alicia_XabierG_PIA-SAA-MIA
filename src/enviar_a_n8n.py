import requests

datos = {
    "cancion": "Mi canción",
    "artista": "Artista de prueba",
    "email": "contacto@ejemplo.com",
    "probabilidad_top30": 0.70,
    "decision": "invertir",
    "modelo": "Random Forest",
    "fecha": "2026-11-09"
}

respuesta = requests.post(
    "http://localhost:5678/webhook-test/empresa/decision",
    json=datos
)

print(respuesta.status_code)
print(respuesta.text)