def crear_password(nombre, anio):
    contra =''
    if len(nomb)>3:
        for i in range(0,3):
            contra += nombre[i]
        contra += anio + '!'
    elif len(nomb) < 3:
        contra = '_' + nombre + anio + '!'
    else:
        contra = nombre + anio + '!'

    return contra

print('#---------------------------- Ejercicio N° 5 -------------------------------#')
print('#-------------------- Generador de contraseñas simples ---------------------#','\n')

print('Vamos a generarte una contraseña ')
print('')

an = input('Ingresa un año: ')
nomb = input('Ingresa tu nombre: ')

print('')
print('La contraseña creada fue:',crear_password(nomb,an))
print('')
print("Gracias por utilizar la aplicacion.")
print('')