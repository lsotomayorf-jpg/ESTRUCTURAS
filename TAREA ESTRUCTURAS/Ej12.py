# elementos_en_multiples_rangos((1, 3), (2, 4))
#
#   crear_rango(1, 3) -> (1, 2, 3)
#   crear_rango(2, 4) -> (2, 3, 4)
#
#   uno ambos en un conjunto (sin repetir):
#     {1, 2, 3} unión {2, 3, 4} = {1, 2, 3, 4}
#
#   ordeno el conjunto -> [1, 2, 3, 4]

class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()
        for inicio, fin in rangos:
            elementos.update(self.crear_rango(inicio, fin))
        return sorted(elementos)

sr = SelectorRango()
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))