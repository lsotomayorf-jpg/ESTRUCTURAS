// ================================================================
//  AeroLista ✈ · pestanas.js — cambiar de pestaña en el panel
// ================================================================

// Muestra la pestaña "nombre" y esconde las demás
function mostrarPestana(nombre) {
  estado.pestana = nombre;                         // la página recuerda cuál está abierta
  // A cada botón: le pone "activa" solo si es el de esta pestaña
  for (const boton of $$(".pestana")) {
    boton.classList.toggle("activa", boton.dataset.pestana === nombre);
  }
  // A cada sección: le pone "activa" solo si su id es "pestana-" + nombre
  for (const seccion of $$(".contenido-pestana")) {
    seccion.classList.toggle("activa", seccion.id === "pestana-" + nombre);
  }
}

// Para cambiar de pestaña DESDE EL CÓDIGO, "hacemos clic" en su botón.
// Así se ejecutan también los oyentes que otros archivos agregan a esos botones.
function cambiarPestana(nombre) {
  $(`.pestana[data-pestana="${nombre}"]`).click();
}

// Cada botón, al hacer clic, muestra su pestaña
for (const boton of $$(".pestana")) {
  boton.addEventListener("click", () => mostrarPestana(boton.dataset.pestana));
}
