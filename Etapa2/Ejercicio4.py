## Crea una tupla con (nombre, edad, ciudad) y desempaquétala en 3 variables.
## Imprime cada variable por separado.

print('#---------------------------- Ejercicio N° 4 ----------------------------#')
print('#------------------------- Desempaquetado - Tuplas ----------------------#','\n')

print('Vamos a crear una Tupla con los siguientes datos que tendra que ingresar: ','\n')
nombre = input("Ingrese el Nombre: ")
edad = input("Ingrese la edad :")
ciudad = input ("Ingrese la ciudad: ")

#datos =('Francisco', 43, 'Resistencia')
datos =(nombre,edad,ciudad)
print("")
print(f"Esta la Tupla que armamos: {datos}",'\n')
print("Ahora vamos a imprimir los datos por separados: ",'\n')
print(f"El nombre es: {datos[0]}")
print(f"La edad es: {datos[1]}")
print(f"La ciudad  es: {datos[2]}",'\n')