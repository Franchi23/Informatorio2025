# Crea un diccionario con tres pares clave–valor.
# Usa .keys() para mostrar las claves.
# Usa .values() para mostrar los valores.
# Usa .items() para mostrar todo como pares.
# Elimina un elemento con .pop() y muestra el diccionario final.

print('#---------------------------- Ejercicio N° 9 -----------------------------#')
print('#---------------------- Metodos de  Diccionarios - Dict ------------------#','\n')

claves= ['Nombre', 'Tipo', 'Sexo']
mascotas = dict.fromkeys(claves)

print("Vamos a crear un diccionario de tu mascota con el nombre, el tipo de animal y su sexo.")
print(mascotas)
print("Te muestro, solo tiene las claves. Ahora te voy solicitar que ingreses los valores.")

mascotas['Nombre']=input("Ingresa el nombre de tu mascota: ")
mascotas['Tipo']=input("Ingresa el el tipo de animal de tu mascota: ")

## ---------------------------------------------------------------------------------------------------------------
valores = ('M','F','m','f')
while True:  
    try:
        s=str(input("Ingresa el sexo de tu mascota: (M o F): "))
        if s in valores:
            mascotas['Sexo']=s
            break
        else:
            print("¡Entrada incorrecta! Por favor, ingresa solo un caracter M para Masculino o F para Femenino.")
    except ValueError:
        print("¡Entrada incorrecta! Por favor, ingresa solo un caracter M para Masculino o F para Femenino.")
## ---------------------------------------------------------------------------------------------------------------

print("Listo, ya tenemos el diccionario de tu mascota hecho. Ahora lo vamos a ver de distintas formas.")

print ("Solo las claves")
for valor in mascotas.keys():     #  imprime las claves
    print(valor)

print('')

print ("Solo los Valores")
for valor in mascotas.values():     #  imprime los valores
    print(valor)

print('')

print ("Las Claves y sus Valores")
for clave,valor in mascotas.items():     #  imprime las claves y los valores
    print(f'Clave: {clave} -- Valor: {valor}')

print('')

print('Finalmente debemos eliminar una de las tres claves del diccionario.')

valores = (1,2,3)
while True:  
    try:
        s=int(input("Por favor elegi cual queres eliminar, para Nombre-1, para Tipo-2 o Sexo-3 : "))
        if s in valores:
            match s:
                case 1:
                    mascotas.pop('Nombre')
                    print('Eliminamos el Nombre.')
                    break
                case 2:
                    mascotas.pop('Tipo')
                    print('Eliminamos el Tipo.')
                    break
                case 3:
                    mascotas.pop('Sexo')
                    print('Eliminamos el Sexo.')
                    break
                case _:   
                    print("¡Entrada incorrecta! Por favor, ingresa un numero entero (1,2 o 3).")
        else:
            print("¡Entrada incorrecta! ingresa un numero entero (1,2 o 3).")
    except ValueError:
        print("¡Entrada incorrecta! Por favor, ingresa un numero entero (1,2 o 3)")

print('')
print('Despues de eliminar una de las tres claves del diccionario. Quedo de la siguiente manera: ')
for clave,valor in mascotas.items():     
    print(f'Clave: {clave} -- Valor: {valor}')

print('')
print('*' * 90)





