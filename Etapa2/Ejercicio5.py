## Conversión tupla ↔ lista
## Crea una tupla con (1, 2, 3, 4).
## Convierte la tupla en una lista.
## Modifica el tercer elemento de la lista.
## Convierte de nuevo a tupla y muéstrala.

print('#---------------------------- Ejercicio N° 5 -----------------------------#')
print('#------------------------- Conversion Tupla ↔ lista ----------------------#','\n')

datos = (1,2,3,4)

print(f"La tupla creada es la siguiente: {datos}",'\n')
lista = list(datos)

print(f"Ahora la vamos a convertir en una Lista: {lista} ",'\n')

print("Tenemos que modifcar el tercer elemento de la lista: ",'\n')
while True:  
    try:
        lista[2]=int(input("Por favor ingresa un entero : "))
        break
    except ValueError:
        print("¡Entrada incorrecta! Por favor, ingresa un número entero.")

print(f"La Lista con el tercer valor modificado: {lista} ",'\n')

datos = tuple(lista)
print(f"Finalmente vamos a convertir la Lista en una Tupla: {datos}",'\n')

print("Prestar atencion a las llaves, cuando es una tupla se muestra entre () y cuando se la convierte a lista se muetra entre []",'\n')