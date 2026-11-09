from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


# ------------------------- funciones -------------------------
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


def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"))
    lista.añadir(Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"))
    lista.añadir(Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    lista.añadir(Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"))
    lista.añadir(Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"))
    print("  ✓ Datos de prueba cargados")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir           2. Listar            3. Insertar en posición")
    print(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar")
    print(" 7. Eliminar por posición                 8. Eliminar por número")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar por destino                  15. Mayores de edad")
    print(" C. Cargar datos de prueba                0. Volver")


def mostrar_busqueda(lista, pos):
    """Muestra el resultado de una búsqueda (posición o -1)."""
    if pos == -1:
        print("  No existe")
    else:
        pasajero = lista.datos[pos] if hasattr(lista, "datos") else lista.pasajeros[pos]
        print(f"  Encontrado en [{pos}]: {pasajero.nombre}")


# ---------------------- MENÚ 1  ----------------------
def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 ")
        op = input("Opción: ").strip().upper()

        if op == "1":                                 
            pasajero = leer_pasajero()                
            if lista1.añadir(pasajero):               
                print("  ✓ Pasajero añadido")        
        elif op == "2":
            lista1.listar()
        elif op == "3":
            pos = leer_entero("  Posición: ")                 
            pasajero = leer_pasajero()
            if lista1.insertar(pos, pasajero):                     
                print(f"  ✓ Pasajero insertado en [{pos}]")       
        elif op == "4":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            mostrar_busqueda(lista1, lista1.buscar(numero))
        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            print("  (la lista debe estar ordenada: usa antes la opción 9)")
            mostrar_busqueda(lista1, lista1.buscar_binaria(numero))
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if lista1.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")
        elif op == "7":
            pos = leer_entero("  Posición a eliminar: ")
            eliminado = lista1.eliminar_por_posicion(pos)
            if eliminado is None:
                print(f"  ⚠ Posición inválida (hay {lista1.longitud()} pasajeros)")
            else:
                print(f"  ✓ Eliminado: {eliminado.nombre}; quedan {lista1.longitud()}")
        elif op == "8":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if lista1.eliminar_por_valor(numero):
                print(f"  ✓ Pasajero {numero} eliminado; quedan {lista1.longitud()}")
            else:
                print("  No existe")
        elif op == "9":
            lista1.ordenar_asc()
            print("  ✓ Ordenada de menor a mayor")
            lista1.listar()
        elif op == "10":
            lista1.ordenar_desc()
            print("  ✓ Ordenada de mayor a menor")
            lista1.listar()
        elif op == "11":
            lista1.reversar()
            print("  ✓ Lista reversada")
            lista1.listar()
        elif op == "12":
            copia = lista1.copiar()
            copia.reversar()
            print("  Copia (reversada):")
            copia.listar()
            print("  Original (no cambia):")
            lista1.listar()
        elif op == "13":
            print(f"  Hay {lista1.longitud()} pasajeros")
        elif op == "C":
            cargar_datos_prueba(lista1)
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2  ----------------------
def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 ", extras=True)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista2.añadir(pasajero):
                print("  ✓ Pasajero añadido")
        elif op == "2":
            lista2.listar()
        elif op == "3":
            pos = leer_entero("  Posición: ")
            pasajero = leer_pasajero()
            if lista2.insertar(pos, pasajero):
                print(f"  ✓ Pasajero insertado en [{pos}]")
        elif op == "4":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            mostrar_busqueda(lista2, lista2.buscar(numero))
        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            print("  (la lista debe estar ordenada: usa antes la opción 9)")
            mostrar_busqueda(lista2, lista2.buscar_binaria(numero))
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if lista2.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")
        elif op == "7":
            pos = leer_entero("  Posición a eliminar: ")
            eliminado = lista2.eliminar_por_posicion(pos)
            if eliminado is None:
                print(f"  ⚠ Posición inválida (hay {lista2.longitud()} pasajeros)")
            else:
                print(f"  ✓ Eliminado: {eliminado.nombre}; quedan {lista2.longitud()}")
        elif op == "8":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if lista2.eliminar_por_valor(numero):
                print(f"  ✓ Pasajero {numero} eliminado; quedan {lista2.longitud()}")
            else:
                print("  No existe")
        elif op == "9":
            lista2.ordenar_asc()
            print("  ✓ Ordenada de menor a mayor")
            lista2.listar()
        elif op == "10":
            lista2.ordenar_desc()
            print("  ✓ Ordenada de mayor a menor")
            lista2.listar()
        elif op == "11":
            lista2.reversar()
            print("  ✓ Lista reversada")
            lista2.listar()
        elif op == "12":
            copia = lista2.copiar()
            copia.reversar()
            print("  Copia (reversada):")
            copia.listar()
            print("  Original (no cambia):")
            lista2.listar()
        elif op == "13":
            print(f"  Hay {lista2.longitud()} pasajeros")
        elif op == "14":
            destino = input("  Destino a filtrar: ").strip()
            filtrados = lista2.filtrar_por_destino(destino)
            if not filtrados:
                print("  No hay pasajeros con ese destino")
            else:
                for p in filtrados:
                    print(f"  {p}")
        elif op == "15":
            mayores = lista2.mayores_de_edad()
            if not mayores:
                print("  No hay pasajeros mayores de edad")
            else:
                for p in mayores:
                    print(f"  {p}")
        elif op == "C":
            cargar_datos_prueba(lista2)
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS ✈ =====")
        print("1. Menú 1 ")
        print("2. Menú 2 ")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
