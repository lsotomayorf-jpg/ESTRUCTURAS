// ================================================================
//  AeroLista ✈ · semaforo.js — pinta cada asiento según su estado
// ================================================================

// El dibujo del pasajero: un SVG con un círculo (cabeza) y una curva (hombros)
function iconoPasajero() {
  return `<svg class="icono-pasajero" viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="6.5" r="4.5"/>
            <path d="M3 23c0-5.5 4-9.5 9-9.5s9 4 9 9.5z"/>
          </svg>`;
}

// Pide la lista de pasajeros (API.listar) y pinta el avión.
// Retorna la respuesta para que otros (el tren, paso 24) también la usen.
async function cargarReservas() {
  const r = await API.listar();
  estado.porAsiento = {};                  // empezamos el "mapa" vacío
  if (r.ok) {
    estado.reservas = r.datos;             // la lista completa, en orden
    // Armamos un diccionario asiento → pasajero:  { "7D": {...Luis}, "1A": {...Ana} }
    // así, para saber quién está en el 7D basta con estado.porAsiento["7D"]
    for (const pasajero of r.datos) {
      estado.porAsiento[pasajero.asiento] = pasajero;
    }
    ocultarAviso("#aviso-avion");
  } else {
    estado.reservas = [];
    mostrarAviso("#aviso-avion", r, "El avión todavía no puede ver las reservas.");
  }
  pintarAsientos();
  return r;
}

// Recorre los 68 botones y le pone a cada uno la clase correcta
function pintarAsientos() {
  for (const boton of $$(".asiento")) {
    const codigo = boton.dataset.asiento;                  // "7D"
    const pasajero = estado.porAsiento[codigo];            // el pasajero, o undefined si está libre
    // Primero le quitamos TODAS las clases de estado...
    boton.classList.remove("libre", "seleccionado", "ocupado", "encontrado", "editando", "menor");

    // ...y luego le ponemos la que corresponde
    if (pasajero) {                                        // 🔴 hay alguien sentado
      boton.classList.add("ocupado");
      if (pasajero.edad < 18) boton.classList.add("menor");   // los menores tienen icono más pequeño
      boton.innerHTML = iconoPasajero();                   // innerHTML mete HTML (el dibujo SVG)
      boton.setAttribute("aria-label", `Asiento ${codigo}: ${pasajero.nombre}`);   // para lectores de pantalla
    } else {                                               // 🟡 o 🟢
      boton.classList.add(codigo === estado.seleccionado ? "seleccionado" : "libre");
      boton.textContent = codigo.slice(-1);                // vuelve a mostrar la letra
      boton.setAttribute("aria-label", `Asiento ${codigo}: libre`);
    }
    if (codigo === estado.encontrado) boton.classList.add("encontrado");   // 🔵 resultado de búsqueda
    // El asiento del pasajero que se está modificando (paso 20) lleva borde punteado
    if (estado.enEdicion && codigo === estado.enEdicion.asiento) boton.classList.add("editando");
  }
}

// Reproduce una animación CSS sobre un asiento ("recien" o "liberado")
function animarAsiento(asiento, animacion) {
  const boton = botonDeAsiento(asiento);
  if (!boton) return;
  boton.classList.remove(animacion);
  void boton.offsetWidth;                  // truco: obliga al navegador a "reiniciar" la animación
  boton.classList.add(animacion);
  setTimeout(() => boton.classList.remove(animacion), 1000);
}

// Hace scroll suave hasta un asiento
function enfocarAsiento(asiento) {
  const boton = botonDeAsiento(asiento);
  if (boton) boton.scrollIntoView({ behavior: "smooth", block: "center" });
}

// Marca un asiento con el borde azul 🔵 y lo enfoca
function resaltar(asiento) {
  estado.encontrado = asiento;
  pintarAsientos();
  enfocarAsiento(asiento);
}
