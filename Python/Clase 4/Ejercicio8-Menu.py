# Ejercicio 8: Menu interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo
# incial de $1000, y tendra el siguiente menu de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo = 1000

while True:
    print('\t.:MENU:.')
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')

    opcion = int(input('Digite una opcion de menu: '))
    print()
    
    if opcion == 1:
        extra = float(input('Cuanto dinero desea ingresar: '))
        saldo += extra
        print(f'Dinero en la cuenta: ${saldo}')
        
    elif opcion == 2:
        retirar = float(input('Cuanto dinero desea retirar: '))
        if retirar > saldo:
            print('No tiene esa cantidad de dinero.')
        else:
            saldo -= retirar
            print(f'Dinero en la cuenta: ${saldo}')
    
    elif opcion == 3:
         print(f'Dinero en la cuenta: ${saldo}')
         
    elif opcion == 4:
        print('Gracias por utilizar su cajero automatico, hasta pronto.')
        break
    else:
        print('Error. Se equivoco de opcion de menu')
        print()