# intercalar([1, 2], [3, 4])
#
#   i = 0 -> tomo lista1[0]=1 -> resultado=[1]
#            tomo lista2[0]=3 -> resultado=[1, 3]
#   i = 1 -> tomo lista1[1]=2 -> resultado=[1, 3, 2]
#            tomo lista2[1]=4 -> resultado=[1, 3, 2, 4]
#
#   Resultado: [1, 3, 2, 4]

class CombinadorListas:
    def intercalar(self, lista1, lista2):
        """Alterna elementos de lista1 y lista2."""
        resultado = []
        largo = max(len(lista1), len(lista2))
        for i in range(largo):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        """Reutiliza intercalar para combinar varias listas de a dos."""
        if not listas:
            return []
        resultado = list(listas[0])
        for lista in listas[1:]:
            resultado = self.intercalar(resultado, lista)
        return resultado


cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))
