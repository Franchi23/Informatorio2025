# Crea una lista con elementos repetidos:
# animales = ["perro", "gato", "perro", "pájaro", "gato"]
# Convierte la lista en un conjunto para eliminar duplicados.
# Convierte el conjunto de vuelta a lista.
# Muestra la lista final.


print('#---------------------------- Ejercicio N° 7 -----------------------------#')
print('#---------------------- Conversión lista ↔ conjunto ----------------------#','\n')

animales = ["perro", "gato", "perro", "pájaro", "gato"]
print(f"Creamos una lista de animales con elementos repetidos: {animales}")

conjunto= set(animales)
print(f"Ahora vamos a convertir la lista en un conjunto o set asi eliminamos los duplicados: {conjunto} ")

animales.clear()     # Metodo para eliminar todos los elementos de la lista - para provar - no es necesaria esta linea
animales=list(conjunto)     
print(f"Ahora convertimos el conjunto en una lista: {animales}",'\n')

print("Prestar atencion a las llaves, cuando es una lista se muetra ente [] y cuando se la convierte a conjnto cambia a {}")
