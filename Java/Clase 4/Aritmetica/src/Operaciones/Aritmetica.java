// Atributos y metodos comienzan con minusculas, para diferenciarlos con las clases que empiezan con mayusculas.

package Operaciones;

public class Aritmetica {        // Para la clase usamos nomenclatura 'PascalCase'
    // Atributos de la clase
    int a;
    int b;
    
    // Metodo
    public void sumarNumeros(){  // Para metodos y atributos usamos nomenclatura 'camelCase'
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
}
