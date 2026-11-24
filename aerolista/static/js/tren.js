// ================================================================
//  AeroLista ✈ · tren.js — dibuja la lista como vagones de tren
//     head → [vagón] → [vagón] → ... → None
// ================================================================

// r: la respuesta de API.listar() · numeroNuevo: la reserva recién creada (se resalta)
function dibujarTren(r, numeroNuevo = null) {
  const tren = $("#tren-vagones");
  tren.innerHTML = "";

  if (!r.ok) {                                  // la lista no se pudo leer
    $("#tren-cantidad").textContent = "nodos = ?";
    const aviso = crear("p", "tren-vacio");
    aviso.innerHTML = r.pendiente
      ? `🚧 Aquí verás los vagones de tu lista cuando implementes <code>listar()</code>.`
      : `💥 ${escapar(r.mensaje)}`;
    tren.append(aviso);
    return;
  }

  $("#tren-cantidad").textContent = `nodos = ${r.datos.length}`;
  tren.append(crear("span", "etiqueta-head", "head"), crear("span", "flecha", "→"));   // la cabeza

  // Un vagón por pasajero, en el MISMO orden de la lista
  r.datos.forEach((pasajero, posicion) => {
    const vagon = crear("div", "vagon");
    if (pasajero.numero === numeroNuevo) vagon.classList.add("nuevo");   // el recién llegado, en verde
    vagon.title = "Clic para ver su asiento";
    vagon.innerHTML = `
      <div class="vagon-data">
        <small>[${posicion}] #${pasajero.numero}</small>
        <b>${escapar(pasajero.nombre)}</b>
        <span>asiento ${escapar(pasajero.asiento)}</span>
      </div>
      <div class="vagon-next">●</div>`;
    vagon.addEventListener("click", () => resaltar(pasajero.asiento));
    tren.append(vagon, crear("span", "flecha", "→"));
  });

  tren.append(crear("span", "nodo-none", "None"));   // el final de la lista
}
