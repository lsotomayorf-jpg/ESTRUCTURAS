// ================================================================
//  AeroLista ✈ · main.js  —  el "director de orquesta"
//  Versión 8 (final): avión + tablero + tren + progreso.
// ================================================================

// ESTADO: la "memoria" de la página
const estado = {
  vuelo: null,          // los datos del avión (de /api/vuelo)
  vista: "3d",          // "3d" o "2d"
  reservas: [],         // la lista de pasajeros (en orden de llegada)
  porAsiento: {},       // atajo para pintar: { "7D": pasajero, ... }
  seleccionado: null,   // asiento libre elegido con clic (🟡)
  encontrado: null,     // asiento resaltado por una búsqueda (🔵)
  enEdicion: null,      // pasajero que se está modificando
  pestana: "reservar",  // pestaña abierta del panel
  filtroClase: "",      // filtro de la pestaña Listar
};

// Vuelve a pedir todo lo que puede cambiar después de reservar, modificar o eliminar
async function refrescar(numeroNuevo = null) {
  const r = await cargarReservas();       // lista → avión pintado (semaforo.js)
  dibujarTren(r, numeroNuevo);            // la misma lista → tren (tren.js)
  await cargarResumen();                  // tablero (tablero.js)
}

// Arranque de la aplicación
async function iniciar() {
  const r = await API.vuelo();            // 1. datos del avión
  if (!r.ok) {
    avisar(r.mensaje, "codigo");
    return;
  }
  estado.vuelo = r.datos;
  dibujarAvion();                         // 2. filas y asientos (avion.js)
  aplicarAngulos();                       // 3. vista 3D (vista3d.js)
  await refrescar();                      // 4. reservas, tren y tablero
  avisar(`Vuelo ${estado.vuelo.codigo} listo · haz clic en un asiento`);
  await cargarProgreso();                 // 5. 🆕 pruebas de tus métodos (progreso.js)
}

iniciar();
