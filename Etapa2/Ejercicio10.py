# Una lista con tres nombres.
# Una tupla con tres edades (una por cada nombre).
# Un diccionario que use cada nombre como clave y la edad correspondiente como valor.
print('#---------------------------- Ejercicio N° 10 -----------------------------#')
print('#--------------------------- Combinando Estructuras -----------------------#','\n')

print("Primero vamos a crear una Lista con tres Nombres que te ire pidiendo que los ingreses.")
nombres =[]
for i in range(0,3):
    nombres.append(input(f'Ingresa el {i+1} nombre: '))

print('Lista resultante: ',nombres,'\n')

edad=[]
#creo una lista para ingresar las edades y despues la convierto a una tupla
print("Ahora vamos a crear una tupla con las edades de las personas que ingresante anteriormente. Te ire pidiendo que las ingreses.")
for i in range(0,3):
    while True:  
        try:
            edad.append(input(f'Ingresa la edad de {nombres[i]} : '))
            break
        except ValueError:
            print("¡Entrada incorrecta! Por favor, ingresa un número entero.")

edades = tuple(edad)
print("")
print(f'Ahora muestramos la tupla cargada con las edades. {edades}','\n')
print('Prestar atencion a las llaves, cuando es una tupla se muestra entre () y la lista se muetra entre []','\n')

print("Finalmente armamos un diccionario con los valores de la lista de nombres y la tupla con las edades.")
        # una forma facil de crear el diccionario y obviar mucho codigo
        #diccionario = dict(zip(nombres, edades))

#Creo un lista vacia para ir ingresando los nombres y las edades a esa lista de la forma ('clave', 'valor')
#para despues cargarla al diccionario
lista_aux=[]

for i in range(0,3):
    lista_aux.append((nombres[i],edades[i]))

#Creo el diccionario con los valores de la lista aux que son del tipo ("Clave", "Valor")
diccionario = dict(lista_aux)

for clave,valor in diccionario.items():     
    print(f'Clave: {clave} -- Valor: {valor}')

print('')
print('*' * 90)










