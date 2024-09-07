// instancia = objeto.  " Crear instancias = Crear objetos "
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona();  // Cuando ponemos 'Persona()' estamos llamando al constructor.
                                   // Cuando se asocia la variable 'persona1' al constructor 'Persona()' 
                                   // esa variable 'persona1' pasa a ser un OBJETO.
                                   
                                   // El constructor es un metodo especial donde reserva memoria para poder
                                   // crear objetos. Al crear el objeto, el constructor le regresa la referencia
                                   // donde se creo el objeto y se lo asigna a la variable. Una vez hecho esto,
                                   // se puede acceder a los atributos y metodos de la clase 'Persona'.
                                   
        persona1.nombre = "Ariel";          // Accedemos a los atributos gracias al constructor
        persona1.apellido = "Betancud";
        persona1.obtenerInformacion();      // Llamamos al metodo.
        
        //Creamos un nuevo objeto
        Persona persona2 = new Persona();
        System.out.println("persona2= "+persona2);  // Con esto vemos la direccion de memoria donde estan alojados.
        System.out.println("person1= "+persona1);   // tienen un valor hexadecimal.
     
        persona2.obtenerInformacion();  // Nos da el valor 'null', porque no le cargamos ningun valor a los atributos.
        
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion();  // Ahora si tiene valores cargados.
    }
}

// ENTONCES...
// El constructor 'Persona()' convirtio en OBJETO a 'persona1'
// Una vez hecho esto, a traves del objeto 'persona1' accedenos a los atributos 'nombre , apellido' y le asignamos un valor a cada uno.
// Ahora el objeto tiene caracteristicas => 'Ariel, Betancud'.
// Luego, con esta informacion llamamos al metodo 'obtenerInformacion', los recibe y los imprime.


