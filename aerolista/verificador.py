# ==============================================================
#  verificador.py  ·  Pruebas automáticas de tus métodos
# --------------------------------------------------------------
#  Corre pruebas sobre una lista de PRÁCTICA (no toca tus reservas
#  reales) y arma el panel "Progreso del backend" de la página.
#  Estados: ok ✅ · pendiente 🚧 · fallo ❌ · error 💥 · lento ⏳
# ==============================================================
import threading      # para correr cada prueba en un "hilo" aparte con tiempo límite

from lista_pasajeros import ListaPasajeros
from pasajero import Pasajero
from revisar import ErrorEnTuMetodo, booleano, lista_de_pasajeros, pasajero_o_none


class Fallo(Exception):
    """La prueba corrió, pero el resultado no es el esperado."""


def esperar(condicion, mensaje):
    """Si la condición es falsa, la prueba falla con ese mensaje."""
    if not condicion:
        raise Fallo(mensaje)


def lista_de_prueba():
    """head → [1 Ana 1A] → [2 Beto 3C] → [3 Carla 5D] → [4 Dani 2C] → None"""
    lista = ListaPasajeros()
    lista.ingresar(Pasajero(1, "Ana", "0000000001", 30, "1A"))
    lista.ingresar(Pasajero(2, "Beto", "0000000002", 15, "3C"))
    lista.ingresar(Pasajero(3, "Carla", "0000000003", 40, "5D"))
    lista.ingresar(Pasajero(4, "Dani", "0000000004", 22, "2C"))
    return lista


def cadena(lista):
    """Lee los números caminando los nodos (sin usar tus métodos)."""
    numeros = []
    actual = lista.head
    while actual is not None:
        numeros.append(actual.data.numero)
        actual = actual.next
        if len(numeros) > 50:
            raise Fallo("La cadena no termina: algún nodo quedó apuntándose en círculo")
    return numeros


def numeros_de(pasajeros):
    resultado = []
    for p in pasajeros:
        resultado.append(p.numero)
    return resultado


# ---------- Una prueba por método ----------
def probar_esta_vacia():
    esperar(ListaPasajeros().esta_vacia() is True, "Con la lista vacía debería retornar True")
    esperar(lista_de_prueba().esta_vacia() is False, "Con 4 pasajeros debería retornar False")


def probar_longitud():
    esperar(ListaPasajeros().longitud() == 0, "Con la lista vacía debería retornar 0")
    valor = lista_de_prueba().longitud()
    esperar(valor == 4, f"Con 4 pasajeros debería retornar 4, retornó {valor!r}")


def probar_listar():
    vacia = ListaPasajeros().listar()
    esperar(vacia == [], f"Con la lista vacía debería retornar [], retornó {vacia!r}")
    lista = lista_de_prueba()
    numeros = numeros_de(lista_de_pasajeros(lista.listar(), "listar"))
    esperar(numeros == [1, 2, 3, 4], f"Esperaba los números [1, 2, 3, 4] (de head al último), obtuve {numeros}")
    esperar(cadena(lista) == [1, 2, 3, 4], "listar() no debe cambiar la lista enlazada")


def probar_busqueda(metodo, casos, clave_inexistente):
    """casos = [(clave, número esperado), ...] → uno en medio, la cabeza y el último."""
    lista = lista_de_prueba()
    for clave, esperado in casos:
        encontrado = pasajero_o_none(getattr(lista, metodo)(clave), metodo)   # getattr: llama al método por su nombre
        esperar(encontrado is not None, f"{metodo}({clave!r}) debería encontrar al pasajero #{esperado}, retornó None")
        esperar(encontrado.numero == esperado,
                f"{metodo}({clave!r}) retornó al pasajero #{encontrado.numero}, esperaba al #{esperado}")
    nada = getattr(lista, metodo)(clave_inexistente)
    esperar(nada is None, f"{metodo}({clave_inexistente!r}) no existe: debería retornar None, retornó {nada!r}")
    esperar(getattr(ListaPasajeros(), metodo)(casos[0][0]) is None, f"En una lista vacía {metodo}() debería retornar None")
    esperar(cadena(lista) == [1, 2, 3, 4], f"{metodo}() no debe cambiar la lista enlazada")


def probar_buscar():
    probar_busqueda("buscar", [(3, 3), (1, 1), (4, 4)], 99)


def probar_buscar_por_asiento():
    probar_busqueda("buscar_por_asiento", [("5D", 3), ("1A", 1), ("2C", 4)], "9F")


def probar_buscar_por_cedula():
    probar_busqueda("buscar_por_cedula", [("0000000003", 3), ("0000000001", 1), ("0000000004", 4)], "0999999999")


def probar_modificar():
    lista = lista_de_prueba()
    esperar(booleano(lista.modificar(3, "Carla M", 41, "6A"), "modificar") is True, "modificar(3, ...) existe: debería retornar True")
    nodo = lista.head.next.next                    # el tercer vagón
    esperar(nodo.data.nombre == "Carla M" and nodo.data.edad == 41 and nodo.data.asiento == "6A",
            "El pasajero #3 no quedó con nombre 'Carla M', edad 41 y asiento '6A'")
    esperar(cadena(lista) == [1, 2, 3, 4], "modificar() no debe mover nodos: el orden cambió")
    esperar(lista.modificar(99, "X", 1, "1A") is False, "modificar(99, ...) no existe: debería retornar False")
    esperar(lista.head.data.asiento == "1A", "modificar(99, ...) cambió a otro pasajero")


def probar_eliminar():
    lista = lista_de_prueba()
    quitado = pasajero_o_none(lista.eliminar(1), "eliminar")
    esperar(quitado is not None and quitado.numero == 1, "eliminar(1) (la cabeza) debería retornar al pasajero #1")
    esperar(cadena(lista) == [2, 3, 4], f"Tras eliminar la cabeza quedó {cadena(lista)}, esperaba [2, 3, 4]")
    esperar(lista.cantidad == 3, "Tras eliminar, self.cantidad debe bajar en 1")
    quitado = lista.eliminar(3)
    esperar(quitado is not None and quitado.numero == 3, "eliminar(3) (en medio) debería retornar al pasajero #3")
    esperar(cadena(lista) == [2, 4], f"Tras eliminar el del medio quedó {cadena(lista)}, esperaba [2, 4]")
    quitado = lista.eliminar(4)
    esperar(quitado is not None and quitado.numero == 4, "eliminar(4) (el último) debería retornar al pasajero #4")
    esperar(cadena(lista) == [2], f"Tras eliminar el último quedó {cadena(lista)}, esperaba [2]")
    esperar(lista.eliminar(99) is None, "eliminar(99) no existe: debería retornar None")
    esperar(cadena(lista) == [2], "eliminar(99) no debería quitar a nadie")
    lista.eliminar(2)
    esperar(lista.head is None and lista.cantidad == 0, "Al eliminar el único nodo, head debe quedar en None y cantidad en 0")
    esperar(lista.eliminar(2) is None, "En una lista vacía eliminar() debería retornar None")


def probar_filtrar_por_clase():
    lista = lista_de_prueba()
    ejecutiva = numeros_de(lista_de_pasajeros(lista.filtrar_por_clase("Ejecutiva"), "filtrar_por_clase"))
    esperar(ejecutiva == [1, 4], f"filtrar_por_clase('Ejecutiva') debería dar [1, 4], dio {ejecutiva}")
    economica = numeros_de(lista.filtrar_por_clase("Económica"))
    esperar(economica == [2, 3], f"filtrar_por_clase('Económica') debería dar [2, 3], dio {economica}")
    esperar(ListaPasajeros().filtrar_por_clase("Ejecutiva") == [], "En una lista vacía debería retornar []")
    esperar(cadena(lista) == [1, 2, 3, 4], "filtrar_por_clase() no debe cambiar la lista enlazada")


# Lista de (nombre del método, función que lo prueba)
PRUEBAS = [
    ("esta_vacia", probar_esta_vacia),
    ("longitud", probar_longitud),
    ("listar", probar_listar),
    ("buscar", probar_buscar),
    ("buscar_por_asiento", probar_buscar_por_asiento),
    ("buscar_por_cedula", probar_buscar_por_cedula),
    ("modificar", probar_modificar),
    ("eliminar", probar_eliminar),
    ("filtrar_por_clase", probar_filtrar_por_clase),
]


def correr_con_tiempo(prueba, segundos=1.0):
    """Corre la prueba en un hilo aparte; si tarda más de 1 s, es un bucle infinito."""
    resultado = {"estado": "lento",
                 "detalle": "Tardó demasiado: ¿bucle infinito? Revisa que avances con actual = actual.next"}

    def tarea():
        try:
            prueba()
            resultado["estado"] = "ok"
            resultado["detalle"] = "Todas las pruebas pasaron"
        except NotImplementedError:
            resultado["estado"] = "pendiente"
            resultado["detalle"] = "Aún no implementado"
        except (Fallo, ErrorEnTuMetodo) as e:
            resultado["estado"] = "fallo"
            resultado["detalle"] = str(e)
        except Exception as e:                   # cualquier otro error de Python
            resultado["estado"] = "error"
            resultado["detalle"] = f"{type(e).__name__}: {e}"

    hilo = threading.Thread(target=tarea, daemon=True)
    hilo.start()
    hilo.join(segundos)                          # espera como máximo 1 segundo
    return resultado


def revisar_todo():
    """Corre las 9 pruebas y retorna una lista de diccionarios para el panel."""
    informe = []
    for nombre, prueba in PRUEBAS:
        resultado = correr_con_tiempo(prueba)
        informe.append({"metodo": nombre, "estado": resultado["estado"], "detalle": resultado["detalle"]})
    return informe
