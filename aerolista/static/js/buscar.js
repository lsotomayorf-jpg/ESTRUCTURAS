// ================================================================
//  AeroLista ✈ · buscar.js — buscar y mostrar el pase de abordar
// ================================================================

// Al enviar el formulario de búsqueda
async function enviarBusqueda(evento) {
  evento.preventDefault();
  const tipo = $('input[name="tipo"]:checked').value;     // :checked = el radio marcado
  const valor = $("#buscar-valor").value.trim();
  // /^\d+$/ = "solo dígitos". test() dice si el texto cumple ese patrón
  if (tipo === "numero" && !/^\d+$/.test(valor)) {
    avisar("El número de reserva solo lleva dígitos (ej: 1002)", "error");
    return;
  }
  await buscar(tipo, valor);
}

// Busca según el tipo y muestra el resultado
async function buscar(tipo, valor) {
  let r;
  if (tipo === "numero") r = await API.buscarNumero(valor);          // en Flask: buscar()
  else if (tipo === "cedula") r = await API.buscarCedula(valor);     // en Flask: buscar_por_cedula()
  else r = await API.buscarAsiento(valor.toUpperCase());             // en Flask: buscar_por_asiento()

  const caja = $("#resultado-buscar");
  caja.innerHTML = "";                                    // borramos el resultado anterior

  if (!r.ok) {                                            // no se encontró (o hubo un error)
    estado.encontrado = null;
    pintarAsientos();
    caja.append(crear("p", "vacio", (r.pendiente ? "🚧 " : "🔎 ") + r.mensaje));
    if (r.pendiente || r.error_codigo) mostrarProblema(r);
    return;
  }
  if (r.datos === null) {                                 // buscó un asiento y está libre
    caja.append(crear("p", "vacio", "💺 " + r.mensaje));
    resaltar(valor.toUpperCase());
    return;
  }
  caja.append(crearPase(r.datos));                        // ¡encontrado!
  resaltar(r.datos.asiento);                              // 🔵 en el avión
}

// Arma el pase de abordar de un pasajero con sus dos botones
function crearPase(p) {
  const clase = claseDeAsiento(p.asiento);
  const v = estado.vuelo;
  const contenedor = crear("div");
  // Plantilla con comillas invertidas: HTML con ${variables} adentro
  contenedor.innerHTML = `
    <article class="pase ${clase === "Ejecutiva" ? "ejecutiva" : ""}">
      <div class="pase-cuerpo">
        <div class="pase-cabecera"><span>✈ AEROLISTA</span><span>PASE DE ABORDAR</span></div>
        <div class="pase-nombre">${escapar(p.nombre)}</div>
        <div class="pase-ruta"><span>${v.codigo_origen}</span><i></i><span>✈</span><i></i><span>${v.codigo_destino}</span></div>
        <div class="pase-detalle">
          <span>Reserva<b>#${p.numero}</b></span>
          <span>Cédula<b>${escapar(p.cedula)}</b></span>
          <span>Edad<b>${p.edad} años</b></span>
        </div>
      </div>
      <div class="pase-talon"><small>ASIENTO</small><b>${escapar(p.asiento)}</b><em>${clase}</em></div>
    </article>
    <div class="pase-acciones">
      <button type="button" class="btn btn-suave" data-accion="modificar">✏️ Modificar</button>
      <button type="button" class="btn btn-peligro" data-accion="eliminar">🗑️ Cancelar reserva</button>
    </div>`;

  // Botón Modificar: va a la pestaña Modificar y carga a este pasajero (paso 20)
  contenedor.querySelector('[data-accion="modificar"]').addEventListener("click", () => {
    cambiarPestana("modificar");
    $("#modificar-numero").value = p.numero;
    cargarParaModificar(p.numero);
  });
  // Botón Cancelar reserva: reutiliza confirmarEliminar (paso 21)
  contenedor.querySelector('[data-accion="eliminar"]').addEventListener("click", async () => {
    const eliminado = await confirmarEliminar(p.numero, p);
    if (eliminado) $("#resultado-buscar").innerHTML = "";   // el pase ya no tiene sentido
  });
  return contenedor;
}

// ---- Conexiones ----
$("#form-buscar").addEventListener("submit", enviarBusqueda);
// Al cambiar de opción, cambia el texto de ejemplo del campo
for (const radio of $$('input[name="tipo"]')) {
  radio.addEventListener("change", () => {
    const ejemplos = { numero: "Ej: 1002", cedula: "Ej: 0912345678", asiento: "Ej: 7D" };
    $("#buscar-valor").placeholder = ejemplos[radio.value];
  });
}
