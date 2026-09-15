# agregar_persona("Ana", 28)
# agregar_persona("Bob", 17)
#
#   diccionario: {"Ana": 28, "Bob": 17}
#
#   personas_mayores(18):
#     Ana -> 28 >= 18? Sí -> incluir
#     Bob -> 17 >= 18? No -> excluir
#
#   Resultado: ["Ana"]

class GestorPersonas:
    def __init__(self):
        self.personas = {}  # diccionario {nombre: edad}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado

    def edad_promedio(self):
        if not self.personas:
            return 0
        return sum(self.personas.values()) / len(self.personas)
gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
print(gp.personas_mayores(18))