// ================================================================
//  AeroLista ✈ · reservar.js — crear una reserva nueva
// ================================================================

// Escribe en el formulario el asiento elegido (o "—" si no hay ninguno)
function actualizarAsientoElegido() {
  const salida = $("#reservar-asiento");
  if (estado.seleccionado) {
    salida.textContent = estado.seleccionado;              // "9C"
    salida.classList.remove("vacio");
    $("#reservar-clase").textContent = "Clase " + claseDeAsiento(estado.seleccionado);
  } else {
    salida.textContent = "—";
    salida.classList.add("vacio");
    $("#reservar-clase").textContent = "Elige uno en el avión";
  }
}

// Se ejecuta al enviar el formulario. "evento" trae información del envío.
async function reservar(evento) {
  evento.preventDefault();          // ⚠ MUY IMPORTANTE: evita que la página se recargue

  if (!estado.seleccionado) {       // sin asiento no se puede reservar
    avisar("Primero haz clic en un asiento verde del avión", "aviso");
    return;
  }

  // 1. LEER: evento.target es el formulario; .nombre es el input con name="nombre"
  const formulario = evento.target;
  const datos = {
    nombre: formulario.nombre.value.trim(),     // trim() quita espacios al inicio y al final
    cedula: formulario.cedula.value.trim(),
    edad: formulario.edad.value,
    asiento: estado.seleccionado,
  };

  // 2. LLAMAR: pedimos la reserva (por ahora al servidor de mentira; en el paso 29, a Flask)
  const r = await API.reservar(datos);

  // 3. MOSTRAR
  if (!r.ok) return mostrarProblema(r);         // ❌ algo salió mal: avisamos y salimos
  avisar(r.mensaje, "ok");                      // ✅
  for (const aviso of r.avisos) avisar(aviso, "aviso");   // ⚠ advertencias (si las hay)
  formulario.reset();                           // limpia los campos
  estado.seleccionado = null;                   // ya no hay asiento elegido
  actualizarAsientoElegido();
  await refrescar(r.datos.numero);              // vuelve a pintar todo
  animarAsiento(r.datos.asiento, "recien");     // el asiento nuevo "salta"
}

// ---- Conexiones ----
// "submit" se dispara al pulsar el botón del formulario (o Enter en un campo)
$("#form-reservar").addEventListener("submit", reservar);

// Si te vas a otra pestaña, el asiento amarillo se suelta
for (const boton of $$(".pestana")) {
  boton.addEventListener("click", () => {
    if (boton.dataset.pestana !== "reservar" && estado.seleccionado && !estado.enEdicion) {
      estado.seleccionado = null;
      actualizarAsientoElegido();
      pintarAsientos();
    }
  });
}
