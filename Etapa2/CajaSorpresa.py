class CajaSorpresa():
    def __init__(self,nombre):
        self.nombre = []

    def AgregarSorpresa(self,nombre):
        self.nombre.append(nombre)
    
    def AbrirSorpresa(self,n=0):
        if (self.nombre[n] == None) or (self.nombre[n] == ''):
           print(f'La caja esta vacia!')
        else:
            print(f'Sorpresa:  {n}')
            print(f' {self.nombre[n]} ')
            
