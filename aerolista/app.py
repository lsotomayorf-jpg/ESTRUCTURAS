# ==============================================================
#  app.py  ·  El servidor de AeroLista
#  Desde ahora, cada paso agrega sus rutas nuevas ENCIMA de la
#  línea que dice ENCENDER EL SERVIDOR (casi al final del archivo).
# ==============================================================

import traceback                       # 🆕 (paso 28) muestra errores completos en la terminal

# Flask:           crea la aplicación
# jsonify:         🆕 convierte un dict de Python en una respuesta JSON
# render_template: busca un archivo dentro de templates/ y lo entrega
# request:         🆕 (paso 29) permite leer lo que nos manda el navegador
from flask import Flask, jsonify, render_template, request
from werkzeug.exceptions import HTTPException   # 🆕 (paso 28) errores web como "404 no existe"

import verificador                               # 🆕 pruebas automáticas (panel de progreso)
import revisar                                   # 🆕 revisa lo que retornan tus métodos
import persistencia                              # 🆕 guarda y lee el archivo JSON
from lista_pasajeros import ListaPasajeros       # 🆕 la lista enlazada
from pasajero import Pasajero                    # 🆕 la clase Pasajero (la usaremos en el paso 29)
from vuelo import VUELO, asiento_existe, total_asientos   # 🆕 más funciones de vuelo.py

# 🆕 La ÚNICA lista enlazada del programa. Vive en la memoria mientras Flask esté encendido.
lista = ListaPasajeros()
persistencia.cargar(lista)        # lee data/reservas.json y hace ingresar() con cada reserva
print(f"  Reservas cargadas en la lista enlazada: {lista.cantidad}")

app = Flask(__name__)


@app.get("/")
def inicio():
    # 🆕 render_template hace 3 cosas:
    #    1. busca templates/index.html
    #    2. reemplaza cada {{ vuelo.algo }} con el dato de este diccionario
    #       (por ejemplo {{ vuelo.origen }} → "Guayaquil")
    #    3. envía el HTML ya completo al navegador
    return render_template("index.html", vuelo=VUELO)


# ==============================================================
#  RESPUESTAS DE LA API: todas tienen la misma forma
#     { "ok": true/false, "datos": ..., "mensaje": "...", "avisos": [...] }
# ==============================================================
def respuesta_ok(datos=None, mensaje="", avisos=None, codigo=200):
    """Respuesta de ÉXITO. codigo 200 = 'todo bien' (201 = 'creado')."""
    return jsonify({
        "ok": True,                 # salió bien
        "datos": datos,             # lo que pidió el navegador
        "mensaje": mensaje,         # un texto para mostrar al usuario
        "avisos": avisos or [],     # advertencias opcionales (si no hay, lista vacía)
    }), codigo


def respuesta_error(mensaje, codigo=400):
    """Respuesta de ERROR. 400 = datos incorrectos · 404 = no existe."""
    return jsonify({"ok": False, "mensaje": mensaje}), codigo


# ==============================================================
#  API: rutas que responden JSON (las llama el JavaScript)
# ==============================================================
@app.get("/api/vuelo")
def ver_vuelo():
    """Datos del avión: el JavaScript los usa para DIBUJAR filas y asientos."""
    return respuesta_ok(VUELO)      # el diccionario VUELO viaja como JSON

def a_diccionarios(pasajeros):
    """[Pasajero, Pasajero, ...]  →  [dict, dict, ...]  (para poder enviarlos como JSON)."""
    resultado = []
    for pasajero in pasajeros:
        resultado.append(pasajero.a_diccionario())
    return resultado


@app.get("/api/resumen")
def ver_resumen():
    """Tablero: cuántas reservas hay y si la lista está vacía."""
    cantidad = revisar.entero(lista.longitud(), "longitud")            # ✍ TU método
    vacia = revisar.booleano(lista.esta_vacia(), "esta_vacia")         # ✍ TU método
    return respuesta_ok({"cantidad": cantidad, "vacia": vacia, "total_asientos": total_asientos()})


@app.get("/api/reservas")
def listar_reservas():
    """LISTAR todas las reservas, o solo una clase si llega ?clase=Ejecutiva"""
    # request.args son los datos que vienen en la dirección después del ?
    clase = request.args.get("clase", "")          # si no viene, vale ""
    if clase == "":
        pasajeros = revisar.lista_de_pasajeros(lista.listar(), "listar")                    # ✍ TU método
    else:
        pasajeros = revisar.lista_de_pasajeros(lista.filtrar_por_clase(clase), "filtrar_por_clase")   # ✍
    return respuesta_ok(a_diccionarios(pasajeros))


@app.get("/api/reservas/<int:numero>")
def buscar_reserva(numero):
    """BUSCAR por número. <int:numero> toma ese pedazo de la dirección y lo vuelve int:
    /api/reservas/1009  →  numero = 1009"""
    pasajero = revisar.pasajero_o_none(lista.buscar(numero), "buscar")                       # ✍
    if pasajero is None:
        return respuesta_error(f"No existe la reserva #{numero}", 404)    # 404 = no existe
    return respuesta_ok(pasajero.a_diccionario(), f"Reserva #{numero} encontrada")


@app.get("/api/asientos/<asiento>")
def buscar_asiento(asiento):
    """¿Quién está sentado en este asiento? (clic en un asiento rojo)"""
    asiento = asiento.upper()                       # "7d" → "7D"
    pasajero = revisar.pasajero_o_none(lista.buscar_por_asiento(asiento), "buscar_por_asiento")  # ✍
    if pasajero is None:
        return respuesta_ok(None, f"El asiento {asiento} está libre")      # libre NO es un error
    return respuesta_ok(pasajero.a_diccionario(), f"En el {asiento} viaja {pasajero.nombre}")


@app.get("/api/cedulas/<cedula>")
def buscar_cedula(cedula):
    """BUSCAR por cédula."""
    pasajero = revisar.pasajero_o_none(lista.buscar_por_cedula(cedula), "buscar_por_cedula")    # ✍
    if pasajero is None:
        return respuesta_error(f"Ningún pasajero tiene la cédula {cedula}", 404)
    return respuesta_ok(pasajero.a_diccionario(), "Pasajero encontrado")


# ==============================================================
#  ERRORES: en vez de romperse, Flask responde un JSON que explica
#  qué pasó, y la página lo muestra en un mensaje.
# ==============================================================
@app.errorhandler(NotImplementedError)
def metodo_pendiente(error):
    """Un método todavía tiene su línea  raise NotImplementedError(...)"""
    metodo = str(error)                             # "listar"
    return jsonify({"ok": False, "pendiente": True, "metodo": metodo,
                    "mensaje": f"Falta implementar {metodo}() en lista_pasajeros.py"}), 501


@app.errorhandler(revisar.ErrorEnTuMetodo)
def metodo_con_problema(error):
    """Un método retornó algo que no corresponde (lo detectó revisar.py)"""
    return jsonify({"ok": False, "error_codigo": True, "mensaje": str(error)}), 500


@app.errorhandler(Exception)
def error_inesperado(error):
    """Cualquier otro error de Python (por ejemplo AttributeError en tu código)"""
    if isinstance(error, HTTPException):            # 404, 405...: rutas que no existen
        return jsonify({"ok": False, "mensaje": f"{error.code} {error.name}"}), error.code
    traceback.print_exc()                           # el detalle completo sale en la terminal
    return jsonify({"ok": False, "error_codigo": True,
                    "mensaje": f"Error en el código Python → {type(error).__name__}: {error}"}), 500

def leer_formulario():
    """Saca los datos que mandó el JavaScript (en formato JSON)."""
    datos = request.get_json(silent=True) or {}     # el cuerpo del pedido como dict (o {} si viene vacío)
    nombre = str(datos.get("nombre", "")).strip()   # .get(clave, valor_si_no_existe)
    cedula = str(datos.get("cedula", "")).strip()
    edad = str(datos.get("edad", "")).strip()
    asiento = str(datos.get("asiento", "")).strip().upper()
    return nombre, cedula, edad, asiento            # retorna 4 valores a la vez (una tupla)


def validar_campos(nombre, cedula, edad, asiento):
    """Revisa los datos. Retorna el problema (texto) o "" si todo está bien."""
    if len(nombre) < 2:
        return "Escribe el nombre del pasajero"
    if not (cedula.isdigit() and len(cedula) == 10):
        return "La cédula debe tener 10 dígitos"
    if not str(edad).isdigit() or int(edad) > 120:
        return "La edad debe ser un número entre 0 y 120"
    if not asiento_existe(asiento):                 # (vuelo.py)
        return f"El asiento '{asiento}' no existe en este avión"
    return ""


@app.post("/api/reservas")
def reservar():
    """AÑADIR: validar → crear Pasajero → ingresar → guardar JSON."""
    nombre, cedula, edad, asiento = leer_formulario()
    problema = validar_campos(nombre, cedula, edad, asiento)
    if problema != "":
        return respuesta_error(problema)            # 400 = datos incorrectos

    # ¿El asiento está libre? ¿La cédula es nueva? Esto usa TUS métodos de búsqueda.
    # Mientras no los programes, la reserva se hace igual pero SIN esta revisión (con un aviso).
    avisos = []
    try:                                            # try: intenta...
        if lista.buscar_por_asiento(asiento) is not None:                                       # ✍
            return respuesta_error(f"El asiento {asiento} ya está reservado")
    except NotImplementedError:                     # ...y si el método aún no existe:
        avisos.append("No se revisó si el asiento estaba libre: falta buscar_por_asiento()")
    try:
        if lista.buscar_por_cedula(cedula) is not None:                                         # ✍
            return respuesta_error(f"La cédula {cedula} ya tiene una reserva en este vuelo")
    except NotImplementedError:
        avisos.append("No se revisó si la cédula se repetía: falta buscar_por_cedula()")

    pasajero = Pasajero(persistencia.nuevo_numero(), nombre, cedula, int(edad), asiento)
    lista.ingresar(pasajero)                        # ✅ el método resuelto: engancha al final
    persistencia.guardar(lista)                     # 💾 escribe data/reservas.json
    mensaje = f"Reserva #{pasajero.numero} creada: {nombre} en el asiento {asiento}"
    return respuesta_ok(pasajero.a_diccionario(), mensaje, avisos, 201)   # 201 = creado


@app.put("/api/reservas/<int:numero>")
def modificar_reserva(numero):
    """MODIFICAR nombre, edad y/o asiento de una reserva."""
    nombre, cedula, edad, asiento = leer_formulario()
    pasajero = revisar.pasajero_o_none(lista.buscar(numero), "buscar")                        # ✍
    if pasajero is None:
        return respuesta_error(f"No existe la reserva #{numero}", 404)
    problema = validar_campos(nombre, pasajero.cedula, edad, asiento)   # la cédula no cambia
    if problema != "":
        return respuesta_error(problema)

    avisos = []
    try:
        ocupante = lista.buscar_por_asiento(asiento)                                            # ✍
        # el asiento nuevo debe estar libre... o ser el suyo (si no lo cambió)
        if ocupante is not None and ocupante.numero != numero:
            return respuesta_error(f"El asiento {asiento} ya es de {ocupante.nombre}")
    except NotImplementedError:
        avisos.append("No se revisó si el asiento nuevo estaba libre: falta buscar_por_asiento()")

    cambiado = revisar.booleano(lista.modificar(numero, nombre, int(edad), asiento), "modificar")  # ✍
    if not cambiado:
        return respuesta_error(f"No se pudo modificar la reserva #{numero}", 404)
    persistencia.guardar(lista)
    actualizado = lista.buscar(numero)
    return respuesta_ok(actualizado.a_diccionario(), f"Reserva #{numero} actualizada", avisos)


@app.delete("/api/reservas/<int:numero>")
def eliminar_reserva(numero):
    """ELIMINAR (cancelar) una reserva: el asiento vuelve a quedar libre."""
    eliminado = revisar.pasajero_o_none(lista.eliminar(numero), "eliminar")                   # ✍
    if eliminado is None:
        return respuesta_error(f"No existe la reserva #{numero}", 404)
    persistencia.guardar(lista)
    mensaje = f"Reserva #{numero} cancelada: el asiento {eliminado.asiento} quedó libre"
    return respuesta_ok(eliminado.a_diccionario(), mensaje)


@app.post("/api/restaurar")
def restaurar_datos():
    """Botón 'Datos de ejemplo' (paso 30): por si tu código dañó las reservas."""
    persistencia.restaurar(lista)
    return respuesta_ok(None, "Se restauraron las 12 reservas de ejemplo")

@app.get("/api/progreso")
def ver_progreso():
    """Panel 'Progreso del backend': prueba tus métodos con una lista de práctica."""
    return respuesta_ok(verificador.revisar_todo())

# ===== ENCENDER EL SERVIDOR =====
if __name__ == "__main__":
    app.run(debug=True, port=5050)
