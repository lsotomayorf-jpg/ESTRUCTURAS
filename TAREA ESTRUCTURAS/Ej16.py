# codificar_palabra("hola", 3)
#   (a=0, b=1, c=2 ... z=25 dentro del alfabeto)
#
#   'h' -> posición 7  -> (7+3) % 26 = 10  -> 'k'
#   'o' -> posición 14 -> (14+3) % 26 = 17 -> 'r'
#   'l' -> posición 11 -> (11+3) % 26 = 14 -> 'o'
#   'a' -> posición 0  -> (0+3) % 26 = 3   -> 'd'
#
#   palabra codificada: "krod"
#   historial -> {"hola": "krod"}

class CodificadorCesar:
    def __init__(self):
        self.historial = {}  # diccionario {palabra_original: palabra_codificada}

    def codificar_letra(self, letra, desplazamiento):
       
        if not letra.isalpha():
            return letra
        base = ord('A') if letra.isupper() else ord('a')
        posicion = ord(letra) - base
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(base + nueva_posicion)

    def codificar_palabra(self, palabra, desplazamiento):
   
        codificada = ""
        for letra in palabra:
            codificada += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = codificada
        return codificada
cc = CodificadorCesar()
print(cc.codificar_palabra("perro", 3))