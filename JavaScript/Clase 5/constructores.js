// El constructor es una función especial que se trabajará con objetos en JavaScript. 
// Para llamar una funciónconstructor se utilizará la palabra reservada new lo que
// reservará espacio en memoria del objeto que se creará. Se recomienda que el nombre 
// de la función empiece co mayúscula.

function Persona3(nombre, apellido, email){  // constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;

    // Agregamos una funcion
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}

let padre = new Persona3('Leo', 'Lopez', 'leo@gmail.com'); // creo objeto
padre.nombre = 'Luis';  // Se puede modificar
padre.telefono = '23424342'; // propiedad exclusiva del objeto
console.log(padre);
console.log(padre.nombreCompleto()); // Utilizamos la funcion

let madre = new Persona3('Laura', 'Caro', 'lau@gmail.com') // otro objeto
console.log(madre);
console.log(madre.telefono);  // La propiedad no esta definida
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos
// Caso objeto 1:
let miObjeto = new Object(); // Opcion formal

// Caso objeto 2:
let miObjeto2 = {}; // Breve y recomendada

// Caso String 1:
let miCadena1 = new String('Hola');  // Sintaxis formal

// Caso String 2:
let miCadena2 = 'Hola'; //Sintaxis simplificada y recomendada

// Caso con numeros 1
let miNumero = new Number(1);  // Formal, no recomendable

// Caso con numeros 2
let miNumero2 = 1;  // Sintaxis recomendada

// Caso boolean 1
let miBoolean1 = new Boolean(false);  // Formal

// Caso boolean 2
let miBoolean2 = false;  // Sintaxis recomendada

// Caso arreglos 1
let miArreglo1 = new Array(); // Formal

// Caso arreglos 2
let miArreglo2 = []; // Sintaxis recomendada

// Caso funcion 1
let miFuncion1 = new function(){} // todo despues de new es considerado objeto

// Caso funcion 2
let miFuncion2 = function(){}; // Notacion simplificada y recomendada



// Uso de prototype
// A través de él se ingresa una propiedad para todos los objetos que formen parte de la función

Persona3.prototype.telefono = '2343243';
console.log(padre);
console.log(madre);
madre.telefono = '34093942';  // se puede modificar
console.log(madre.telefono);


// Uso de call
// Esta función permite llamar un método que está definido en un objeto desde otro objeto.

let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic.','342424352'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '+24342342'));
