import os
print('#---------------------------- Ejercicio N° 3 -------------------------------#')
print('#------------------- Contador de Vocales, Consonantes y mas ----------------#','\n')

cVocales =0
cConso =0
c=0
s=0
vocales = ['a','e','i','o','u','A', 'E', 'I', 'O','U']

while True:
    print('Vamos a contar la cantidad de vocales y consonantes de una palabra o frase','\n')
    palabra= str(input("Ingrese una palabra o frase; presiona Enter para finalizar: "))

    for n in palabra:
        if  ('a' <= n <= 'z' or 'A' <= n <= 'Z')  and not (n.isdigit()):
            if (n in vocales):
                cVocales+=1
            else:
                cConso+=1

        if not (n.isspace()):
            c+=1
        else:
            s+=1

    print('')
    print(f'La cantidad de Vocales que hay es: {cVocales}')
    print(f'La cantidad de Consonantes que hay es: {cConso}') 
    print(f'La cantidad de caracteres ingresados es: {c}')
    print(f'La cantidad de espacios en blanco ingresados es: {s}')
    print('')

    respuesta = input('¿Desea volver a ejecutar el programa: S - N?')
    if respuesta == 'N' or respuesta =='n':
        print('')
        print("Gracias por utilizar la aplicacion.")
        print('')
        break
    else:
        os.system('cls')    #Limpia la Pantalla
        cVocales=0          #Reinicio los contadores. Se vuelve a ejecutar la aplicacion
        cConso=0
        c=0
        s=0
    
