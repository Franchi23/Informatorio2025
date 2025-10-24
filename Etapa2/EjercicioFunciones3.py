def pedido(sabores):
    lista_aux=[]
    for i in range(0,len(sabores)):
        lista_aux.append((i+1,sabores[i]))
    
    return lista_aux

print('#---------------------------- Ejercicio N° 2 -------------------------------#')
print('#------------------------- EMPANADAS ARGENTINAS ----------------------------#','\n')

lista=[]
aux=''
print('Ingresa los sabores de las empandas: X-Para terminar la carga')
while True:
    aux=str(input('Ingresa el Sabor: '))
    if aux.upper() =='X':
        break
    else:
        lista.append(aux)

print('')
diccionario = dict(pedido(lista))
for clave,valor in diccionario.items():     
    print(f'{clave} . {valor}')

print('')
print("Gracias por utilizar la aplicacion.")
print('')