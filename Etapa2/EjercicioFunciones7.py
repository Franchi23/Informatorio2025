import random,os
cont=0
def tirar_dado():
     return random.randint(1, 6)

def jugar():
    t1= tirar_dado()
    t2= tirar_dado()

    if (t1 == t2):
         print(f'Ganaste. Abos dados son iguales Dado 1: {t1} - Dado 2: {t2}. Lo lograste en {cont} intentos')
         return True
    else:
         print(f'Segui participando. Los dados son distintos Dado 1: {t1} - Dado 2: {t2}')

while True:

    print('#---------------------------- Ejercicio N° 7 -------------------------------#')
    print('#------------------------------ Juego del Dado -----------------------------#','\n')

    print("Vamos a tirar 2 dados si son iguales Ganaste",'\n')
    cont+=1
    if jugar() == True:
        break
    else:
        try:
            op = int(input("Desea volver a tirar los dados  1-Si / 0-No : "))     
            if (op == 0):
                break
            else:
                os.system('cls')    #Limpia la Pantalla
        except ValueError:
            print("¡Entrada incorrecta! Por favor, ingresa un número entero.")

print('')
print("Gracias por utilizar la aplicacion.")
print('')