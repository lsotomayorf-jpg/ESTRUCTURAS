# encontrar_divisores(12)
#
#   ¿12 divisible por 1?   Sí
#   ¿12 divisible por 2?   Sí
#   ¿12 divisible por 3?   Sí
#   ¿12 divisible por 4?   Sí
#   ¿12 divisible por 5?   No
#   ¿12 divisible por 6?   Sí
#   ¿12 divisible por 7 al 11? No (ninguno)
#   ¿12 divisible por 12?  Sí
#
#   Resultado: (1, 2, 3, 4, 6, 12)
#
#   es_perfecto(12):
#     suma sin el mismo = 1+2+3+4+6 = 16 -> 16 != 12 -> No es perfecto

class DivisorFinder:
    def encontrar_divisores(self, numero):
        """Retorna una tupla con todos los divisores del número."""
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        """True si la suma de sus divisores (sin contar él mismo) es igual a numero."""
        divisores = self.encontrar_divisores(numero)
        suma = sum(divisores) - numero
        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        """Retorna {numero: tupla_divisores} reutilizando encontrar_divisores."""
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado
df = DivisorFinder()
print(df.encontrar_divisores(12))