// ================================================================
//  AeroLista ✈ · utilidades.js — atajos que usan todos los archivos
// ================================================================

// $("#cabina") es un atajo de document.querySelector("#cabina"):
// devuelve el PRIMER elemento que cumple el selector CSS.
// (selector) => ... es una "función flecha": una forma corta de escribir una función.
const $ = (selector) => document.querySelector(selector);

// $$(".asiento") devuelve TODOS los elementos que cumplen el selector.
const $$ = (selector) => document.querySelectorAll(selector);

// Crea un elemento HTML nuevo de una sola vez.
// Ejemplo: crear("span", "ventana")  →  <span class="ventana"></span>
// Los parámetros con = "" son OPCIONALES: si no los pasas, valen "".
function crear(etiqueta, clase = "", texto = "") {
  const elemento = document.createElement(etiqueta);   // 1. crea la etiqueta
  if (clase) elemento.className = clase;               // 2. le pone su(s) clase(s)
  if (texto) elemento.textContent = texto;             // 3. le pone el texto
  return elemento;                                     // todavía NO se ve: falta meterlo en la página
}

// Protege el texto que escribe el usuario antes de meterlo con innerHTML.
// Si alguien escribe <b>Ana</b> como nombre, se mostrará tal cual y no como HTML.
function escapar(texto) {
  const div = document.createElement("div");
  div.textContent = String(texto);       // textContent nunca interpreta etiquetas
  return div.innerHTML;                  // devuelve el texto ya "escapado" (&lt;b&gt;...)
}

// Dice la clase de un asiento: "1A" → "Ejecutiva", "7D" → "Económica".
function claseDeAsiento(asiento) {
  const fila = parseInt(asiento);        // parseInt("12A") lee el número del inicio → 12
  return fila <= estado.vuelo.filas_ejecutiva ? "Ejecutiva" : "Económica";
  //     condición ? valor si es verdad : valor si es mentira   (operador ternario)
}

// Busca el botón de un asiento por su código: botonDeAsiento("7D")
function botonDeAsiento(asiento) {
  return document.querySelector(`.asiento[data-asiento="${asiento}"]`);
}
