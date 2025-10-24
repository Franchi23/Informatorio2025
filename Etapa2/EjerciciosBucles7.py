print('#---------------------------- Ejercicio N° 7 -------------------------------#')
print('#------------------------- SECEUENCIA CRECIENTE ----------------------------#','\n')

print('Vamos a verificar si una secuencia de numeros fue ingresada en orden creciente.','\n')
n=int(input("Primero te voy a solicitar cuantos numeros queres que tenga la secuencia: "))
print(f'Perfecto, ahora te voy a ir solicitando que ingreses los {n} numeros: ')
aux = []
c=0

for i in range (0,n):
    aux.append(int(input(f'Ingresa el {i+1} Numero: ')))
    if (i > 0):
        if (aux[i-1] > aux[i]):
            c=1                 #el nro anterior es mayor al ingresado, no se cumple la condicion

print('')

if (c==1):
    print('Los numeros NO fueron ingresados estrictamente en orden creciente','\n')
else:
    print('Los numeros fueron ingresados estrictamente en orden creciente','\n')
    
print(aux)
print('')
print("Gracias por utilizar la aplicacion.")
print('')