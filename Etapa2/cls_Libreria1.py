 ##         CLASE BLIBLIOTECA       ##

class Libro():
    def __init__(self,idlibro,titulo,autor,isbn,num_pag,genero,editorial,edicion,anio_pub,cantidad,estado):
        self.idlibro = idlibro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.numpag = num_pag
        self.genero = genero
        self.editorial = editorial
        self.edicion = edicion
        self.anio_pub = anio_pub
        self.cantidad = cantidad
        self.__estado = estado
    
    def mostrar_libro(self):
        return f'Titulo: {self.titulo}; Autor: {self.autor}; ISBN: {self.isbn}; Unidades: {self.cantidad}; Disponibles: '
    
    def Agregar_Libro(self):
        pass

    def buscar_porTitulo(self):
        pass

    #Metodos de Clase
    @classmethod
    def prestar_devolver_libro(cls, estado):
        cls.__estado =estado        #1-Prestado / 0-En biblioteca


class Autor():
    def __init__(self,nombre,nacionalidad,fec_nac,publicaciones):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fec_nac = fec_nac
        self.publicaciones = publicaciones
    
    def publicar_libro(self):
        pass

    def cantidad_publicaciones(self):
        pass


class Socio():
    def __init__(self,idsocio,nombre,fec_nac,domicilio,sexo,mail,telefono):
        self.idsocio = idsocio
        self.nombre = nombre
        self.fe_nac = fec_nac
        self.domicilio = domicilio
        self.sexo = sexo
        self.mail =mail
        self.telefono =telefono
        self.en_prestamo = []

    def solicitar_prestamo(self,libro):
        if libro.estado == 1:
            self.en_prestamo.append(libro)
            print(f'El libro {libro.idlibro} - {libro.titulo} se dio en prestamo a: {self.nombre}')
        else:
            print(f'El libro {libro.idlibro} - {libro.titulo} no esta disponible o no quedan mas unidades')
    
    def devolver_libro(self, libro):
        if libro.estado == 0 and libro in self.en_prestamo:
            self.en_prestamo.remove(libro)
            libro.prestar_devolver_libro(1)
            print(f'El libro {libro.idlibro} - {libro.titulo} fue devuelto por: {self.nombre}')


class Biblioteca():
    def __init__(self):
        self.libros =[]
        self.socio=[]
        self.autores =[]

    def agregar_socio(self,socio):
        if socio in self.socio:
            return f'El Socio: {socio.nombre} ya fue registrado como cliente de la Biblioteca anteriormente'
        else:
            self.socio.append(socio)
            return f'El Socio: {socio.nombre} fue registrado como cliente de la Biblioteca'
    
    def quitar_socio(self,socio):
        if socio in self.socio:
            self.socio.remove(socio)
            return f'El Socio: {socio.nombre} fue dado de baja de la Biblioteca'
        else:
            return f'El Socio: {socio.nombre} no esta registrado como cliente de la Biblioteca'
        
    def mostrar_socio(self):
        for socio in self.lector:
            print(f'Socio: {socio.nombre}')
    
    def mostrar_libros(self):
        for libro in self.libro:
            print(libro.mostrar_libro())