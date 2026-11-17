from fastapi import FastAPI

app = FastAPI(title="GPT1M AI")

@app.get("/")
def home():
    return {
        "nombre": "GPT1M",
        "personaje": "Hayato normal",
        "mascota": "Draki",
        "estilo": "Agresivo",
        "rango_objetivo": "Heroico",
        "estado": "En desarrollo"
    }

@app.get("/estrategia")
def estrategia():
    return {
        "modo": "Battle Royale",
        "personajes": ["Hayato", "Kelly", "Alok"],
        "mascotas": ["Draki", "Rockie"],
        "consejo": "Usa cobertura y trabaja en equipo."
    }
