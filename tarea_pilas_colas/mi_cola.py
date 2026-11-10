from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):                     # = añadir de MiLista
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        # Mejora: no se permiten números repetidos (se usa buscar)
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # EJEMPLO: del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):                # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- recorre SIEMPRE del frente al final -------
    def desencolar(self):
        # Siempre sale el frente (datos[0]) y todos se corren a la izquierda
        if self.cantidad == 0:
            return None
        pasajero = self.datos[0]
        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]         # cada uno avanza un lugar
        self.datos[self.cantidad - 1] = None          # el último cajón queda libre
        self.cantidad = self.cantidad - 1
        return pasajero

    def ver_frente(self):
        # Retorna el frente sin sacarlo
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        # Búsqueda lineal del frente al final
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)                     # reutilizo buscar
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        # No se puede sacar del medio: la fila da una vuelta completa.
        # Desencolo "cantidad" veces; si no es el buscado lo vuelvo a encolar.
        if self.buscar(numero) == -1:
            return False
        vueltas = self.cantidad                       # guardo el valor porque cantidad va cambiando
        encontrado = False
        for _ in range(vueltas):
            pasajero = self.desencolar()
            if pasajero.numero == numero:
                encontrado = True                     # este no vuelve a la fila
            else:
                self.encolar(pasajero)
        return encontrado

    def copiar(self):
        # Encolo del frente al final para mantener el mismo orden
        nueva = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva.encolar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
