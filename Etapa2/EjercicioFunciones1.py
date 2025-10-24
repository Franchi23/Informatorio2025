def misterio(palabra):
    invertida=""
    if (len(palabra) > 5):
        for caracter in palabra:
            invertida = caracter + invertida
        return invertida
    else:
        return palabra.upper()
    
print('#---------------------------- Ejercicio N° 1 -------------------------------#')
print('#--------------------------- FRASES MISTERIOSAS ----------------------------#','\n')

print('Vamos a solicitarle que ingrese una palabra')
print('El resultado de la funcion sera la palabra escrita al revés, pero solo si tiene más de 5 letras')
print('Si no, va a devolver la palabra en mayúsculas','\n')

pal=str(input('Por favor ingresa una palabra. ENTER para finalizar: '))
print('')
resultado = misterio(pal)
print(f'El resultado de la funacion es: {resultado}','\n')
print("Gracias por utilizar la aplicacion.")
print('')



