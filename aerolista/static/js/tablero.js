// ================================================================
//  AeroLista ✈ · tablero.js — los números de arriba del avión
// ================================================================

async function cargarResumen() {
  const r = await API.resumen();          // { cantidad, vacia, total_asientos }
  const totalAsientos = $$(".asiento").length;      // 68 (contamos los botones dibujados)
  $("#dato-total").textContent = totalAsientos;

  if (!r.ok) {                            // si falla, dejamos guiones y mostramos el aviso
    for (const id of ["#dato-reservados", "#dato-libres", "#dato-ocupacion"]) $(id).textContent = "—";
    $("#luz-ocupacion").className = "luz";
    $("#barra-ocupacion").style.width = "0";
    mostrarAviso("#aviso-tablero", r, "El tablero no puede contar las reservas.");
    return;
  }
  ocultarAviso("#aviso-tablero");

  const cantidad = r.datos.cantidad;
  const porcentaje = Math.round((cantidad * 100) / totalAsientos);   // regla de tres

  // El semáforo de ocupación
  let color = "verde";                    // 🟢 menos de la mitad
  if (porcentaje >= 80) color = "rojo";   // 🔴 casi lleno
  else if (porcentaje >= 50) color = "ambar";   // 🟡 más de la mitad

  $("#dato-reservados").textContent = cantidad;
  $("#dato-libres").textContent = totalAsientos - cantidad;
  $("#dato-ocupacion").textContent = porcentaje + "%";
  $("#luz-ocupacion").className = "luz " + color;            // className reemplaza TODAS las clases
  $("#barra-ocupacion").style.width = porcentaje + "%";      // la barrita crece
  $("#barra-ocupacion").style.background = `var(--${color})`;
}
