// Metodo Aplly
// Este método nos permite llamar a un método que no se encuentra definido en cierto objeto.
// Apply lee el arreglo y lo está asignando como argumentos. La única diferencia entre call
// y Apply es que a call se le pasan directamente los argumentos y Apply va necesitar que 
// tengamos a disposición un arreglo en el que estarán ingresados como elementos de ese arreglo los argumentos

let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic.','342424352'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '+24342342'));

// Metodo apply
let arreglo = ['Ing.', '4244245435'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));


