# cargar_notas(85, 92, 110, 78, -5, 88)
#
#   ¿85 está entre 0 y 100?   Sí  -> guardo
#   ¿92 está entre 0 y 100?   Sí  -> guardo
#   ¿110 está entre 0 y 100?  No (110 > 100) -> descarto
#   ¿78 está entre 0 y 100?   Sí  -> guardo
#   ¿-5 está entre 0 y 100?   No (-5 < 0)    -> descarto
#   ¿88 está entre 0 y 100?   Sí  -> guardo
#
#   Lista de notas válidas: [85, 92, 78, 88]
#
#   promedio():
#     suma = 85 + 92 + 78 + 88 = 343
#     cantidad = 4
#     promedio = 343 / 4 = 85.75

class Calificador:
    def __init__(self):
        # Lista: guarda solo las notas válidas
        self.notas = []

    def validar_nota(self, nota):
        """Retorna True si 0 <= nota <= 100."""
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
     
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
       
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)


c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())