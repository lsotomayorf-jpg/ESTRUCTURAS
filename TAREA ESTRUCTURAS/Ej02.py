# agregar_multiples("hola", "mundo", "hola")
#
#   agregar "hola"  - conjunto: {hola}            lista: [hola]
#   agregar "mundo" - conjunto: {hola, mundo}      lista: [hola, mundo]
#   agregar "hola" otra vez -
#       ¿ya está en el conjunto? Sí - el conjunto NO cambia
#       conjunto: {hola, mundo}     lista: [hola, mundo, hola]
#
#   contar_palabras() = len(conjunto) = 2

class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()   # conjunto: evita duplicados
        self.orden = []                # lista: conserva el orden de ingreso

    def agregar_palabra(self, palabra):
     
        self.palabras_unicas.add(palabra)
        self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)
at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())