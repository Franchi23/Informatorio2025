def descuento(pre,porc):
    p=0
    if porc == 0:
        p=10
    else:
        p=porc
    return (pre -(pre * p /100))

print('#---------------------------- Ejercicio N° 2 -------------------------------#')
print('#---------------------------- DESCUENTO MAGICO -----------------------------#','\n')

print('Define una función que calcula el precio final después de aplicar el descuento')
print('Si no se especifica el porcentaje, se aplica el 10% por defecto.','\n')

p1=float(input('Ingrese el Precio del articulo $ ') or 0)
p2=float(input('Ingrese el porcentaje de descuento a aplicar % ') or 0)

if (p1 > 0):
    resu=descuento(p1,p2)

    print('')
    if (p2 == 0):
        print(f'Se aplicó el 10% de descuento. El precio final del articulo con el descuento aplicado es $ {resu}','\n')
        print('')
    else:
        print(f'El precio final del articulo con el descuento aplicado es $ {resu}','\n')
        print("Gracias por utilizar la aplicacion.")
        print('')
else:
    print('')
    print('No se puede efectuar el calculo si el precio no fue ingresado o es 0. Por favor verifique','\n')
    print("Gracias por utilizar la aplicacion.")
    print('')

