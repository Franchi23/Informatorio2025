## 3. Métodos útiles ##
## Crea una lista con números desordenados:
## numeros = [8, 3, 1, 7, 2, 3]
## Usa .count() para saber cuántas veces aparece el 3.
## Usa .index() para obtener la posición del 7.
## Ordena la lista con .sort() y muéstrala.
## Invierte el orden con .reverse() y muéstrala de nuevo.

print('#---------------------------- Ejercicio N° 3 ----------------------------#')
print('#---------------------------- Metodos Utiles ----------------------------#','\n')

numeros =[8, 3, 1, 7, 2, 3]

print(f'Esta es la lista en la cual trabajaremos {numeros}','\n')
print(f'El N° 3 aparece {numeros.count(3)} veces')
print(f'El N° 7 esta en la posicion {numeros.index(7)} o en la posicion {numeros.index(7)+1} si contamos desde 1' ,'\n')
numeros1 =sorted(numeros)       #crea una nueva lista ordenada sin tocar la original
print(f'Ahora ordenamos la lista {numeros1}')
numeros.reverse()
print(f'Finalmente invertimos el orden de la lista {numeros}')

# numeros.sort()     
# print(f'Ahora ordenamos la lista {numeros}')
# numeros.reverse()
# print(f'Finalmente invertimos el orden de la lista {numeros}')

