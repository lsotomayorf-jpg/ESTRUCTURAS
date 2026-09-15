# separar(1, 2, 3, 4, 5)
#
#   ¿1 es par? 1 % 2 = 1 -> No -> impar
#   ¿2 es par? 2 % 2 = 0 -> Sí -> par
#   ¿3 es par? 3 % 2 = 1 -> No -> impar
#   ¿4 es par? 4 % 2 = 0 -> Sí -> par
#   ¿5 es par? 5 % 2 = 1 -> No -> impar
#
#   Resultado:
#     pares:   [2, 4]
#     impares: [1, 3, 5]
#
#   cantidad_pares_impares() = (2, 3)

class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        self.pares = []
        self.impares = []
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        return {'pares': self.pares, 'impares': self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))
an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))