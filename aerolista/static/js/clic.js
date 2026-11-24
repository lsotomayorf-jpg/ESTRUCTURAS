// ================================================================
//  AeroLista ✈ · clic.js — qué pasa al hacer clic en un asiento
//  Versión 3 (final): rojo → pase de abordar · verde → elegir.
// ================================================================

async function clicEnAsiento(codigo) {
  // a) Asiento ROJO: buscamos quién está ahí y mostramos su pase  🆕
  if (estado.porAsiento[codigo]) {
    cambiarPestana("buscar");                                    // abre la pestaña Buscar
    $('input[name="tipo"][value="asiento"]').checked = true;     // marca la opción "Asiento"
    $("#buscar-valor").value = codigo;                           // escribe el asiento
    await buscar("asiento", codigo);                             // y busca (buscar.js)
    return;
  }

  // b) Asiento VERDE mientras se modifica una reserva: será su asiento nuevo
  if (estado.enEdicion) {
    estado.seleccionado = codigo;
    $("#modificar-asiento").textContent = codigo;
    pintarAsientos();
    return;
  }

  // c) Asiento VERDE: lo elegimos para una reserva nueva (otro clic lo suelta)
  if (estado.pestana !== "reservar") cambiarPestana("reservar");
  estado.seleccionado = estado.seleccionado === codigo ? null : codigo;
  estado.encontrado = null;
  actualizarAsientoElegido();
  pintarAsientos();
  if (estado.seleccionado) $('#form-reservar [name="nombre"]').focus({ preventScroll: true });
}
