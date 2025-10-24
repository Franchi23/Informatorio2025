## Ejercicios: Listas, tuplas, conjuntos y diccionarios
import sys
op = 99

def Ejercicio1():
    print('\n','---------------------------- Ejercicio N° 1 ----------------------------','\n')
    print('\n','---------------------------- Lista de Colores ---------------------------','\n')
    colores =['Rojo','Verde','Azul',]
    print('La Lista Completa: ',colores,'\n')
    print(f"Primer elemento de la Lista: {colores[0]}, Ultimo elemento de la lista: {colores[-1]}",'\n')
    colores[1]="Amarillo"
    print('Se cambio el segundo elemento por amarillo','\n')
    print('Lista resultante: ',colores,'\n')

def Ejercicio2():
    print('------------------------------ Ejercicio N° 2 ------------------------------')
    print('---------------------------- Metodos con Listas ----------------------------','\n')

    nombres=[]
    print("Se solicitará ingrese 3 nombres para guardarlos en una Lista ",'\n')

    for i in range(0,3):
        nombres.append(input(f'Ingresa el {i+1} nombre: '))
    
    print('La Lista generada con los nombre ingresados: ',nombres,'\n')
    nombres.insert(0, input('Ahora ingresa 1 nombre mas por favor: '))
    print('\n','La nueva Lista generada es: ',nombres,'\n')
    print('Se eliminara el ultimo elemento','\n')
    nombres.pop(-1)
    print('La Lista final es: ',nombres,'\n')

def Ejercicio3():
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

def Ejercicio4():
    print('#---------------------------- Ejercicio N° 4 ----------------------------#')
    print('#------------------------- Desempaquetado - Tuplas ----------------------#','\n')

    print('Vamos a crear una Tupla con los siguientes datos que tendra que ingresar: ','\n')
    nombre = input("Ingrese el Nombre: ")
    edad = input("Ingrese la edad :")
    ciudad = input ("Ingrese la ciudad: ")
    datos =(nombre,edad,ciudad)
    print("")
    print(f"Esta la Tupla que armamos: {datos}",'\n')
    print("Ahora vamos a imprimir los datos por separados: ",'\n')
    print(f"El nombre es: {datos[0]}")
    print(f"La edad es: {datos[1]}")
    print(f"La ciudad  es: {datos[2]}",'\n')

def Ejercicio5():
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

def Ejercicio6():
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

def Ejercicio7():
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

def Ejercicio8():
    print('#---------------------------- Ejercicio N° 8 -----------------------------#')
    print('#--------------------- Trabajando con Diccionarios - Dict ----------------#','\n')

    dicc ={"Nombre": "Ana", "Edad": 25, "Ciudad": "Resistencia"}
    print("Creamos un Diccionario. Ahora te lo muestro ...........")

    for clave,valor in dicc.items():     # imprime las claves y los valores
        print(f'Clave: {clave} - Valor: {valor}')
    print("")
    print("Ahora te muestro cada valor por su clave")
    for valor in dicc.values():     # Solo imprime los valores
        print(valor)
    print("")
    print("Ahora vamos a cambiar la edad.",'\n')

    while True:  
        try:
            dicc['Edad']=int(input("Por favor ingresa la edad, debe ser un numero entero : "))
            break
        except ValueError:
            print("¡Entrada incorrecta! Por favor, ingresa un número entero.")
    print("")
    print("Ahora vamos a ingresar otra clave, la profesion.",'\n')
    dicc['Profesion']=str(input("Por favor ingresa una profesion : "))
    print("")
    print("Habiendo modificado la edad e ingresado la profesión, el diccionario quedo de la siguiente manera: ")

    for clave,valor in dicc.items():     
        print(f'{clave}: {valor}')
    print("")

def Ejercicio9():
    print('#---------------------------- Ejercicio N° 9 -----------------------------#')
    print('#---------------------- Metodos de  Diccionarios - Dict ------------------#','\n')

    claves= ['Nombre', 'Tipo', 'Sexo']
    mascotas = dict.fromkeys(claves)
    print("Vamos a crear un diccionario de tu mascota con el nombre, el tipo de animal y su sexo.")
    print(mascotas)
    print("Te muestro, solo tiene las claves. Ahora te voy solicitar que ingreses los valores.")
    mascotas['Nombre']=input("Ingresa el nombre de tu mascota: ")
    mascotas['Tipo']=input("Ingresa el el tipo de animal de tu mascota: ")
    
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

def Ejercicio10():
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

def Menu():
    print('#-------------------- TODOS LOS EJERCICIOS JUNTOS --------------------#')
    print('#                                                                     #')
    print('#------------------------------- MENU --------------------------------#')
    print('#                                                                     #')
    print('#------------------------------- LISTAS ------------------------------#')
    print('#                                                                     #')
    print('#                    1. Crear y acceder                               #')
    print('#                    2. Agregar y eliminar                            #')
    print('#                    3. Métodos útiles                                #')
    print('#                                                                     #')
    print('#------------------------------- TUPLAS ------------------------------#')
    print('#                                                                     #')
    print('#                    4. Desempaquetado                                #')
    print('#                    5. Conversión tupla ↔ lista                      #')
    print('#                                                                     #')
    print('#------------------------------- CONJUNTOS ---------------------------#')
    print('#                                                                     #')
    print('#                    6. Crear conjuntos                               #')
    print('#                    7. Conversión lista ↔ conjunto                   #')
    print('#                                                                     #')
    print('#------------------------------- DICCIONARIOS-------------------------#')
    print('#                                                                     #')
    print('#                    8. Crear y acceder                               #')
    print('#                    9. Métodos de diccionarios                       #')
    print('#                                                                     #')
    print('#------------------------------- INTEGRADOR --------------------------#')
    print('#                                                                     #')
    print('#                    10. Combinar estructuras                         #')
    print('#                                                                     #')
    print('#                     0. TERMINAR                                     #')
    print('#                                                                     #')
    print('')
    return(int(input('            Seleccione Opcion: ')))

def TomarOpcion():
    d = str(input('¿Desea Seguir Ejecutando? : S/N:'))
    if d == 'S' or d =='s' :
        op=Menu()
    else:
        op=0
    return op
# VER EL MENU QUE NO ESTA FUNCIONANDO

if (op > 0):
    op=Menu()
    while True:
        try:
            print('')
            #op = int(input('            Seleccione Opcion: '))
            if op in range(0,10):
                match op:
                    case 1:
                        Ejercicio1()
                    # d = str(input('¿Desea Seguir Ejecutando? : S/N:'))
                    # if d == 'S' or d =='s' :
                    #     op=Menu()
                    # else:
                    #     break
                        TomarOpcion()
                    case 2:
                        Ejercicio2()
                        d = str(input('¿Desea Seguir Ejecutando? : S/N:'))
                        if d == 'S' or d =='s' :
                            op=Menu()
                        else:
                            break
                    case 3:
                        Ejercicio3()
                        d = str(input('¿Desea Seguir Ejecutando? : S/N:'))
                        if d == 'S' or d =='s' :
                            op=Menu()
                        else:
                            break
                    case 4:
                        Ejercicio4()
                    case 5:
                        Ejercicio5()
                    case 6:
                        Ejercicio6()
                    case 7:
                        Ejercicio7()
                    case 8:
                        Ejercicio8()
                    case 9:
                        Ejercicio9()
                    case 10:
                        Ejercicio10()
                    case 0:
                        print("Fin del Programa. Muchas gracias")  
                        break
            else:
                print("¡Entrada incorrecta! ingresa un numero entero (del 1 al 10 - 0 Para Terminar).")        
        except ValueError:
            print("¡Entrada incorrecta! Por favor, ingresa un número entero.")
else:
    print("Fin del Programa. Muchas gracias")  






