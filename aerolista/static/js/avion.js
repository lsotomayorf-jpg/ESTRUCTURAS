// ================================================================
//  AeroLista ✈ · avion.js — crea las filas y los asientos
//  Usa estado.vuelo (filas, letras...) que llegó de Flask.
// ================================================================

// Dibuja TODO el interior del avión dentro de <div id="cabina">
function dibujarAvion() {
  const cabina = $("#cabina");
  const v = estado.vuelo;                    // atajo: v.filas, v.letras_economica, ...
  cabina.innerHTML = "";                     // empezamos con la cabina vacía

  cabina.append(crearServicio("🍽 Cocina", "🚻 Baño"));   // zona de servicio adelante

  // Recorrido de las filas: 1, 2, 3, ..., 12
  for (let fila = 1; fila <= v.filas; fila++) {
    // Antes de la fila 1 ponemos el letrero "EJECUTIVA"
    if (fila === 1) cabina.append(crear("div", "separador ejecutiva", "EJECUTIVA"));
    // Antes de la primera fila económica (la 3) ponemos "ECONÓMICA"
    if (fila === v.filas_ejecutiva + 1) cabina.append(crear("div", "separador", "ECONÓMICA"));
    cabina.append(crearFila(fila));          // creamos la fila y la metemos en la cabina
  }

  cabina.append(crearServicio("🚻 Baño", "🍽 Cocina"));   // zona de servicio atrás
}

// Una franja con dos letreros (cocina y baño)
function crearServicio(izquierda, derecha) {
  const zona = crear("div", "servicio");
  zona.append(crear("span", "", izquierda), crear("span", "", derecha));
  return zona;
}

// Crea UNA fila:   ventana | A B C | 7 | D E F | ventana
function crearFila(fila) {
  const v = estado.vuelo;
  const esEjecutiva = fila <= v.filas_ejecutiva;                         // ¿fila 1 o 2?
  const letras = esEjecutiva ? v.letras_ejecutiva : v.letras_economica;  // ["A","C","D","F"] o ["A",...,"F"]

  // La fila es un div. Las filas ejecutivas llevan una clase extra (asientos más grandes)
  const divFila = crear("div", esEjecutiva ? "fila fila-ejecutiva" : "fila");
  // includes() pregunta si la lista contiene ese valor: ¿es fila de salida de emergencia?
  if (v.filas_salida.includes(fila)) divFila.classList.add("fila-salida");

  const izquierda = crear("div", "lado");    // lado izquierdo del pasillo
  const derecha = crear("div", "lado");      // lado derecho del pasillo

  // Recorrido de las letras de esta fila
  for (const letra of letras) {
    const boton = crearAsiento(fila + letra);   // 7 + "D" → "7D"
    if (letra < "D") izquierda.append(boton);   // A, B, C van a la izquierda ("A" < "D" es true)
    else derecha.append(boton);                 // D, E, F van a la derecha
  }

  // Armamos la fila en orden: ventana, lado izq, número, lado der, ventana
  divFila.append(crear("span", "ventana"), izquierda,
                 crear("span", "numero-fila", String(fila)),
                 derecha, crear("span", "ventana"));
  return divFila;
}

// Crea UN asiento: <button class="asiento libre" data-asiento="7D">D</button>
function crearAsiento(codigo) {
  const boton = crear("button", "asiento libre", codigo.slice(-1));   // slice(-1) = última letra
  boton.type = "button";                     // un botón normal (no envía formularios)
  boton.dataset.asiento = codigo;            // guarda el código en data-asiento="7D"
  // Cuando le hagan clic, llama a clicEnAsiento con SU código (está en clic.js)
  boton.addEventListener("click", () => clicEnAsiento(codigo));
  return boton;
}
