## Crea una lista vacía y:                      ##
## Agrega tres nombres usando .append().        ##
## Inserta un nombre en la primera posición.    ##
## Elimina el último elemento con .pop().       ##
## Imprime la lista final.                     ##

print('------------------------------ Ejercicio N° 2 ------------------------------')
print('---------------------------- Metodos con Listas ----------------------------','\n')

nombres=[]
print("Se solicitará ingrese 3 nombres para guardarlos en una Lista ",'\n')

for i in range(0,3):
    nombres.append(str(input(f'Ingresa el {i+1} nombre: ')))
    
print('La Lista generada con los nombre ingresados: ',nombres,'\n')

## Inserta un nombre en la primera posición
nombres.insert(0, input('Ahora ingresa 1 nombre mas por favor: '))

print('\n','La nueva Lista generada es: ',nombres,'\n')

## Elimina el último elemento con .pop().

print('Se eliminara el ultimo elemento','\n')
nombres.pop(-1)
print('La Lista final es: ',nombres,'\n')
