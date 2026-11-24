// ================================================================
//  AeroLista ✈ · progreso.js — el panel "Progreso del backend"
// ================================================================

// Un icono para cada estado que manda verificador.py
const ICONOS_PROGRESO = { ok: "✅", pendiente: "🚧", fallo: "❌", error: "💥", lento: "⏳" };

// Pide las pruebas a Flask y dibuja un renglón por método.
// Retorna true si los 9 pasaron.
async function cargarProgreso() {
  const lista = $("#progreso-lista");
  const r = await API.progreso();
  lista.innerHTML = "";
  if (API.modo === "demo") {                       // con datos de mentira no hay nada que probar
    $("#progreso-cuenta").textContent = "demo";
    lista.innerHTML = `<li><span>🧪</span><span>Modo de prueba: los datos vienen de <code>datos-demo.js</code>.</span></li>`;
    return false;
  }
  if (!r.ok) {
    lista.innerHTML = `<li class="error"><span>💥</span><span>${escapar(r.mensaje)}</span></li>`;
    return false;
  }
  // filter deja solo los "ok"; length cuenta cuántos son
  const listos = r.datos.filter((m) => m.estado === "ok").length;
  $("#progreso-cuenta").textContent = `${listos}/${r.datos.length}`;          // "3/9"
  $("#progreso-barra").style.width = (listos * 100) / r.datos.length + "%";
  for (const m of r.datos) {
    const item = crear("li", m.estado);
    item.innerHTML = `<span>${ICONOS_PROGRESO[m.estado]}</span><code>${m.metodo}()</code>`;
    // Si falló, mostramos el detalle (qué esperaba y qué obtuvo)
    if (m.estado !== "ok" && m.estado !== "pendiente") item.append(crear("small", "", m.detalle));
    lista.append(item);
  }
  return listos === r.datos.length;
}

// Botón "Revisar otra vez": vuelve a probar y refresca toda la página
async function revisarProgreso() {
  const completo = await cargarProgreso();
  if (completo) avisar("¡Backend completo! Todos tus métodos pasaron las pruebas 🎉", "ok");
  await refrescar();
}

// Botón "Datos de ejemplo": vuelve a los 12 pasajeros (pregunta antes con el dialog del paso 21)
async function restaurarDatos() {
  const acepta = await preguntar("¿Restaurar los datos de ejemplo?",
    "Se borrarán las reservas actuales y volverán las 12 reservas de prueba.");
  if (!acepta) return;
  const r = await API.restaurar();
  if (!r.ok) return mostrarProblema(r);
  avisar(r.mensaje, "ok");
  estado.encontrado = null;
  await refrescar();
}

$("#btn-revisar").addEventListener("click", revisarProgreso);
$("#btn-restaurar").addEventListener("click", restaurarDatos);
