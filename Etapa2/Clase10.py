 ## POO ##

# # class vacio:
# #    pass

# # obj = vacia()
# # obj_2 = vacia()
# # obj_3 = vacia()
# # obj_saludo ="Hola"

# from coche import Coche

# # #Crear una instancia de la clase coche
# un_coche =Coche("Totyota", "Corola", "Rojo")
# otro_coche =Coche("Chevrolet", "Onix", "Blanco")

#  #Acceder al estado de los atributos

# print("Atributos del coche 1: ")
# print(f'Marca: {un_coche.marca}\n Modelo: {un_coche.modelo}\n Color: {un_coche.color}\n Ruedas: {un_coche.ruedas}\n ----------------')

# print("Atributos del coche 2: ")
# print(f'Marca: {otro_coche.marca}\n Modelo: {otro_coche.modelo}\n Color: {otro_coche.color}\n Ruedas: {otro_coche.ruedas}\n ----------------')

# # Uso de los Metodos
# un_coche.acelerar()
# un_coche.frenar()

# otro_coche.acelerar()
# otro_coche.frenar()


# print(un_coche.ruedas)

# otro_coche.incrementar_ruedas()
# print(un_coche.ruedas)

# print(f'El la distancia que recorre el {un_coche.marca} {un_coche.modelo} a 80 Km en 2 hs es: {un_coche.calcular_distancia(80,2)} Km')


# class Perro():
#     def __init__(self, nombre, raza, poder):
#         self.nombre = nombre
#         self.raza = raza
#         self.poder = poder

# catdoog = Perro("CatDog","Pastor","Super Velocidad")

# print(catdoog.nombre)
# print(catdoog.raza)
# print(catdoog.poder)

import random

class Dado():
    def __init__(self, caras =6):
        self.caras = caras

    def LanzarDado(self):
        return random.randint(1, self.caras)
    
Dado_1 =Dado()
Dado_2 =Dado(15)

print(f'Dado 1: {Dado_1.LanzarDado()}')

print(f'Dado 2: {Dado_2.LanzarDado()}')