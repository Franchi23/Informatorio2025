# # SUMA DE PARES E IMPARES

print('#---------------------------- Ejercicio N° 2 -------------------------------#')
print('#--------------------------- Suma de Pares e Impares -----------------------#','\n')

n= int(input("Ingrese la Cantidad de Numeros: "))
print('')
pares=0
impares=0
i=0 
lista=[]

while i < n:
    #aux =int(input(f'Ingresa el {i+1} Numero: '))
    lista.append(int(input(f'Ingresa el {i+1} Numero: ')))
    if (lista[i] % 2) == 0:
        pares+= lista[i]
    else:
        impares+=lista[i]
    i+=1

print('')
lista.sort()    #ordeno la lista para mostrarla de menor a mayor
print(f'Los Numeros ingresados fueros: {lista}')
print(f'La Suma de los Numeros pares ingresados es: {pares}')
print(f'La Suma de los Numeros impares ingresados es: {impares}')
print('')