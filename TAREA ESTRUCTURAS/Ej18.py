# distancia_euclidiana((0, 0), (3, 4))
#
#   dx = 3 - 0 = 3
#   dy = 4 - 0 = 4
#   distancia = raíz(dx^2 + dy^2) = raíz(3^2 + 4^2) = raíz(9 + 16) = raíz(25)
#
#   Resultado: 5.0
#   (se guarda también en la lista self.distancias)

import math


class CalculadorDistancia:
    def __init__(self):
        self.distancias = []  # lista: guarda todas las distancias calculadas

    def distancia_euclidiana(self, p1, p2):
        """Recibe dos tuplas (x, y) y calcula la distancia euclidiana."""
        x1, y1 = p1
        x2, y2 = p2
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        """Reutiliza distancia_euclidiana para hallar el punto más cercano."""
        mas_cercano = None
        menor_distancia = None
        for punto in puntos:
            d = self.distancia_euclidiana(referencia, punto)
            if menor_distancia is None or d < menor_distancia:
                menor_distancia = d
                mas_cercano = punto
        return mas_cercano
cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))
