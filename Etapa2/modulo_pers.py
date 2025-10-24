def crear_libro(titulo, autor, año):
    """ Retorna un libro en forma de diccionario dict() """
    return {'Titulo': titulo, 'Autor': autor, 'Año': año}

def agregar_libro(bilioteca, libro):
    """ Agrega el libro pasado como arguemtno a la lista de libros de la biblioteca """
    bilioteca.append(libro)

def buscar_libro(bilioteca, titulo):
    """ busca un libro dentro de una lista biblioteca """
    for libro in bilioteca:
        if (libro['Titulo']== titulo):
            return libro
    return None

def mostrar_catalogo(biblioteca):
    for libro in biblioteca:
        print(f'Titulo: {libro['Titulo']}\nAutor:{libro['Autor']}\nAño: {libro['Año']} -------------')

def otra_funcion():
    pass