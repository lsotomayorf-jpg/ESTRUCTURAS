// ================================================================
//  AeroLista ✈ · modificar.js — cambiar nombre, edad o asiento
// ================================================================

// Al enviar el primer formulario (Cargar)
async function enviarCargar(evento) {
  evento.preventDefault();
  await cargarParaModificar($("#modificar-numero").value);
}

// Busca la reserva y llena el segundo formulario con sus datos
async function cargarParaModificar(numero) {
  const r = await API.buscarNumero(numero);     // en Flask usará buscar() de tu lista
  if (!r.ok) return mostrarProblema(r);
  const p = r.datos;
  estado.enEdicion = p;                         // la página recuerda a quién modificamos
  estado.seleccionado = null;
  const formulario = $("#form-modificar");
  formulario.nombre.value = p.nombre;           // llenamos los campos
  formulario.cedula.value = p.cedula;
  formulario.edad.value = p.edad;
  $("#modificar-asiento").textContent = p.asiento;
  formulario.hidden = false;                    // mostramos el formulario
  resaltar(p.asiento);                          // 🔵 y borde punteado en su asiento
}

// Al enviar el segundo formulario (Guardar cambios)
async function guardarCambios(evento) {
  evento.preventDefault();
  const p = estado.enEdicion;
  const formulario = evento.target;
  const datos = {                               // 1. LEER
    nombre: formulario.nombre.value.trim(),
    edad: formulario.edad.value,
    // || significa "o": si no eligió otro asiento, se queda en el suyo
    asiento: estado.seleccionado || p.asiento,
  };
  const r = await API.modificar(p.numero, datos);   // 2. LLAMAR
  if (!r.ok) return mostrarProblema(r);             // 3. MOSTRAR
  avisar(r.mensaje, "ok");
  for (const aviso of r.avisos) avisar(aviso, "aviso");
  cancelarEdicion();
  await refrescar();
  animarAsiento(r.datos.asiento, "recien");
  resaltar(r.datos.asiento);
}

// Sale del modo edición y esconde el formulario
function cancelarEdicion() {
  estado.enEdicion = null;
  estado.seleccionado = null;
  $("#form-modificar").hidden = true;
  pintarAsientos();
}

// ---- Conexiones ----
$("#form-cargar").addEventListener("submit", enviarCargar);
$("#form-modificar").addEventListener("submit", guardarCambios);
$("#btn-cancelar-edicion").addEventListener("click", cancelarEdicion);
// Si te vas a otra pestaña en medio de una edición, se cancela
for (const boton of $$(".pestana")) {
  boton.addEventListener("click", () => {
    if (boton.dataset.pestana !== "modificar" && estado.enEdicion) cancelarEdicion();
  });
}
