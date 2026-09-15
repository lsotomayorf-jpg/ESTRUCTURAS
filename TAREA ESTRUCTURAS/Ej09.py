# contar_por_tipo("Hola123")
#
#   recorro carácter por carácter:
#     'H' -> ¿dígito? No. ¿letra? Sí. ¿vocal (aeiou)? No  -> consonante
#     'o' -> ¿dígito? No. ¿letra? Sí. ¿vocal? Sí           -> vocal
#     'l' -> ¿dígito? No. ¿letra? Sí. ¿vocal? No           -> consonante
#     'a' -> ¿dígito? No. ¿letra? Sí. ¿vocal? Sí           -> vocal
#     '1' -> ¿dígito? Sí                                    -> dígito
#     '2' -> ¿dígito? Sí                                    -> dígito
#     '3' -> ¿dígito? Sí                                    -> dígito
#
#   Conteo final: vocales: 2   consonantes: 2   dígitos: 3

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""  # guarda el texto más largo analizado

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        conteo = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
        for caracter in texto:
            if caracter.isdigit():
                conteo['digitos'] += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    conteo['vocales'] += 1
                else:
                    conteo['consonantes'] += 1
        return conteo
astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))