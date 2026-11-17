import os
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parent / ".env")

URL_N8N = os.getenv("N8N_URL")
CLAVE = os.getenv("N8N_CLAVE")
CABECERA = os.getenv("N8N_CABECERA", "X-Api-Key")


def enviar_decision(datos):
    if not URL_N8N or not CLAVE:
        return False, (
            "ERROR: falta el archivo .env o está incompleto. "
            "Revisad N8N_URL y N8N_CLAVE."
        )

    headers = {
        CABECERA: CLAVE
    }

    try:
        respuesta = requests.post(
            URL_N8N,
            json=datos,
            headers=headers,
            timeout=15
        )

        respuesta.raise_for_status()

        try:
            resultado = respuesta.json()
        except ValueError:
            resultado = respuesta.text

        return True, resultado

    except requests.RequestException as e:
        return False, str(e)