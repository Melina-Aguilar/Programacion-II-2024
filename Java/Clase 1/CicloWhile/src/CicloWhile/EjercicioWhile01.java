package CicloWhile;

public class EjercicioWhile01 {
   
    public static void main(String[] args){
  
//              --- Ciclo While ---

        var conteo = 0;     // Inferencia de tipos
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++;     // Vamos aumentando en uno la variable
        }
  
        
 //             --- Ciclo Do While ---
 
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 3);
        
        
  //               --- Ciclo For ---
  
  // for(declarar variable de tipo contador;  condicion; incremento o decremento)
        for(var contando = 0; contando < 4; contando++){
            System.out.println("contando = " + contando);
        }
    }        
}
