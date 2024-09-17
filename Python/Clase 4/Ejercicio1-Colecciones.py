# Ejercicio 1: Eliminar duplicados de una lista.
# Escriba un programa donde tenga una lista y que a continuacion elimine
# los elementos repetidos, por ultimo mostrar la lista.

# Creamos una lista

lista = [1, 2, 3, 2,'Melina', 7, 7, 3, 'Ale', 5, 'Ariel']

# Convertimos la lista a un conjunto (set) y de esta forma se eliminan 
# los elementos duplicados.
# Porque set no permite elementos duplicados.

conjunto = set(lista)

lista = list(conjunto) # Convertimos el conjunto a una lista, neuvamente.
print(lista)




# La converesion hecha en una sola linea de codigo (eficiente)

lista1 = [1, 2, 3, 2,'Melina', 7, 7, 3, 'Ale', 5, 'Ariel']
lista1 = list(set(lista1))  # Set convierte la lista a conjuntos, y con 'list' volvemos a lista.
print(lista1)