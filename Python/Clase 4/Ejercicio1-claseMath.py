import math  # Importamos la clase MATH para hacer uso de la funcion sqrt(raiz cuadrada)

# Ejercicio de matematicas
# Para sacar la raiz cuadrada de un numero positivo

numero = int(input('Digite un numero positivo: '))

while numero < 0:
    print("Error. Deberia ser un numero positivo.")
    numero = int(input('Digitie un numero positivo: '))

print(f'La raiz cuadrada es: {math.sqrt(numero):.2f}')
