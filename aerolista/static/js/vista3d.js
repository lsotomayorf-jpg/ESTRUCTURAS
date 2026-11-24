// ================================================================
//  AeroLista ✈ · vista3d.js — vista 3D: inclinar y girar el avión
// ================================================================

// Cambia entre "3d" y "2d"
function cambiarVista(vista) {
  estado.vista = vista;                                       // la página recuerda la vista
  $("#avion").classList.toggle("vista-3d", vista === "3d");   // toggle(clase, condición): la pone si es true
  $("#ajustes-3d").hidden = vista !== "3d";                   // deslizadores solo en 3D
  for (const boton of $$(".btn-vista")) {                     // marca el botón elegido
    boton.classList.toggle("activo", boton.dataset.vista === vista);
  }
  aplicarAngulos();
}

// Pasa los valores de los deslizadores a las variables CSS del avión
function aplicarAngulos() {
  const avion = $("#avion");
  const en3D = estado.vista === "3d";
  // En 2D los dos ángulos valen 0: el avión queda plano (y la transición lo anima)
  avion.style.setProperty("--inclinacion", (en3D ? $("#rango-inclinacion").value : 0) + "deg");
  avion.style.setProperty("--giro", (en3D ? $("#rango-giro").value : 0) + "deg");
  ajustarEscena();
}

// Calcula DÓNDE se ve en pantalla un punto (x, y) del avión después de girarlo.
// Es el mismo cálculo que hace el navegador con rotateZ → rotateX → perspective.
function proyectar(x, y, giro, incl) {
  const x1 = x * Math.cos(giro) - y * Math.sin(giro);    // rotateZ (girar sobre la mesa)
  const y1 = x * Math.sin(giro) + y * Math.cos(giro);
  const y2 = y1 * Math.cos(incl);                        // rotateX: se acorta...
  const z2 = y1 * Math.sin(incl);                        // ...y gana profundidad
  const factor = 1800 / (1800 - z2);                     // perspective(1800px): lo cercano crece
  return [x1 * factor, y2 * factor];
}

// Elige la escala y el alto de la escena para que el avión quepa COMPLETO
function ajustarEscena() {
  const avion = $("#avion");
  const escena = $("#escena");
  const mitadAncho = avion.offsetWidth / 2;              // offsetWidth = ancho real en px
  const mitadAlto = avion.offsetHeight / 2;
  const en3D = estado.vista === "3d";
  // Math.PI / 180 convierte grados en radianes (lo que usan Math.cos y Math.sin)
  const giro = en3D ? ($("#rango-giro").value * Math.PI) / 180 : 0;
  const incl = en3D ? ($("#rango-inclinacion").value * Math.PI) / 180 : 0;

  // Proyectamos las 4 esquinas del avión y buscamos la caja que las encierra
  let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
  const esquinas = [[-mitadAncho, -mitadAlto], [mitadAncho, -mitadAlto],
                    [mitadAncho, mitadAlto], [-mitadAncho, mitadAlto]];
  for (const [x, y] of esquinas) {
    const [px, py] = proyectar(x, y, giro, incl);
    minX = Math.min(minX, px); maxX = Math.max(maxX, px);
    minY = Math.min(minY, py); maxY = Math.max(maxY, py);
  }
  // Si no cabe a lo ancho, lo achicamos (escala menor a 1); nunca lo agrandamos
  const escala = Math.min(1, (escena.clientWidth - 24) / (maxX - minX));
  avion.style.setProperty("--escala", escala.toFixed(3));
  avion.style.setProperty("--ajuste-y", (-(minY + maxY) / 2 * escala).toFixed(1) + "px");   // lo centra
  escena.style.height = Math.round((maxY - minY) * escala + 50) + "px";                     // alto justo
}

// ---- Conectamos los controles (esto se ejecuta apenas se carga el archivo) ----
for (const boton of $$(".btn-vista")) {
  boton.addEventListener("click", () => cambiarVista(boton.dataset.vista));
}
// "input" se dispara MIENTRAS mueves el deslizador
$("#rango-inclinacion").addEventListener("input", aplicarAngulos);
$("#rango-giro").addEventListener("input", aplicarAngulos);
// "resize" se dispara cuando cambia el tamaño de la ventana
window.addEventListener("resize", ajustarEscena);
