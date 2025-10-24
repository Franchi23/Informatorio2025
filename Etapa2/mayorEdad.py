anio_actual = 2025
c=0
while c < 1:
    try:
       anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
       c=1       
    except ValueError:
        print("El ano ingresado no es correcto. El año debe ser un numero entero")
        c=0
     
if c >=1:
    edad = anio_actual - anio_nacimiento  
    if edad >= 18:
        print("Tenes " + str(edad) + " años. Sos Mayor de edad")
    else:
        print("Tenes " + str(edad) + " años. Sos menor de edad")