# registrar_multiples(20, 25, 18, 30)
#
#   lista de temperaturas: [20, 25, 18, 30]
#
#   minima()  -> el menor valor de la lista = 18
#   maxima()  -> el mayor valor de la lista = 30
#   promedio():
#     suma = 20 + 25 + 18 + 30 = 93
#     cantidad = 4
#     promedio = 93 / 4 = 23.25

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []  # lista de temperaturas registradas

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        if not self.temperaturas:
            raise ValueError("No hay temperaturas registradas")
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)
gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.promedio())