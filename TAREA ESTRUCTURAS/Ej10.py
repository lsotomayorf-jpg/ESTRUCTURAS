# agregar_tarea("Estudiar", "alta")
# agregar_tarea("Leer", "baja")
#
#   lista de tuplas: [("Estudiar", "alta"), ("Leer", "baja")]
#
#   tareas_prioritarias():
#     ("Estudiar","alta") -> prioridad == "alta"? Sí -> incluir
#     ("Leer","baja")     -> prioridad == "alta"? No -> excluir
#
#   Resultado: [("Estudiar", "alta")]

class Tareas:
    def __init__(self):
        self.tareas = []  # lista de tuplas (descripcion, prioridad)

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [t for t in self.tareas if t[1] == "alta"]

    def eliminar_completada(self, descripcion):
        self.tareas = [t for t in self.tareas if t[0] != descripcion]
t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())