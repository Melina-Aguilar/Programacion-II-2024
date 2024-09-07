/*
Ejercicio 6: Pedir numeros hasta que se teclee un 0, mostrar la suma de todos los numeros introducidos.
*/
package Ciclos06;

import java.util.Scanner;

public class Ciclos06 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, suma = 0;                   //Declaramos variables
        
        do{
            System.out.println("Digite un numero: ");          // Pedimos que ingrese el numero
            numero = Integer.parseInt(entrada.nextLine());     // Lo guardamos aqui. Para esto necesitamos 
                                                               // la clase Scanner, lo creamos en la linea 10.
                                                               
                                                               // La clase Scanner nos permite capturar datos del  tipo
                                                               // int, double, string, etc.
            
            suma+= numero;  // Los numeros que vamos ingresando se deben ir sumando
            
        }while(numero != 0);
        
        System.out.println("La suma de todos los numeros ingresados es: "+suma);
    }
}
