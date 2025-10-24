# Suma flexible
# Crea una función sumar_todo(*numeros) que acepte cualquier cantidad de números y devuelva la suma total.
# Ejemplo: sumar_todo(2, 4, 6) → 12

def sumar_todo(*args):
    resultado=0

    for num in args:
        resultado += num
    return resultado

print('#---------------------------- Ejercicio N° 9 -------------------------------#')
print('#----------------------------- SUMA FLEXIBLE -------------------------------#','\n')

cant=int(input('Ingrese cuantos numeros desea sumar: '))
print('Genial. Ahora le solicitare que ingrese los numeros que desea que se sumen, uno a uno')

lista=[]
n=0
for i in range(0,cant):
    n= int(input('Ingrese el numero a sumar :'))
    lista.append(n)

#print(f'La suma de los numeros ingresados da como resultado: {sumar_todo(lista)}')
print(f'La suma de los numeros ingresados da como resultado: {sumar_todo(2,4,6,8)}')
#sumar_todo(2,4,6,8)