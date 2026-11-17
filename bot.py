from fastapi import FastAPI

app = FastAPI(title="GPT1M AI")

@app.get("/")
def home():
    return {
        "nombre": "GPT1M",
        "estado": "Funcionando",
        "modos": ["Battle Royale", "PVP", "1 vs 1"]
    }

@app.get("/estrategia")
def estrategia():
    return {
        "modo": "Battle Royale",
        "personajes": ["Hayato", "Kelly", "Alok"],
        "mascotas": ["Draki", "Rockie"],
        "consejo": "Usa cobertura y trabaja en equipo."
    }

@app.get("/pvp")
def pvp():
    return {
        "modo": "PVP - Duelo de Escuadras",
        "personajes": ["Hayato", "Kelly", "Alok"],
        "consejo": "Coordina con tu equipo y aprovecha la cobertura."
    }

@app.get("/1vs1")
def uno_vs_uno():
    return {
        "modo": "1 vs 1",
        "personaje": "Hayato",
        "mascota": "Draki",
        "consejo": "Mantén la calma, practica tu precisión y usa bien la cobertura."
    }
