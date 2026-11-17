# GPT2M
GPTFF

from fastapi import FastAPI

app = FastAPI(title="GPT2M AI")

jugador = {
    "nombre": "GPT 1M",
    "personaje": "Hayato normal",
    "mascota": "Draki",
    "estilo": "Agresivo",
    "rango_objetivo": "Heroico",
    "armas": "Todas"
}

@app.get("/")
def inicio():
    return {
        "mensaje": "GPT2M AI está funcionando",
        "jugador": jugador
    }

@app.get("/estrategia")
def estrategia():
    return {
        "modo": "Battle Royale y Duelo de Escuadras",
        "estilo": "Agresivo",
        "objetivo": "Mejorar precisión y reflejos"
    }
