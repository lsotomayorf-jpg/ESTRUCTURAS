# ==============================================================
#  vuelo.py  ·  Datos fijos del vuelo y del avión
# --------------------------------------------------------------
#  La app maneja UN solo vuelo. El avión tiene 12 filas:
#    - Filas 1 y 2  → clase Ejecutiva  (asientos A C | D F     → 4 por fila)
#    - Filas 3 a 12 → clase Económica  (asientos A B C | D E F → 6 por fila)
#    Total: 2 x 4 + 10 x 6 = 68 asientos.
#  Un asiento se escribe como fila + letra: "1A", "7D", "12F".
# ==============================================================

# Un diccionario con todos los datos. Las claves están entre comillas.
VUELO = {
    "codigo": "AL-204",                 # código del vuelo
    "aerolinea": "AeroLista",
    "origen": "Guayaquil",              # ciudad de salida
    "codigo_origen": "GYE",             # código del aeropuerto de salida
    "destino": "Quito",
    "codigo_destino": "UIO",
    "fecha": "2026-12-20",
    "hora": "07:30",
    "filas": 12,                                         # cuántas filas tiene el avión
    "filas_ejecutiva": 2,                                # las primeras 2 filas son Ejecutiva
    "letras_ejecutiva": ["A", "C", "D", "F"],            # asientos de una fila Ejecutiva
    "letras_economica": ["A", "B", "C", "D", "E", "F"],  # asientos de una fila Económica
    "filas_salida": [6, 7],             # filas junto a las salidas de emergencia (sobre las alas)
}


def total_asientos():
    """Calcula cuántos asientos tiene el avión (68)."""
    # filas de Ejecutiva x asientos por fila Ejecutiva
    ejecutiva = VUELO["filas_ejecutiva"] * len(VUELO["letras_ejecutiva"])
    # filas de Económica x asientos por fila Económica
    economica = (VUELO["filas"] - VUELO["filas_ejecutiva"]) * len(VUELO["letras_economica"])
    return ejecutiva + economica


def separar_asiento(asiento):
    """Separa '12A' en (12, 'A'). Si el texto no tiene forma de asiento, retorna (0, '')."""
    asiento = str(asiento).strip().upper()   # quitamos espacios y pasamos a mayúsculas
    if len(asiento) < 2:                     # "A" o "" no son asientos válidos
        return 0, ""
    fila_texto = asiento[:-1]                # todo menos la última letra  → "12"
    letra = asiento[-1]                      # solo la última letra        → "A"
    if not fila_texto.isdigit():             # "XA" no sirve: la fila debe ser un número
        return 0, ""
    return int(fila_texto), letra            # convertimos "12" en el número 12


def clase_de_asiento(asiento):
    """'1A' → 'Ejecutiva'   ·   '7D' → 'Económica'."""
    fila, letra = separar_asiento(asiento)
    if fila <= VUELO["filas_ejecutiva"]:
        return "Ejecutiva"
    return "Económica"


def asiento_existe(asiento):
    """True si el asiento existe en ESTE avión ('13A' o '1B' no existen)."""
    fila, letra = separar_asiento(asiento)
    if fila < 1 or fila > VUELO["filas"]:            # la fila está fuera del avión
        return False
    if fila <= VUELO["filas_ejecutiva"]:             # en Ejecutiva no hay B ni E
        return letra in VUELO["letras_ejecutiva"]
    return letra in VUELO["letras_economica"]
