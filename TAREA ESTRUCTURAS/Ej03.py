# agregar_articulo("pan", 2.50)
# agregar_articulo("leche", 3.00)
#
#   diccionario después de agregar:
#     {"pan": 2.50, "leche": 3.00}
#
#   total_carrito():
#     suma los valores -> 2.50 + 3.00 = 5.50

class CarroCompras:
    def __init__(self):
        self.articulos = {}  # diccionario {nombre: precio}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado
carro = CarroCompras()
carro.agregar_articulo("pan", 4.50)
carro.agregar_articulo("leche", 3.00)
print(carro.total_carrito())
