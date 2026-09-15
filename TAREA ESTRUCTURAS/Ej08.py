# crear_equipo("A")            -> equipos = {"A": []}
# agregar_jugador("A", "Juan")  -> equipos = {"A": ["Juan"]}
# agregar_jugador("A", "Pedro") -> equipos = {"A": ["Juan", "Pedro"]}
#
#   equipo_mayor_integrantes():
#     reviso cada equipo del diccionario
#     "A" tiene 2 jugadores -> es el único, por lo tanto el mayor
#
#   Resultado: "A"

class Equipos:
    def __init__(self):
        self.equipos = {}  # diccionario {nombre_equipo: [jugadores]}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = None
        for nombre, jugadores in self.equipos.items():
            if mayor is None or len(jugadores) > len(self.equipos[mayor]):
                mayor = nombre
        return mayor
eq = Equipos()
eq.crear_equipo("A")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
print(eq.equipos)
