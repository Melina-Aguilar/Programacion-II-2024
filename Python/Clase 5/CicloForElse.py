numbers = [1, 2, 3, 4, 5]  # Se creo lista
for n in numbers:   # la recorro
    print(n)
    if n == 3:
        break   # Esta es la unica manera para que no se muestre el 'else'
else:
    print('Esto se termino')  # Termina de recorrer for, y termina ejecutandose el else