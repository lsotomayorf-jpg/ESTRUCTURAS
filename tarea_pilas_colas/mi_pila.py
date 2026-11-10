from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # = añadir de MiLista
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        # Mejora: no se permiten números repetidos (se usa buscar)
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- recorre SIEMPRE del tope al fondo -------
    def desapilar(self):
        # Solo puede salir el tope. Si está vacía no hay nada que sacar.
        if self.cantidad == 0:
            return None
        pasajero = self.datos[self.cantidad - 1]      # guardo el tope
        self.datos[self.cantidad - 1] = None          # dejo ese cajón vacío (no se corre nada)
        self.cantidad = self.cantidad - 1
        return pasajero

    def ver_tope(self):
        # Retorna el tope sin sacarlo
        if self.cantidad == 0:
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        # Búsqueda lineal empezando por el tope y bajando hasta el fondo
        for i in range(self.cantidad - 1, -1, -1):
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
        # No se puede sacar del medio: desapilo hacia una pila auxiliar
        # hasta encontrarlo, lo descarto y devuelvo los demás a esta pila.
        if self.buscar(numero) == -1:
            return False
        aux = MiPila(self.capacidad)
        encontrado = False
        while self.cantidad > 0 and not encontrado:
            pasajero = self.desapilar()
            if pasajero.numero == numero:
                encontrado = True                     # este se descarta
            else:
                aux.apilar(pasajero)
        # Vuelvo a apilar lo de la auxiliar: así el orden original queda igual
        while aux.cantidad > 0:
            self.apilar(aux.desapilar())
        return encontrado

    def copiar(self):
        # Apilo del fondo (0) al tope (cantidad-1) para que el tope siga siendo el mismo
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva.apilar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
