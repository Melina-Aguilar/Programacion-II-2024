# Ejercicio 3: Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el numero 3, debe imprimir:
# 3
# 2
# 1
# Si se ingresan numeros negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero-1) # caso recursivo 
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto...')

# imprimir_numeros_recursivos(1) # TAREA: que el numero lo ingrese el usuario

# TAREA

numero_usuario = int(input("Ingresa un número positivo para imprimir de manera descendente: "))

# Llamamos a la función con el número ingresado por el usuario
imprimir_numeros_recursivos(numero_usuario)
