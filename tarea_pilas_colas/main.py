from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


# ------------------------- funciones de apoyo -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()                 # 1. LEER
            if pila.apilar(pasajero):                  # 2. LLAMAR
                print("  ✓ Apilado: ahora es el tope") # 3. MOSTRAR
        elif op == "2":
            pila.listar()
        elif op == "3":
            salio = pila.desapilar()                   # LLAMAR
            if salio is None:                          # MOSTRAR
                print("  La pila está vacía")
            else:
                print(f"  ✓ Salió: {salio.nombre}")
                nuevo = pila.ver_tope()
                if nuevo is None:
                    print("  La pila quedó vacía")
                else:
                    print(f"  Nuevo tope: {nuevo.nombre}")
        elif op == "4":
            tope = pila.ver_tope()
            if tope is None:
                print("  La pila está vacía")
            else:
                print(f"  Tope: {tope.nombre} ({tope.numero})")
        elif op == "5":
            numero = leer_entero("  N.º a buscar: ")   # LEER
            pos = pila.buscar(numero)                  # LLAMAR
            if pos == -1:                              # MOSTRAR
                print("  No existe")
            else:
                print(f"  Encontrado en [{pos}]: {pila.datos[pos].nombre}")
        elif op == "6":
            numero = leer_entero("  N.º a modificar: ")
            nuevo_destino = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if pila.modificar(numero, nuevo_destino, nuevo_asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe ese número")
        elif op == "7":
            numero = leer_entero("  N.º a eliminar: ")
            if pila.eliminar_por_numero(numero):
                print("  ✓ Pasajero eliminado")
            else:
                print("  No existe ese número")
        elif op == "8":
            copia = pila.copiar()
            print("  ✓ Copia creada. Contenido de la copia:")
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {pila.longitud()}")
            if pila.esta_vacia():
                print("  La pila está vacía")
            else:
                print("  La pila no está vacía")
        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            print("  ✓ Datos de prueba apilados")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()                 # 1. LEER
            if cola.encolar(pasajero):                 # 2. LLAMAR
                print("  ✓ Encolado: está al final")   # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "3":
            salio = cola.desencolar()                  # LLAMAR
            if salio is None:                          # MOSTRAR
                print("  La cola está vacía")
            else:
                print(f"  ✓ Salió: {salio.nombre}")
                nuevo = cola.ver_frente()
                if nuevo is None:
                    print("  La cola quedó vacía")
                else:
                    print(f"  Nuevo frente: {nuevo.nombre}")
        elif op == "4":
            frente = cola.ver_frente()
            if frente is None:
                print("  La cola está vacía")
            else:
                print(f"  Frente: {frente.nombre} ({frente.numero})")
        elif op == "5":
            numero = leer_entero("  N.º a buscar: ")
            pos = cola.buscar(numero)
            if pos == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{pos}]: {cola.datos[pos].nombre}")
        elif op == "6":
            numero = leer_entero("  N.º a modificar: ")
            nuevo_destino = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if cola.modificar(numero, nuevo_destino, nuevo_asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe ese número")
        elif op == "7":
            numero = leer_entero("  N.º a eliminar: ")
            if cola.eliminar_por_numero(numero):
                print("  ✓ Pasajero eliminado")
            else:
                print("  No existe ese número")
        elif op == "8":
            copia = cola.copiar()
            print("  ✓ Copia creada. Contenido de la copia:")
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {cola.longitud()}")
            if cola.esta_vacia():
                print("  La cola está vacía")
            else:
                print("  La cola no está vacía")
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            print("  ✓ Datos de prueba encolados")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
