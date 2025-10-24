# Crea una función ficha(**datos) que reciba datos con nombre (por ejemplo: nombre="Ana", edad=25,
# ciudad="Chaco")
# y los imprima en formato:
# Nombre: Ana | Edad: 25 | Ciudad: Chaco

def ficha(**kwargs):
    # for clave,valor in kwargs.items():
    #     print(clave,":",valor)
        print(kwargs)
        

print('#---------------------------- Ejercicio N° 4 -------------------------------#')
print('#---------------------------- FICHA PERSONAL -------------------------------#','\n')

# lista=[]

# lista.append(str(input("Ingrese el nombre: ")))
# lista.append(int(input("Ingrese la edad: ")))
# lista.append(str(input("Ingrese la ciudad: ")))

#ficha(nombre=lista[0], edad=lista[1], ciudad=lista[2])
ficha(nombre="Ana", edad=25, ciudad="Chaco")