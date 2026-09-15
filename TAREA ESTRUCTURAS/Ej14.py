# registrar("Ana", 95)
# registrar("Bob", 70)
#
#   diccionario: {"Ana": 95, "Bob": 70}
#
#   mejor_estudiante():
#     reviso "Ana" -> 95, aún no hay mejor -> mejor = ("Ana", 95)
#     reviso "Bob" -> 70, ¿70 > 95? No -> mejor sigue siendo Ana
#
#   Resultado: ("Ana", 95)

class RegistroNotas:
    def __init__(self):
        self.notas = {}  # diccionario {estudiante: nota}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        """Retorna lista de estudiantes con nota >= nota_minima."""
        return [nombre for nombre, nota in self.notas.items() if nota >= nota_minima]

    def mejor_estudiante(self):
        """Retorna (nombre, nota) del estudiante con mayor calificación."""
        mejor_nombre = None
        mejor_nota = None
        for nombre, nota in self.notas.items():
            if mejor_nota is None or nota > mejor_nota:
                mejor_nombre, mejor_nota = nombre, nota
        return (mejor_nombre, mejor_nota)


rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.mejor_estudiante())