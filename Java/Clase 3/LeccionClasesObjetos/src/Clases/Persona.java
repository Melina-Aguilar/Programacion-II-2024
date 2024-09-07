// Una clase es una plantilla, de la cual vamos a poder crear "objetos"
// Clase persona: tiene atributos y metodos
// La clase es un "molde" donde podemos crear uno o mas objetos.
// en objetos se define a la "persona"


// Un metodo es un codigo que podemos reutilizar, por esto, podemos llamarlo las vecse que sea
// necesario. 
// Un metodo puede recibir valores, conocidos como 'argumentos' 
// Un metodo puede regresar un valor, conocido como 'valor de retorno', tambien puede volver a
// nuestro metodo.


package Clases;

public class Persona {  // 'Persona' es un constructor. Sirve para poder crear un objeto de la clase.
    
   // Atributos de la clase (Caracteristicas)
    String nombre;
    String apellido;
    
    // Metodos de la clase (Acciones)
    public void obtenerInformacion(){ // 'public' indica que el metodo se puede utilizar fuera de esta clase. 
                                      // 'void' indica que no regresa ningun tipo de informacion.
                                      // '()' indica que podemos recibir informacion (argumentos). 
                                      
        System.out.println("Nombre: "+nombre);  // 'nombre' no es simplemente una variable. Es un atributo de la clase.
                                                // y no importa que no se defina dentro del metodo, porque al ser
                                                // un atributo se puede utilizar dentro de cualquier metodo definido
                                                // dentro de la clase.
        System.out.println("Apellido: "+apellido);                                    
    }
}
