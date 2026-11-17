
from fastapi import FastAPI

app = FastAPI(title="GPT2M AI")

@app.get("/")
def home():
    return {
        "nombre": "GPT 1M",
        "personaje": "Hayato normal",
        "mascota": "Draki",
        "estilo": "Agresivo",
        "rango_objetivo": "Heroico",
        "estado": "En desarrollo"
    }

@app.get("/estrategia")
def estrategia():
    return {
        "modos": ["Battle Royale", "Duelo de Escuadras"],
        "armas": "Todas",
        "precision": "Alta",
        "reflejos": "Rapidos"
    }
