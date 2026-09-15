# invertir_lista([1, 2, 3])
#
#   índices originales: [0]=1  [1]=2  [2]=3
#   recorro desde el último índice (2) hasta el primero (0):
#     tomo índice 2 -> 3 -> invertida = [3]
#     tomo índice 1 -> 2 -> invertida = [3, 2]
#     tomo índice 0 -> 1 -> invertida = [3, 2, 1]
#
#   Resultado: [3, 2, 1]

class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
      
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)
        return resultado
inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
