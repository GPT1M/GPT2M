import random

class GPT1MBot:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.vida = 100
        self.modo = "PVP"

    def decidir(self):
        if self.vida < 30:
            return "Buscar cobertura"

        acciones = [
            "Avanzar",
            "Moverse a la derecha",
            "Moverse a la izquierda",
            "Buscar cobertura"
        ]
        return random.choice(acciones)

    def jugar(self):
        accion = self.decidir()

        if accion == "Avanzar":
            self.y += 1
        elif accion == "Moverse a la derecha":
            self.x += 1
        elif accion == "Moverse a la izquierda":
            self.x -= 1

        return {
            "modo": self.modo,
            "accion": accion,
            "posicion": [self.x, self.y],
            "vida": self.vida
        }

bot = GPT1MBot()
