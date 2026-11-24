// ================================================================
//  AeroLista ✈ · listar.js — la tabla de pasajeros
// ================================================================

async function cargarTabla() {
  // "" → todos (en Flask: listar())  ·  "Ejecutiva" → solo esa clase (filtrar_por_clase())
  const r = await API.listar(estado.filtroClase);
  const cuerpo = $("#tabla-reservas");
  cuerpo.innerHTML = "";                       // vaciamos la tabla

  if (!r.ok) {                                 // colspan="5": una celda que ocupa las 5 columnas
    cuerpo.innerHTML = `<tr><td colspan="5" class="sin-datos">${r.pendiente ? "🚧" : "💥"} ${escapar(r.mensaje)}</td></tr>`;
    return;
  }
  if (r.datos.length === 0) {
    cuerpo.innerHTML = `<tr><td colspan="5" class="sin-datos">No hay pasajeros en esta clase</td></tr>`;
    return;
  }
  // forEach recorre la lista y nos da cada pasajero y su posición (i)
  r.datos.forEach((p, i) => {
    const fila = crear("tr");
    const ejecutiva = claseDeAsiento(p.asiento) === "Ejecutiva" ? "ejecutiva" : "";
    fila.innerHTML = `<td>${i}</td><td>${p.numero}</td><td>${escapar(p.nombre)}${p.edad < 18 ? " 🧒" : ""}</td>
                      <td>${p.edad}</td><td><span class="etiqueta-asiento ${ejecutiva}">${escapar(p.asiento)}</span></td>`;
    fila.addEventListener("click", () => resaltar(p.asiento));   // clic en la fila → 🔵 en el avión
    cuerpo.append(fila);
  });
}

// Clic en un filtro. Delegación: un oyente en la caja de filtros
function elegirFiltro(evento) {
  const chip = evento.target.closest(".chip");
  if (!chip) return;                           // hizo clic fuera de un botón
  estado.filtroClase = chip.dataset.clase;
  for (const otro of $$(".chip")) otro.classList.toggle("activo", otro === chip);
  cargarTabla();
}

// ---- Conexiones ----
$(".filtros").addEventListener("click", elegirFiltro);
// Cada vez que abres la pestaña Listar, la tabla se vuelve a cargar
$('.pestana[data-pestana="listar"]').addEventListener("click", cargarTabla);
