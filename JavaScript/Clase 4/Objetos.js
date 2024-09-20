let x = 10;  // Variable de tipo primitiva
console.log(x.length);

console.log('Tipos primitivos');
// Creamos un objeto
let persona = {   // Se le asigna un espacio de memoria a 'persona'
    // Ingresamos atributos
    nombre: 'Carlos',
    apellido: 'Lopez',
    email: 'carlos@gmail.com',
    edad: 30,

    // Agregar metodo para imprimir el nombre completo -->  concatenar
    nombreCompleto: function(){  // Metodo o funcion en JS
        return this.nombre+' '+this.apellido;
    }
}

console.log(persona);
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email)
console.log(persona.edad);

console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');

// Creamos otro objeto
let persona2 = new Object();  // Debe crear un nuevo objeto en memoria.
//Agrego atributos
persona2.nombre = 'Maria';
persona2.direccion = 'Salada 14';
persona2.telefono = 392949239;

console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');

// Como acceder a las propiedades de estos obejtos
console.log(persona['apellido']);  // Accedemos como si fuera un arreglo

console.log('Usamos el ciclo for in');
// for in  --> para acceder a las propiedades de un objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log('Cambiamos y eliminamos un error');
// Agregamos nueva propiedad
persona.apellido = 'Betancud';  // Cambiamos dinamicamente un valor del objeto
persona.nombres = 'Maria';  // error al poner el atributo 'nombres', y se agrega como otro atributo
delete persona.nombres; // eliminamos el error
console.log(persona);


// Distintas formas de imprimir un objeto
// Numero 1: la mas sencilla, concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto:');
console.log('Forma 1:');
console.log(persona.nombre+', '+persona.apellido);

// Numero 2: a traves del ciclo for in
console.log('Forma 2:');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

// Numero 3: La funcion Object.values()  (nos regresa el objeto pero como un arreglo)
console.log('Forma 3:');
let personaArray = Object.values(persona);
console.log(personaArray);

// Numero 4: Utilizaremos el metodo JSON.stringify
console.log('Forma 4:');
let personaString = JSON.stringify(persona);
console.log(personaString);