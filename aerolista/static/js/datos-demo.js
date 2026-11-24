// ================================================================
//  AeroLista ✈ · datos-demo.js — un SERVIDOR DE MENTIRA
//  Finge ser Flask mientras construimos la interfaz (Etapa D).
//  En el paso 29 lo desconectamos y los datos vendrán de Python.
//  ⚠ Si recargas la página, todo vuelve a como estaba (no se guarda).
// ================================================================

API.modo = "demo";      // una marca para saber que estamos usando datos falsos

// Los 12 pasajeros de prueba, en ORDEN DE LLEGADA (Diana reservó primero).
// Cada pasajero es un objeto con 5 datos. Son los mismos que tendrá data/ejemplo.json
const RESERVAS_INICIALES = [
  { numero: 1005, nombre: "Diana",   cedula: "0923456789", edad: 22, asiento: "3C" },
  { numero: 1002, nombre: "Ana",     cedula: "0912345678", edad: 28, asiento: "1A" },
  { numero: 1009, nombre: "Luis",    cedula: "0987654321", edad: 35, asiento: "7D" },
  { numero: 1004, nombre: "Beto",    cedula: "0934567890", edad: 16, asiento: "7E" },
  { numero: 1001, nombre: "Elena",   cedula: "0901234567", edad: 41, asiento: "2F" },
  { numero: 1008, nombre: "Carla",   cedula: "0945678901", edad: 33, asiento: "5A" },
  { numero: 1003, nombre: "Jorge",   cedula: "0956789012", edad: 52, asiento: "10B" },
  { numero: 1010, nombre: "Sofía",   cedula: "0967890123", edad: 9,  asiento: "10C" },
  { numero: 1007, nombre: "Mateo",   cedula: "0978901234", edad: 27, asiento: "12F" },
  { numero: 1006, nombre: "Valeria", cedula: "0989012345", edad: 30, asiento: "4D" },
  { numero: 1011, nombre: "Pedro",   cedula: "0990123456", edad: 45, asiento: "1D" },
  { numero: 1012, nombre: "Lucía",   cedula: "0911223344", edad: 19, asiento: "8B" },
];

// Copia de trabajo: { ...p } copia cada objeto, para no dañar los originales
let reservasDemo = RESERVAS_INICIALES.map((p) => ({ ...p }));
let siguienteNumero = 1013;          // el próximo número de reserva

// ---- Ayudantes: responden igual que Flask, con una pequeña espera (120 ms) ----
// Una Promise es "un valor que llegará después": así se comporta igual que fetch.
function responder(datos = null, mensaje = "") {
  return new Promise((resolver) =>
    setTimeout(() => resolver({ ok: true, datos, mensaje, avisos: [] }), 120));
}
function fallar(mensaje) {
  return new Promise((resolver) => setTimeout(() => resolver({ ok: false, mensaje }), 120));
}

// Revisa los datos de un formulario. Retorna el problema o "" si todo está bien.
function problemaEnDatos(datos) {
  if (!datos.nombre || datos.nombre.length < 2) return "Escribe el nombre del pasajero";
  if (!/^\d{10}$/.test(datos.cedula)) return "La cédula debe tener 10 dígitos";   // /^\d{10}$/ = exactamente 10 dígitos
  const edad = Number(datos.edad);
  if (datos.edad === "" || !Number.isInteger(edad) || edad < 0 || edad > 120) return "La edad debe ser un número entre 0 y 120";
  return "";
}

// ---- Las funciones del "servidor" ----

// Resumen para el tablero: cuántos hay y cuántos asientos tiene el avión
API.resumen = () => responder({
  cantidad: reservasDemo.length,
  vacia: reservasDemo.length === 0,
  total_asientos: $$(".asiento").length,
});

// Listar todos (o solo una clase). filter() deja pasar solo los que cumplen la condición
API.listar = (clase = "") => {
  if (clase === "") return responder(reservasDemo.map((p) => ({ ...p })));
  return responder(reservasDemo.filter((p) => claseDeAsiento(p.asiento) === clase));
};

// Buscar por número. find() devuelve el PRIMERO que cumple la condición (o undefined)
API.buscarNumero = (numero) => {
  const p = reservasDemo.find((r) => r.numero === Number(numero));
  return p ? responder({ ...p }, `Reserva #${numero} encontrada`) : fallar(`No existe la reserva #${numero}`);
};

// Buscar por asiento: si nadie está sentado, responde datos = null (asiento libre)
API.buscarAsiento = (asiento) => {
  const p = reservasDemo.find((r) => r.asiento === asiento);
  return p ? responder({ ...p }, `En el ${asiento} viaja ${p.nombre}`)
           : responder(null, `El asiento ${asiento} está libre`);
};

// Buscar por cédula
API.buscarCedula = (cedula) => {
  const p = reservasDemo.find((r) => r.cedula === cedula);
  return p ? responder({ ...p }, "Pasajero encontrado") : fallar(`Ningún pasajero tiene la cédula ${cedula}`);
};

// Reservar: valida y agrega AL FINAL (en Python será lista.ingresar)
API.reservar = (datos) => {
  const problema = problemaEnDatos(datos);
  if (problema) return fallar(problema);
  // some() pregunta: ¿ALGUNO cumple la condición?
  if (reservasDemo.some((r) => r.asiento === datos.asiento)) return fallar(`El asiento ${datos.asiento} ya está reservado`);
  if (reservasDemo.some((r) => r.cedula === datos.cedula)) return fallar(`La cédula ${datos.cedula} ya tiene una reserva en este vuelo`);
  const nuevo = { numero: siguienteNumero, nombre: datos.nombre, cedula: datos.cedula,
                  edad: Number(datos.edad), asiento: datos.asiento };
  siguienteNumero = siguienteNumero + 1;
  reservasDemo.push(nuevo);                          // push() = append() de Python
  return responder({ ...nuevo }, `Reserva #${nuevo.numero} creada: ${nuevo.nombre} en el asiento ${nuevo.asiento}`);
};

// Modificar nombre, edad y asiento
API.modificar = (numero, datos) => {
  const p = reservasDemo.find((r) => r.numero === Number(numero));
  if (!p) return fallar(`No existe la reserva #${numero}`);
  const problema = problemaEnDatos({ ...datos, cedula: p.cedula });
  if (problema) return fallar(problema);
  const ocupante = reservasDemo.find((r) => r.asiento === datos.asiento);
  if (ocupante && ocupante.numero !== p.numero) return fallar(`El asiento ${datos.asiento} ya es de ${ocupante.nombre}`);
  p.nombre = datos.nombre;
  p.edad = Number(datos.edad);
  p.asiento = datos.asiento;
  return responder({ ...p }, `Reserva #${numero} actualizada`);
};

// Eliminar: findIndex da la posición; splice(posición, 1) quita 1 elemento
API.eliminar = (numero) => {
  const posicion = reservasDemo.findIndex((r) => r.numero === Number(numero));
  if (posicion === -1) return fallar(`No existe la reserva #${numero}`);
  const [quitado] = reservasDemo.splice(posicion, 1);
  return responder(quitado, `Reserva #${numero} cancelada: el asiento ${quitado.asiento} quedó libre`);
};

// Volver a los 12 pasajeros iniciales
API.restaurar = () => {
  reservasDemo = RESERVAS_INICIALES.map((p) => ({ ...p }));
  siguienteNumero = 1013;
  return responder(null, "Se restauraron las 12 reservas de ejemplo");
};

// El panel de progreso no existe en modo demo
API.progreso = () => responder(null);
