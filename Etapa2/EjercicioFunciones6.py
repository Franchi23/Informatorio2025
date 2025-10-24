def contar_vocales(palabra):
    cVocales =0
    vocales = ['a','e','i','o','u','A', 'E', 'I', 'O','U']

    for n in palabra:
        if  ('a' <= n <= 'z' or 'A' <= n <= 'Z'):
            if (n in vocales):
                cVocales+=1
 
    return cVocales

print('#---------------------------- Ejercicio N° 6 -------------------------------#')
print('#--------------------------- Contador de Vocales ---------------------------#','\n')

print('Vamos a contar la cantidad de vocales de una palabra o frase','\n')
palabra= str(input("Ingrese una palabra o frase; presiona Enter para finalizar: "))
print('')

print('')
print('La cantidad de vocales que hay en la franse ingresasda es:',contar_vocales(palabra))
print('')
print("Gracias por utilizar la aplicacion.")
print('')