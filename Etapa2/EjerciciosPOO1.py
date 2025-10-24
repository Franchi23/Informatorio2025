import random
from CajaSorpresa import CajaSorpresa

sorpresa = CajaSorpresa('')

c=0
print('** Vamos a agregar las sorpresas **')
while True:
    print('')
    sorp= input("Ingresa la sorpresa: - Presiona X para terinar: ")
   
    if (sorp == 'x') or (sorp == 'X'):
        break
    else:
        sorpresa.AgregarSorpresa(sorp)
        c+=1

n = random.randint(0,c-1)
sorpresa.AbrirSorpresa(n)

print('')
print("Gracias por utilizar la aplicacion.")
print('')

