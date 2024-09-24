/*
Proyecto caja: 
Ejercicio 1: Crear un proyecto segun las especificaciones mostradas a continuacion.
La formula es: Volumen = ancho * alto * profundidad
 */
package caja;

public class Caja {     // Clase publica caja
    
   // Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundidad;
    
    // Metodos y constructores (Acciones)
    public Caja(){  // Constructor 1 (vacio)       
    }
    
    // Constructor con parametros
    public Caja(int ancho, int alto, int profundidad){  // Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    
    public int calcularVolumen(){ // Metodo para calcular
        return ancho * alto * profundidad;
    }
}
