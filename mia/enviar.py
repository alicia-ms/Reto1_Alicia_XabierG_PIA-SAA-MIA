
import requests


URL_N8N = "http://localhost:5678/webhook-test/empresa/decision"


def enviar_decision(datos):

    try:
        respuesta = requests.post(
            URL_N8N,
            json=datos,
            timeout=15
        )

        respuesta.raise_for_status()

        return True, respuesta.text

    except requests.RequestException as e:

        return False, str(e)
