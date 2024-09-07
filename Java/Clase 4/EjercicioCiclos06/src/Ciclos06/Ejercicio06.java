// Resuelto con la clase JOptionPane

package Ciclos06;

import javax.swing.JOptionPane;

public class Ejercicio06 {
    public static void main(String[] args) {
        
        int numero, suma = 0;                   //Declaramos variables
        
        do{
                                                                                              // Pedimos que ingrese el numero
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));     // Y lo guardamos aqui mismo. Con  
                                                                                              // la clase JOptionPane.
                                                               
                                                               // La clase JOptionPane nos permite mostrar un dialogo grafico con
                                                               // el que podemos interactuar para introducir la informacion que queramos.
            
            suma+= numero;  // Los numeros que vamos ingresando se deben ir sumando
            
        }while(numero != 0);
        
        JOptionPane.showMessageDialog(null,"La suma de todos los numeros ingresados es: "+suma);
    }
}
