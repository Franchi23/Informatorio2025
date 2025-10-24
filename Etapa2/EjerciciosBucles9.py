import os
print('#---------------------------- Ejercicio N° 9 -------------------------------#')
print('#--------------------------- MENU INTERACTIVO ------------------------------#','\n')

op=0
while op in range(0,4):
    print('*' * 50)
    print('         Menu de Operaciones Matematicas')
    print('*' * 50)
    print('         Opciones :')
    print('*' * 50)
    print('         1- Sumar')
    print('         2- Restar')
    print('         3- Multiplicar')
    print('         4- Dividir')
    print('         0- Terminar')
    print('*' * 50)

    try:
        op=int(input('Seleccione que operacion desea efectuar : '))
        print('')
        if (op ==0):
            break

        print('Por favor ingrese 2 Numeros Enteros:')
        n1=int(input('Ingrese el 1° operador: '))
        n2=int(input('Ingrese el 1° operador: '))

        print('')
        if (op == 1):
            print(f'El resultado de sumar {n1} + {n2} es igual a: {n1+n2}')
        elif (op == 2):
            print(f'El resultado de restar {n1} - {n2} es igual a: {n1-n2}')
        elif (op == 3):
            print(f'El resultado de multiplicar {n1} x {n2} es igual a: {n1*n2}')
        elif (op == 4):
            if (n1 >= n2):
                print(f'El resultado de dividir {n1} / {n2} es igual a: {n1/n2}')
            else:
                print(f'No se puede efectuar la division, {n1} es menor que {n2}')
        else:
            print('Opcion invalida - Por favor, ingresa un número entre el 0 y el 4 ')
    except ValueError:
        print("¡Entrada incorrecta! Por favor, ingresa un número entero.")    
           
    print('')
    op = int(input("Desea volver a ejecutar el menu 1-Si / 0-No : "))     
    if (op == 0):
        break
    else:
        os.system('cls')    #Limpia la Pantalla

print('')
print("Gracias por utilizar la aplicacion.")
print('')