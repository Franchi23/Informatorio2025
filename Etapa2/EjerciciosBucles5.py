print('#---------------------------- Ejercicio N° 5 -------------------------------#')
print('#------------------------- VERIFICAR CONTRASEÑAS  --------------------------#','\n')

valor ='python123'
print('Tenes 3 Intentos para ingresar correctamente la contraseña','\n')
contra = ''
salida = False

for i in range(0,3):
    contra = str(input('Por favor ingrese la cotraseña: '))
    if (contra.lower() == valor.lower()):
        salida = True
        break
    else:
        print('Contraseña incorrecta.','\n')

if salida == True:
    print('')
    print('Correcto, contraseña ingresada exitosamente.','\n')
else:    
    print('Se terminaron los intentos permitidos.','\n')

print("Gracias por utilizar la aplicacion.")
print('')