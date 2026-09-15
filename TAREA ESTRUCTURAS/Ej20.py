# agrupar_por_longitud("el gato está aquí")
#
#   separo el texto por espacios (split):
#     ["el", "gato", "está", "aquí"]
#
#   mido la longitud de cada palabra:
#     "el"   -> 2 letras
#     "gato" -> 4 letras
#     "está" -> 4 letras
#     "aquí" -> 4 letras
#
#   agrupo por longitud:
#     {2: ["el"], 4: ["gato", "está", "aquí"]}
#
#   palabras_unicas() (con set, sin repetidos):
#     {"el", "gato", "está", "aquí"}

class AnalizadorPatrones:
    def __init__(self):
        self.todas_palabras = []  # lista: acumula todas las palabras vistas

    def _registrar_palabras(self, texto):
        """Guarda las palabras del texto en self.todas_palabras (uso interno)."""
        for palabra in texto.split():
            self.todas_palabras.append(palabra)

    def encontrar_palabras(self, texto, patron):
        """Retorna una lista con palabras que inician con el patrón."""
        self._registrar_palabras(texto)
        return [p for p in texto.split() if p.startswith(patron)]

    def agrupar_por_longitud(self, texto):
        """Retorna {longitud: [palabras]}."""
        self._registrar_palabras(texto)
        grupos = {}
        for palabra in texto.split():
            grupos.setdefault(len(palabra), []).append(palabra)
        return grupos

    def palabras_unicas(self):
        """Retorna un conjunto con todas las palabras únicas vistas hasta ahora."""
        return set(self.todas_palabras)



ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato está aquí"))
print(ap.palabras_unicas())