# agregar_elemento("a")  -> frecuencias = {"a": 1}
# agregar_elemento("b")  -> frecuencias = {"a": 1, "b": 1}
# agregar_elemento("a")  -> frecuencias = {"a": 2, "b": 1}
#
#   elemento_mas_frecuente():
#     comparo los valores del diccionario
#     "a" tiene 2, "b" tiene 1 -> el mayor es "a"
#
#   Resultado: "a"

class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}  # diccionario {elemento: cantidad}

    def agregar_elemento(self, elemento):
        self.frecuencias[elemento] = self.frecuencias.get(elemento, 0) + 1

    def elemento_mas_frecuente(self):
        if not self.frecuencias:
            return None
        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())
