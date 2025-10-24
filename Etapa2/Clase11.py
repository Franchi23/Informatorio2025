## HERENCIA ##

# class Vehiculo:
#     def __init__(self,ruedas, marca, modelo,color):
#         self.ruedas = ruedas
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color

#     def acelerar(self):
#         print(f"El {self.marca} {self.modelo} esta acelerando!!!!")
    
#     def frenar(self):
#         print(f"El {self.marca} {self.modelo} esta frenando!!!!")
    
# class Coche(Vehiculo):
#     def __init__(self, ruedas, marca, modelo, color, dueno):
#         super().__init__(ruedas, marca, modelo, color)
#         self.dueno = dueno


#     def bocina(self):
#         print('PIIIIIIIIIIIIIIII ')
    
#     def acelerar(self):
#         print(f"Ahora estoy acelerando desde Coche")

# class Bicicleta(Vehiculo):
#     def acelerar(self):
#         print(f"Ahora estoy empezando a pedalear desde Bicileta")

# un_coche = Coche(ruedas=4, marca='Toyota', modelo='Corola',color='Rojo',dueno='Franchi')
# una_bici = Bicicleta(ruedas=2,marca='SMP',modelo='Mountain Bike',color='Negro')


# print(f'Este auto {un_coche.marca} {un_coche.modelo} esta activo. Tiene {un_coche.ruedas} ruedas. Su dueño es {un_coche.dueno}')
# un_coche.bocina()
# un_coche.acelerar()
# print(f'Esta bici {una_bici.marca} {una_bici.modelo} esta activa, Tiene {una_bici.ruedas} ruedas')
# una_bici.acelerar()

# class A():
#     def __init__(self):
#         print("Soy la Clase A")

# class B():
#     def __init__(self):
#         print("Soy la Clase B")

# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         # A.__init__(self)
#         # B.__init__(self)
#         print("Soy la Clase C")

# Test = C()
# print(f'MRO : {C.__mro__}')

## POLIMORFISMO ##

# class Empleado():
#      def __init__(self,nombre,sueldo):
#          self.nombre = nombre
#          self.sueldo = sueldo

#      def CalcularSueldoAnual(self):
#          suedoAnual = 12 * self.sueldo * (1 + 1/100)
#          print(f'El Sueldo anual de {self.nombre}, que es empleado General es de: $ {suedoAnual}')

# class Programador(Empleado):
#      def CalcularSueldoAnual(self):
#          suedoAnual = 12 * self.sueldo + (1 + 5/100)
#          print(f'El Sueldo anual de {self.nombre}, que es PROGRAMADOR es de: $ {suedoAnual}')

# class Diseñador(Empleado):
#      def CalcularSueldoAnual(self):
#          suedoAnual = 12 * self.sueldo + (1 + 3/100)
#          print(f'El Sueldo anual de {self.nombre}, que es DISEÑAROR  es de: $ {suedoAnual}')

# empleados = [
#      Empleado('Jose',500),
#      Programador('Franchi', 1000),
#      Diseñador('Luis',1500),
#      Empleado('Sandra',2000)
# ]

# def CalculoSueldos():
#      for empleado in empleados:
#          empleado.CalcularSueldoAnual()
    
# CalculoSueldos()


## ENCAPSULAMIENTO ##
class Circulo():
    def __init__(self, radio):
        self.radio = radio
        self.__pi = 3.1415
    
    def calcular_perimetro(self):
        return 2 * self.__pi * self.radio

    def calcular_area(self):
        return self.__pi * self.radio ** 2
    
    def GetPI(self):
        return f'El valor de PI es: {self.__pi}'
    
    def SetPI(self, nuevo_valor):
        if (type(nuevo_valor) == int or type(nuevo_valor) == float):
            if (nuevo_valor > 0):
                self.__pi = nuevo_valor
                print(f"El nuevo valor de PI es: {self.__pi}")
            else:
                print("PI NO puede ser un valor negativo")
        else:
            print("PI deber ser un numero positivo")


circulo_1 = Circulo(3.5)

print(circulo_1.calcular_perimetro())
print(circulo_1.calcular_area())
print(circulo_1.GetPI())

circulo_1.SetPI(4.8)
circulo_1.SetPI(-5)
circulo_1.SetPI('Hola')


