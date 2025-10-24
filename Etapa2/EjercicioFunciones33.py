def pedido(titulo,*args):

    print('')
    print(titulo)
    c=1
    for sabores in args:
        print('\n'.join(sabores))
           
print('#---------------------------- Ejercicio N° 3 -------------------------------#')
print('#------------------------- EMPANADAS ARGENTINAS ----------------------------#','\n')

lista=[]
print('Ingresa los sabores de las empandas para el pedido N° 99: X-Para terminar la carga')
c=1
while True:
    aux=str(input('Ingresa el Sabor: '))
    if aux.upper() =='X':
        break
    else:
        lista.append(aux)
        c+=1

pedido('Pedido N° 99 ',lista)
print('')
print("Gracias por utilizar la aplicacion.")
print('')