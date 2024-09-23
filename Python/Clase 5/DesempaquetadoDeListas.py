# Desempaquetado de listas o List Unpacking

def show (name, lastName):
    print(name+' '+lastName)
person = ['Ariel', 'Betancud']
show(person[0], person[1])  # Pasamos uno por uno los datos de la lista a la funcion
show(*person)  # Esto es lo mismo que lo anterior pero le pasamos todo junto (Mas resumido)

# Tuplas
person2 = ('Osvaldo', 'Giordanini')  # Desempaquetamos a traves de una tupla
show(*person2)

# Diccionario
person3 = {'lastName': 'Lucero', 'name':'Natalia'}
show(**person3)
