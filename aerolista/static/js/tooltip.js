// ================================================================
//  AeroLista ✈ · tooltip.js — el globo de ayuda de los asientos
// ================================================================

// Llena el globo con los datos del asiento y lo muestra
function mostrarTooltip(codigo, evento) {
  const tooltip = $("#tooltip");
  const p = estado.porAsiento[codigo];          // ¿hay alguien sentado ahí?
  const clase = claseDeAsiento(codigo);
  tooltip.innerHTML = p
    ? `<b>${escapar(p.nombre)}</b> ${p.edad < 18 ? "🧒" : ""}<br>Asiento ${codigo} · ${clase}<br>` +
      `<small>Reserva #${p.numero} · clic para ver su pase</small>`
    : `<b>Asiento ${codigo}</b><br>${clase} · <span style="color:#86EFAC">libre</span><br><small>clic para elegirlo</small>`;
  tooltip.hidden = false;
  moverTooltip(evento);
}

// Pone el globo un poquito abajo y a la derecha del mouse.
// clientX / clientY = posición del mouse en la pantalla
function moverTooltip(evento) {
  const tooltip = $("#tooltip");
  tooltip.style.left = evento.clientX + 16 + "px";
  tooltip.style.top = evento.clientY + 16 + "px";
}

function ocultarTooltip() {
  $("#tooltip").hidden = true;
}

// ---- Delegación: UN solo oyente en la cabina vigila los 68 asientos ----
// "mouseover" se dispara cuando el mouse entra a cualquier cosa dentro de la cabina.
// evento.target es el elemento exacto; closest(".asiento") sube hasta encontrar el botón.
$("#cabina").addEventListener("mouseover", (evento) => {
  const boton = evento.target.closest(".asiento");
  if (boton) mostrarTooltip(boton.dataset.asiento, evento);
});
$("#cabina").addEventListener("mousemove", (evento) => {
  if (!$("#tooltip").hidden) moverTooltip(evento);       // el globo sigue al mouse
});
$("#cabina").addEventListener("mouseout", (evento) => {
  if (evento.target.closest(".asiento")) ocultarTooltip();   // salió de un asiento
});
