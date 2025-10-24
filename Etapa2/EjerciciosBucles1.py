#Numero Mayor, Menor y promedio

print('#---------------------------- Ejercicio N° 1 ------------------------------#')
print('#--------------------------- Mayor, Menor, Promedio -----------------------#','\n')

n= int(input("Ingrese la Cantidad de Numeros: "))
print('')
max=0
min=10000
prom=0
aux=0
i=0 

while i <n:
    aux =int(input(f'Ingresa el {i+1} Numero: '))

    if (aux> max):
        max= aux
    
    if (aux< min):
        min= aux

    prom+=aux
    i+=1

print('')
print(f'El Maximo valor es: {max}')
print(f'El Minimo valor es: {min}')
print(f'El promedio de los {n} numeros ingresados es: {round(prom/n,2)}')
print('')