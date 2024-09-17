# Ejercicio 3: Agregar personajes a una lista.
# Escriba un programa donde cree una lista con los siguientes personajes
# del Señor de los anillos.

# Nombre: Aragon
# Clase: Guerrero
# Raza: Dunadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = []  # Creamos una lista vacia.

# Creamos diccionarios
P1 = {'Nombre': 'Aragorn', 'Clase': 'Guerrero', 'Raza': 'Dunadan del Norte'}
personajes.append(P1)  # Agregamos a la lista un personaje

P2 = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P1)

P3 = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P1)

P = {'Nombre': 'Sauron', 'Clase': 'Guerrero', 'Raza': 'Ainur y Maiar'}
personajes.append(P)

P = {'Nombre': 'Galadriel', 'Clase': 'Mago', 'Raza': 'Elfos Noldor'}
personajes.append(P)

P = {'Nombre': 'Frodo', 'Clase': 'Mago', 'Raza': 'Hobbit'}
personajes.append(P)

# Se puede borrar los numeros de 'P1' P3, y re utilizar la variable

print(personajes)