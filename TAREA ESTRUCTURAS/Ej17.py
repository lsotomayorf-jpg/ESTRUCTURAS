# agrupar_por_categoria(5, 15, 30, 70)
#   (niño < 13, adolescente 13-17, adulto 18-59, mayor 60+)
#
#   edad 5  -> 5 < 13          -> "niño"
#   edad 15 -> 13 <= 15 < 18   -> "adolescente"
#   edad 30 -> 18 <= 30 < 60   -> "adulto"
#   edad 70 -> 70 >= 60        -> "mayor"
#
#   Resultado:
#     {"niño": [5], "adolescente": [15], "adulto": [30], "mayor": [70]}

class AgrupadorEdades:
    def __init__(self):
        self.ultimo_grupo = {}  # guarda el último agrupamiento realizado

    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        grupos = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            grupos.setdefault(categoria, []).append(edad)
        self.ultimo_grupo = grupos
        return grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.ultimo_grupo.get(categoria, [])
        if not edades:
            return 0
        return sum(edades) / len(edades)
    
ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))
