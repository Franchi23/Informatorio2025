## Modulos ##

## Importacion de modulos estandar
# import random
# import datetime

# import builtins

# print(dir(builtins))

## MODULOS PERSONALIZADOS ##


# import modulo_pers
from modulo_pers import agregar_libro,crear_libro,buscar_libro,mostrar_catalogo
biblioteca =[]

libro1 = crear_libro('Harry Potter','J.K. Rowl',1995)
libro2= crear_libro('Libro 2', 'Franchi',2001)

agregar_libro(bilioteca=biblioteca, libro=libro1)
agregar_libro(biblioteca,libro2)

mostrar_catalogo(biblioteca)

libro_buscado = buscar_libro(biblioteca,'Libro 2')

print(libro_buscado)