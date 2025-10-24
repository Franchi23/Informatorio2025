class Coche:
    ruedas =4

    def __init__(self,marca,modelo,color):
        self.marca=marca
        self.modelo=modelo
        self.color=color

# Metodos de instancia
    def acelerar(self):
        print(f"El {self.marca} {self.modelo} esta acelerando!!!!")
    
    def frenar(self):
        print(f"El {self.marca} {self.modelo} esta frenando!!!!")

#Metodos de Clase
    @classmethod
    def incrementar_ruedas(cls):
        cls.ruedas +=1

#Metodo Estatico
    @staticmethod
    def calcular_distancia(velocidad, tiempo):
        return velocidad*tiempo
