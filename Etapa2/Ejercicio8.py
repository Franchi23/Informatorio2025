# 8. Crear y acceder
# Crea un diccionario con tus datos:{"nombre": "Ana", "edad": 25, "ciudad": "Resistencia"}
# Accede y muestra cada valor por su clave.
# Cambia la edad por otro número.
# Agrega una nueva clave "profesion".

print('#---------------------------- Ejercicio N° 8 -----------------------------#')
print('#--------------------- Trabajando con Diccionarios - Dict ----------------#','\n')

dicc ={"Nombre": "Ana", "Edad": 25, "Ciudad": "Resistencia"}
print("Creamos un Diccionario. Ahora te lo muestro ...........")

for clave,valor in dicc.items():     # imprime las claves y los valores
    print(f'Clave: {clave} - Valor: {valor}')

# for clave,valor in dicc.items():     
#     print(f'{clave}: {valor}')
print("")
print("Ahora te muestro cada valor por su clave")
for valor in dicc.values():     # Solo imprime los valores
    print(valor)

print("")
print("Ahora vamos a cambiar la edad.",'\n')

## -----------------------------------------------------------------------
# Bucle infinito hasta que se obtenga un entero
while True:  
    try:
        dicc['Edad']=int(input("Por favor ingresa la edad, debe ser un numero entero : "))
        break
    except ValueError:
        print("¡Entrada incorrecta! Por favor, ingresa un número entero.")
## -------------------------------------------------------------------------

print("")
print("Ahora vamos a ingresar otra clave, la profesion.",'\n')

dicc['Profesion']=str(input("Por favor ingresa una profesion : "))

print("")
print("Habiendo modificado la edad e ingresado la profesión, el diccionario quedo de la siguiente manera: ")

for clave,valor in dicc.items():     
    print(f'{clave}: {valor}')
print("")