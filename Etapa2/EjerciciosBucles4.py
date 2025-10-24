import os
print('#---------------------------- Ejercicio N° 4 -------------------------------#')
print('#------------------- Busqueda de nombre en Lista - Break -------------------#','\n')

nombres =['Francisco', 'Paula', 'Santiago', 'Jose', 'Belen', 'Valeria', 'Eduardo','Noelia']
resultado =''
print('Hay una lista de nombres y vamos a buscar si aparece el nombre que ingreses','\n')
salida = False

while True:

    if (salida == True):
        break

    buscado= str(input("Ingrese el nombre a buscar: "))

    for nombre in nombres:    
        if nombre.lower() == buscado.lower():
            resultado = nombre
            break

    print('')
    if (resultado != ''):
        print(f'Se encontro el nombre: {resultado} en la lista','\n')
    else:
        print(f'No se enecontro el nombre {buscado}', '\n')

    
    while True:
        respuesta = input('¿Desea volver a ejecutar el programa: S - N?')
        if respuesta == 'N' or respuesta =='n':
            print('')
            print("Gracias por utilizar la aplicacion.")
            print('')
            salida = True
            break
        elif respuesta != 'S' and respuesta !='s':
            print('Ingreso otra tecla. Por favor verifique e ingrese S o N')  
            salida=False      
        else:
            os.system('cls')    #Limpia la Pantalla
            resultado=''
            respuesta=''
            break
            
