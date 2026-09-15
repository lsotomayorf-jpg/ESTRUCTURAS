# agregar_stock("pan", 50)   -> stock = {"pan": 50}
# restar_stock("pan", 30):
#   ¿hay al menos 30 de "pan"? 50 >= 30 -> Sí
#   stock["pan"] = 50 - 30 = 20 -> stock = {"pan": 20}
#   retorna True
#
# productos_bajo_stock(15):
#   "pan" -> 20 < 15? No -> no entra en la lista
#
#   Resultado: []

class Inventario:
    def __init__(self):
        self.stock = {}  # diccionario {producto: cantidad}

    def agregar_stock(self, producto, cantidad):
        """Guarda/aumenta la cantidad de un producto en el diccionario."""
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        """Disminuye stock si hay suficiente; retorna True/False."""
        if self.stock.get(producto, 0) >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        """Retorna lista de productos con cantidad < minimo."""
        return [p for p, cant in self.stock.items() if cant < minimo]



invent = Inventario()
invent.agregar_stock("pan", 50)
print(invent.restar_stock("pan", 30))
print(invent.productos_bajo_stock(15))
