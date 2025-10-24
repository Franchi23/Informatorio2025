import os
print('#---------------------------- Ejercicio N° 10 -------------------------------#')
print('#---------------------------- NUMERO PERFECTO -------------------------------#','\n')

while True:
    print('Vamos a determinar si un numero ingresado es un numero perfecto.','\n')
    n=int(input("Te voy a solicitar que ingreses el Numero a determinar : "))
    perfect=0

    print('')
    divisores = []
    for i in range(1, n - 1):
        if n % i == 0:
            divisores.append(i)
            perfect+=i

    print(f'Los Divisores del Numero {n} son: {divisores}','\n')
    if (n == perfect):
        print(f'Entonces, el Numero: {n} es un NUMERO PERFECTO. La suma de sus divisores, excluyéndose a sí mismo es: {perfect} ')
    else:
        print(f'Entonces, el Numero: {n} NO es un numero perfecto. La suma de sus divisores, excluyéndose a sí mismo es: {perfect}')

    print('')
    try:
        op = int(input("Desea volver a ejecutar el menu 1-Si / 0-No : "))     
        if (op == 0):
            break
        else:
            os.system('cls')    #Limpia la Pantalla
    except ValueError:
        print("¡Entrada incorrecta! Por favor, ingresa un número entero.")    

print('')
print("Gracias por utilizar la aplicacion.")
print('')