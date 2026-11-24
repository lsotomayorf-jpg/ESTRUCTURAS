// ================================================================
//  AeroLista ✈ · mensajes.js — mensajes para el usuario
// ================================================================

// Muestra un mensaje flotante (toast) que desaparece solo.
//   texto: lo que dice el mensaje
//   tipo:  "ok" ✅ · "aviso" ⚠️ · "pendiente" 🚧 · "error" ❌ · "codigo" 💥
function avisar(texto, tipo = "ok") {
  // Un objeto como "diccionario": a cada tipo le corresponde un icono
  const iconos = { ok: "✅", aviso: "⚠️", pendiente: "🚧", error: "❌", codigo: "💥" };

  // Los mensajes buenos duran 3.5 s; los problemas, 7 s (para que alcances a leerlos)
  const duracion = tipo === "ok" ? 3500 : 7000;

  // Armamos:  <div class="toast toast-ok"> <span>✅</span> <p>texto</p> </div>
  const toast = crear("div", "toast toast-" + tipo);
  toast.append(crear("span", "", iconos[tipo]), crear("p", "", texto));
  $("#toasts").append(toast);                                   // ahora SÍ se ve

  // setTimeout(función, milisegundos) = "ejecuta esto dentro de X milisegundos"
  setTimeout(() => toast.classList.add("saliendo"), duracion);  // empieza a irse...
  setTimeout(() => toast.remove(), duracion + 400);             // ...y se borra de la página
}

// Recibe una respuesta de Flask que salió mal (r.ok === false) y elige el toast:
function mostrarProblema(r) {
  if (r.pendiente) avisar(r.mensaje, "pendiente");                        // 🚧 método sin programar
  else if (r.error_codigo) avisar(r.mensaje + "  (revisa la terminal de Flask)", "codigo");   // 💥 error de Python
  else avisar(r.mensaje, "error");                                        // ❌ dato incorrecto
}

// Muestra un aviso FIJO (no se va solo) dentro de una caja de la página.
// Lo usaremos para decir qué método de Python falta. selector = "#aviso-avion", etc.
function mostrarAviso(selector, r, titulo) {
  const caja = $(selector);
  caja.hidden = false;                                  // la hacemos visible
  caja.classList.toggle("es-error", !r.pendiente);      // rojo si es error, ámbar si es pendiente
  caja.innerHTML = r.pendiente
    ? `🚧 ${titulo} Implementa <code>${r.metodo}()</code> en <code>lista_pasajeros.py</code>, guarda y recarga la página.`
    : `💥 ${escapar(r.mensaje)}`;
}

// Esconde un aviso fijo
function ocultarAviso(selector) {
  $(selector).hidden = true;
}
