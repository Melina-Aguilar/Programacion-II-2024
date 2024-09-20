// El método GET permite solicitar información 
// desde un servidor, y el servidor responde con los datos solicitados.

// El método set se utilizará para modificar los valores de los objetos.
// Se combinará el uso del set con el uso del get.

let persona = {   // Se le asigna un espacio de memoria a 'persona'
    // Ingresamos atributos
    nombre: 'Carlos',
    apellido: 'Lopez',
    email: 'carlos@gmail.com',
    edad: 28,
    idioma: 'ES',

    get lang(){
        return this.idioma.toUpperCase();  // Convierte las minusculas en mayusculas
    },

    set lang(lang){
        this.idioma = lang.toUpperCase();
    },

    // Agregar metodo para imprimir el nombre completo -->  concatenar
    nombreCompleto: function(){  // Metodo o funcion en JS
        return this.nombre+' '+this.apellido;
    },

    get nombreEdad(){  // Este es el metodo get
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    },

}

console.log('Comenzamos a utilizar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);