# 6. Crear conjuntos
# Crea un conjunto con los números 1, 2, 3, 3, 2.
# Muestra el conjunto (debería eliminar duplicados).
# Agrega el número 4 con .add().
# Elimina el 2 con .remove().

print('#---------------------------- Ejercicio N° 6 -----------------------------#')
print('#---------------------------- Crear Conjuntos ----------------------------#','\n')

print("Vamos a crear la estructura de datos llamada Conjuntos o Set con los siguientes valores: 1, 2, 3, 3, 2")
conjunto = {1, 2, 3, 3, 2}
print("Recuerda que los Conjuntos o Set no aceptan duplicados ☺ ",'\n')
print(f"Este es nuestro Conjunto o Set: {conjunto} ",'\n')

conjunto.add(4)
print(f"Ahora vamos a agregar el N° 4 al conjunto, el cual quedaria asi: {conjunto} ",)

conjunto.remove(2)
print(f"Ahora vamos a eliminar el N° 2 de conjunto. Este es el Conjunto o Set final: {conjunto} ",'\n')

