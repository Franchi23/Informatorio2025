from cls_Libreria import Biblioteca,Socio,Libro

socio = Socio("29440821","Francisco Santiago Muñoz","23/05/1982","Av. Moreno 339","M","franchi@xxx.com","3624666789")
biblio = Biblioteca()
libro = Libro('1','El Monje','J.J Abraham','258963222','256','Terror','XX-Star','1°','2004','2','0')

print(biblio.agregar_socio(socio))


print(biblio.Agregar_Libro(libro))



biblio.mostrar_libros()
biblio.mostrar_socio()
