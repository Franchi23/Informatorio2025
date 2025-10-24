import os
print('#---------------------------- Ejercicio N° 6 -------------------------------#')
print('#--------------------- CONTADOR DE PALABRAS Y LETAS ------------------------#','\n')
cPalabras =1
cLetras=0

while True:
    print('Vamos a contar la cantidad de Palabras y Letras de una frase','\n')
    palabra= str(input("Ingrese una frase por favor; presiona Enter para finalizar: "))
    pal = palabra.split()

    for n in palabra:
        if  ('a' <= n <= 'z' or 'A' <= n <= 'Z')  and not (n.isdigit()) and not (n.isspace()):
           cLetras+=1

        if (n.isspace()):
            cPalabras+=1

    print('')
    print(f'La cantidad de Palabras que hay es: {cPalabras}')
    print(f'La cantidad de letras que hay es: {cLetras}') 
    print('')
    print(f'La cantidad de Palabras que hay usando la funcion Split: {len(pal)}') 
    print('')

    respuesta = input('¿Desea volver a ejecutar el programa: S - N?')
    if respuesta == 'N' or respuesta =='n':
        print('')
        print("Gracias por utilizar la aplicacion.")
        print('')
        break
    else:
        os.system('cls')    #Limpia la Pantalla
        cPalabras=0          #Reinicio los contadores. Se vuelve a ejecutar la aplicacion
        cLetras=0
