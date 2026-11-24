# ==============================================================
#  persistencia.py  ·  Guardar y leer las reservas en JSON
# --------------------------------------------------------------
#    RAM (se borra)                           DISCO (permanece)
#    head -> [1005] -> [1002] -> None   --guardar-->   data/reservas.json
#                                       <--cargar---
# ==============================================================
import json      # librería de Python para leer y escribir JSON
import os        # librería para trabajar con rutas de archivos y carpetas

from pasajero import Pasajero

# Rutas de los archivos. os.path.join une partes de una ruta con la barra correcta
# (\ en Windows, / en Mac). __file__ es la ruta de ESTE archivo.
CARPETA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
ARCHIVO = os.path.join(CARPETA, "reservas.json")     # las reservas reales
EJEMPLO = os.path.join(CARPETA, "ejemplo.json")      # copia de seguridad (datos de prueba)

siguiente_numero = 1001          # el próximo número de reserva que se entregará


def cargar(lista, ruta=ARCHIVO):
    """Lee el JSON y mete cada reserva al FINAL de la lista con ingresar()."""
    global siguiente_numero      # global: vamos a cambiar la variable de afuera de la función
    if not os.path.exists(ruta):                 # la primera vez aún no existe reservas.json...
        ruta = EJEMPLO                           # ...entonces usamos los datos de prueba
    # with open(...) abre el archivo y lo cierra solo al terminar. "r" = leer
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = json.load(archivo)           # texto JSON → dict de Python

    for d in contenido["reservas"]:              # cada d es un dict con los 5 datos
        pasajero = Pasajero(d["numero"], d["nombre"], d["cedula"], d["edad"], d["asiento"])
        lista.ingresar(pasajero)                 # ✅ el ingresar de tu lista enlazada

    siguiente_numero = contenido["siguiente_numero"]


def guardar(lista):
    """Recorre la lista enlazada (head → None) y escribe todo en el JSON."""
    reservas = []
    actual = lista.head                          # el dedo en la cabeza
    while actual is not None:                    # mientras haya vagón...
        reservas.append(actual.data.a_diccionario())   # ...guardo su pasajero como dict
        actual = actual.next                     # ...y avanzo
        if len(reservas) > 1000:                 # seguro: un avión no tiene 1000 asientos
            raise RuntimeError("La lista no termina nunca: ¿un nodo se apunta a sí mismo?")

    contenido = {"siguiente_numero": siguiente_numero, "reservas": reservas}
    os.makedirs(CARPETA, exist_ok=True)          # crea data/ si no existe
    # "w" = escribir (borra lo anterior). indent=2 = bonito y legible.
    # ensure_ascii=False = guarda las tildes tal cual (Sofía y no Sofía)
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, ensure_ascii=False, indent=2)   # dict → texto JSON


def nuevo_numero():
    """Entrega un número de reserva que nunca se ha usado: 1013, 1014, ..."""
    global siguiente_numero
    numero = siguiente_numero
    siguiente_numero = siguiente_numero + 1
    return numero


def restaurar(lista):
    """Vuelve a los 12 pasajeros de data/ejemplo.json."""
    lista.head = None             # soltar la cabeza = soltar todo el tren
    lista.cantidad = 0            # (Python borra solito los vagones que nadie apunta)
    cargar(lista, EJEMPLO)
    guardar(lista)
