def sumar2(a = 0, b = 0):  # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en funciones
def listarNombres(*nombres):       # Normalmente se utiliza: *args
    for nombre in nombres:      # Se va a convertir en una tupla
        print(nombre)

listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listarNombres('Mario', 'Melina', 'Ale')


# Argumentos variables para un diccionario
def listarTerminos(**terminos):  # Lo mas utilizados es **kwargs para recibir los argumenos
    for llave, valor in terminos.items():  # kwargs significa: key word argument
        print(f'{llave}: {valor}')
        
listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Develoment Enviroment', PK='Primary Key')
listarTerminos(Nombre='Leonel Messi')


# Lista de elementos con funciones (convertir)
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10, 11)  // No es un objeto iterable
desplegarNombres((10, 11)) # La convertimos a una tupla (si es un solo elemento, no olvidar la coma)
desplegarNombres([22, 55]) # La convertimos en una lista


# Funciones recursivas
def factorial(numero):
    if numero == 1:  # caso base
        return 1
    else:
        return numero * factorial(numero-1)  # caso recursivo
    
# resultado = factorial(5)  # Lo hacemos en codigo duro
# print(f'El factorial del numero 5 es: {resultado}')  # Tarea: que el usuario ingrese el numero para calcular el factorial

# TAREA

numero_usuario = int(input("Ingresa un número para calcular su factorial: "))

# Calcular el factorial usando el número ingresado por el usuario
resultado = factorial(numero_usuario)

# Mostrar el resultado
print(f'El factorial del número {numero_usuario} es: {resultado}')
