# ==============================================================
#  revisar.py  ·  Revisa lo que RETORNAN tus métodos
# --------------------------------------------------------------
#  Antes de enviar un resultado al navegador, app.py lo pasa por
#  estas funciones. Si algo no cuadra, lanzan ErrorEnTuMetodo con
#  un mensaje que te dice qué corregir.
# ==============================================================
from lista_pasajeros import Nodo
from pasajero import Pasajero


class ErrorEnTuMetodo(Exception):
    """Un error 'nuestro': un método retornó algo de un tipo que no corresponde."""


def pasajero_o_none(valor, metodo):
    """Para buscar, buscar_por_asiento, buscar_por_cedula y eliminar."""
    if valor is None or isinstance(valor, Pasajero):    # isinstance: ¿es de esta clase?
        return valor                                    # ✅ está bien
    if isinstance(valor, Nodo):
        raise ErrorEnTuMetodo(f"{metodo}() retornó un Nodo. Retorna el pasajero: actual.data")
    raise ErrorEnTuMetodo(f"{metodo}() debe retornar un Pasajero o None, "
                          f"pero retornó {type(valor).__name__}: {valor!r}")


def lista_de_pasajeros(valor, metodo):
    """Para listar y filtrar_por_clase: debe ser una list de Pasajero."""
    if valor is None:
        raise ErrorEnTuMetodo(f"{metodo}() retornó None. ¿Olvidaste el  return resultado ?")
    if not isinstance(valor, list):
        raise ErrorEnTuMetodo(f"{metodo}() debe retornar una list, pero retornó {type(valor).__name__}")
    for elemento in valor:
        if isinstance(elemento, Nodo):
            raise ErrorEnTuMetodo(f"{metodo}() guardó Nodos en la lista. Guarda el pasajero: actual.data")
        if not isinstance(elemento, Pasajero):
            raise ErrorEnTuMetodo(f"{metodo}() debe guardar objetos Pasajero, pero encontré "
                                  f"{type(elemento).__name__}: {elemento!r}")
    return valor


def booleano(valor, metodo):
    """Para esta_vacia y modificar: debe ser True o False."""
    if valor is True or valor is False:
        return valor
    raise ErrorEnTuMetodo(f"{metodo}() debe retornar True o False, pero retornó {valor!r}")


def entero(valor, metodo):
    """Para longitud: debe ser un número entero."""
    if isinstance(valor, int) and not isinstance(valor, bool):
        return valor
    raise ErrorEnTuMetodo(f"{metodo}() debe retornar un número entero, pero retornó {valor!r}")
