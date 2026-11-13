import math

LIMITE_INVERSION = 0.80
LIMITE_REVISION_ALTA = 0.60
LIMITE_REVISION_MEDIA = 0.40


def si_R1(d):
    """R1 (SEGURIDAD). ¿La probabilidad del modelo es inválida?"""
    p = d.get("p")

    try:
        p = float(p)
    except (TypeError, ValueError):
        return True

    return not math.isfinite(p) or not 0 <= p <= 1


def si_R2(d):
    """R2 (SEGURIDAD). ¿Falta algún dato obligatorio?"""

    campos_obligatorios = [
        "performer",
        "spotify_track_duration_ms",
        "spotify_track_explicit",
        "spotify_genre",
        "danceability",
        "key",
        "loudness",
        "mode",
        "speechiness",
        "instrumentalness",
        "tempo",
        "time_signature",
        "acoustic_mood_cluster"
    ]

    for campo in campos_obligatorios:
        valor = d.get(campo)

        if valor is None:
            return True

        if isinstance(valor, str) and not valor.strip():
            return True

        if isinstance(valor, (float, int)) and not math.isfinite(valor):
            return True

    return False
    
def si_R3(d):
    """R3. ¿La probabilidad es igual o superior al 80 %?"""
    return float(d["p"]) >= LIMITE_INVERSION


def si_R4(d):
    """R4. ¿La probabilidad está entre el 60 % y el 80 %?"""
    return (
        LIMITE_REVISION_ALTA <= float(d["p"])
        < LIMITE_INVERSION
    )


def si_R5(d):
    """R5. ¿La probabilidad está entre el 40 % y el 60 %?"""
    return (
        LIMITE_REVISION_MEDIA <= float(d["p"])
        < LIMITE_REVISION_ALTA
    )


def si_R6(d):
    """R6. ¿La probabilidad es inferior al 40 %?"""
    return float(d["p"]) < LIMITE_REVISION_MEDIA


reglas = [
    ('R1', si_R1, {'decision':'BLOQUEAR ANALISIS'}, 10, 'La probabilidad del modelo es inexistente o inválida.'),
    ('R2', si_R2, {'decision':'SOLICITAR CORRECCION'}, 10, 'Falta algún dato obligatorio.'),
    ('R3', si_R3, {'decision':'RECOMENDAR INVERSION'}, 3, 'La probabilidad es igual o superior al 80 %.'),
    ('R4', si_R4, {'decision':'REVISION PRIORITARIA'}, 2, 'La probabilidad está entre el 60 % y el 80 %.'),
    ('R5', si_R5, {'decision':'REVISION ADICIONAL'}, 1, 'La probabilidad está entre el 40 % y el 60 %.'),
    ('R6', si_R6, {'decision':'NO RECOMENDAR INVERSION'}, 1, 'La probabilidad es inferior al 40 %.'),
]