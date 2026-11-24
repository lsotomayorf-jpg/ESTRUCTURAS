# ==============================================================
#  pasajero.py  ·  La clase Pasajero
# --------------------------------------------------------------
#  Cada reserva del vuelo es un objeto Pasajero.
#  La lista enlazada guarda un Pasajero dentro de cada Nodo
#  (en nodo.data).
# ==============================================================

from vuelo import clase_de_asiento     # función que dice si un asiento es Ejecutiva o Económica


class Pasajero:
    """Un pasajero con su reserva en el vuelo AL-204."""

    # El CONSTRUCTOR se ejecuta al crear un objeto: Pasajero(1005, "Diana", ...)
    # self es "el objeto que se está creando"; guardamos cada dato en él.
    def __init__(self, numero, nombre, cedula, edad, asiento):
        self.numero = numero      # int → 1005          (número de reserva: ÚNICO)
        self.nombre = nombre      # str → "Diana"
        self.cedula = cedula      # str → "0923456789"  (texto: así no se pierde el 0 inicial)
        self.edad = edad          # int → 22
        self.asiento = asiento    # str → "3C"          (fila + letra)

    def clase(self):
        """Retorna 'Ejecutiva' (filas 1-2) o 'Económica' (filas 3-12)."""
        return clase_de_asiento(self.asiento)

    def es_menor_de_edad(self):
        """True si tiene menos de 18 años."""
        return self.edad < 18

    def a_diccionario(self):
        """Convierte el objeto en un dict.
        Así se puede guardar en el JSON y enviar al navegador
        (un objeto no se puede convertir a JSON; un dict sí)."""
        return {
            "numero": self.numero,
            "nombre": self.nombre,
            "cedula": self.cedula,
            "edad": self.edad,
            "asiento": self.asiento,
        }

    def __str__(self):
        """Lo que se muestra al hacer print(pasajero).
        {self.nombre:<8} = alineado a la izquierda en 8 espacios (para que quede en columna)."""
        return (f"#{self.numero} | {self.nombre:<8} | {self.cedula} | "
                f"{self.edad:>2} años | asiento {self.asiento:<3} | {self.clase()}")
