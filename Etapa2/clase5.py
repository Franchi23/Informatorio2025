## LISTAS ##

# lista =['hola', 123, True]

# print(lista[0],'\n')
# print(lista[1],'\n')
# print(lista[2],'\n')

# lista2 =['Franchi','Pao','Paula','Santi']

# lista3 =[1,True,lista,'cadena',1.5,lista2]

# print('\t',lista,'\n')
# print(lista2,'\n')
# print(lista3,'\n')

# lista4=['Azul','Blanco','Rosa','Verde','Negro','Lila','Morado']

# print('\t', lista4)

# print('\t',lista4[0:3])

# print(lista4[-3])

# lista4 [-1] = 'Negro'
# print(lista4)


# lista4.append('Rojo')
# print(lista4)

# lista4.remove('Lila')
# print(lista4)

# tupla =('Informatorio','Chaco',2025)
# print(tupla)

# conjunto ={'Info','Chaco','Info',2025,123,456,456}
# print(conjunto)

# if ('Info' in conjunto):
#     print("Info Si Existe en conjunto",'\n')
# else:
#     print("Infos No Existe en conjunto",'\n')

# for i in conjunto:
#     print(i)

# frutas ={'Naranja','Manzana','Banana','Frutilla','Tomates'}
# verdutas = {'Lechuga','Tomates','Zanahorias','Tomates'}

# union = frutas | verdutas

# print('\n', union)

# union = frutas & verdutas

# print('\n', union)

# variable ='Informatorio'
# print(f'Bienvenidos al {variable} 2025')

# diccionario = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(diccionario["brand"])

# EJERCIIO FINAL DE CLASE #

#Sistema de alumnos#

alumnos = [
    {'Nombre' : 'Francisco', 'Apellido':'Muñoz', 'Materias':('Matermaricas','Historia')},
    {'Nombre' : 'Paola', 'Apellido':'Meza', 'Materias':('Matermaricas','Biologia')},
    {'Nombre' : 'Santiago', 'Apellido':'Muñoz', 'Materias':('Lengua','Geografia')},
    {'Nombre' : 'Paula', 'Apellido':'Muñoz', 'Materias':('Matermaricas','Ingles')}]

#Mostrar la lista de los alumnos
print('Lista completa de los alumnos :','\n')
for alumno in alumnos:
    print(alumno)
print('-' * 90)

nombre = input("Ingrese el nombre del alumno: ")
encontrado = False
for alumno in alumnos:
    if alumno['Nombre'].lower()== nombre.lower():
        print('Alumno Encontrado! ', alumno)
        encontrado=True
if not encontrado:
    print("Ese alumno no se encuentra en la Base de Datos")

print('-' * 90)

# Mostrar todas las materias distintas ( usando set )

materias = set()

for alumno in alumnos:
    materias.update(alumno["Materias"])

print("Materias distintas que se cursan: ", materias)

print('-' * 90)

# Contar cuantos alumnos cursan cada materia ( usando dict)

conteo = {}
for alumno in alumnos:
    for materia in alumno['Materias']:
        conteo[materia] = conteo.get(materia,0) + 1

print("Cantidad de Alumnos por Materia: ")
for materia, cantidad in conteo.items():
    print(f"{materia}: {cantidad }")

print('-' * 90)