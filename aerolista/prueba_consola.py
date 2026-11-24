# ==============================================================
#  prueba_consola.py  ·  Prueba tus métodos SIN Flask
#      python prueba_consola.py
#  Cada vez que termines un método, quita el # de sus líneas
#  y vuelve a ejecutar este archivo.
# ==============================================================
from lista_pasajeros import ListaPasajeros
from pasajero import Pasajero

lista = ListaPasajeros()                  # una lista vacía: head = None
lista.ingresar(Pasajero(1005, "Diana", "0923456789", 22, "3C"))   # ✅ ingresar ya funciona
lista.ingresar(Pasajero(1002, "Ana", "0912345678", 28, "1A"))
lista.ingresar(Pasajero(1009, "Luis", "0987654321", 35, "7D"))
lista.ingresar(Pasajero(1004, "Beto", "0934567890", 16, "7E"))
print("ingresar OK: 4 pasajeros ingresados, cantidad =", lista.cantidad)

# --- descomenta a medida que avances (lo que debería salir está a la derecha) ---
# print("esta_vacia:", lista.esta_vacia())                 # False
# print("longitud:", lista.longitud())                     # 4
# for pasajero in lista.listar():                          # Diana, Ana, Luis, Beto
#     print("   ", pasajero)
# print("buscar 1009:", lista.buscar(1009))                # Luis
# print("buscar 9999:", lista.buscar(9999))                # None
# print("asiento 7E:", lista.buscar_por_asiento("7E"))     # Beto
# print("cedula de Ana:", lista.buscar_por_cedula("0912345678"))
# print("modificar:", lista.modificar(1009, "Luis A.", 36, "9F"))   # True
# print("eliminar cabeza:", lista.eliminar(1005))          # Diana
# print("eliminar 9999:", lista.eliminar(9999))            # None
# print("ejecutiva:", [str(p) for p in lista.filtrar_por_clase("Ejecutiva")])
