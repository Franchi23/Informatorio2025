from tkinter import *
import os
import tkinter as tk
from PIL import Image, ImageTk
from socios import Socios
from libros import Libros
from autores import Autores
from buscarLibros import BuscarLibros

class Contenedor(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=800, height=500)
        self.config(bg="#C6D9E3")
        self.widgets()

    def mostrar_frames(self, contenedor):
        top_level= tk.Toplevel(self)
        frame = contenedor(top_level)
        frame.config(bg="#C6D9E3")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(False,False)

        #Para que los mensajes queden por delante del frame y no se vayan atras
        top_level.transient(self.master)
        top_level.grab_set()
        top_level.focus_set()
        top_level.lift()

    def socios(self):
        self.mostrar_frames(Socios)
    
    def libros(self):
        self.mostrar_frames(Libros)

    def autores(self):
        self.mostrar_frames(Autores)
    
    def prestamos(self):
        #self.mostrar_frames(Autores)
        pass

    def devvoluciones(self):
        #self.mostrar_frames(Autores)
        pass

    def buscarLibros(self):
        self.mostrar_frames(BuscarLibros)

    def widgets(self):

        frame1 = tk.Frame(self,bg="#C6D9E3")
        frame1.pack()
        frame1.place(x=0,y=0,width=800, height=600)

        btnSocios = Button(frame1, bg="#F4B400",foreground="white", font="sans 18 bold" ,text="Ir a Socios",command=self.socios)
        btnSocios.place(x=20,y=30,width=240,height=60)

        btnLibros = Button(frame1, bg="#c62e26",foreground="white", font="sans 18 bold",text="Ir a Libros",command=self.libros)
        btnLibros.place(x=20,y=110,width=240,height=60)

        btnAutores = Button(frame1, bg="#12B820",foreground="white", font="sans 18 bold",text="Ir a Autores",command=self.autores)
        btnAutores.place(x=20,y=190,width=240,height=60)

        btnPrestamos = Button(frame1, bg="#A2DA09",foreground="white", font="sans 18 bold",text="Prestamos",command=self.prestamos)
        btnPrestamos.place(x=20,y=270,width=240,height=60)

        btnDevoluciones = Button(frame1, bg="#B10B6C",foreground="white", font="sans 18 bold",text="Devoluciones",command=self.devvoluciones)
        btnDevoluciones.place(x=20,y=350,width=240,height=60)

        dir= os.path.dirname(os.path.abspath(__file__))
        ruta_imagen = os.path.join(dir,'imagenes','fondo.png')
        self.logo_image = Image.open(ruta_imagen)
        self.logo_image = self.logo_image.resize((380,270))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#C6D9E3") 
        self.logo_label.place(x=380,y=30)

        copyright_label = tk.Label(frame1, text="© 2025 Franchi. Todos los derechos reservados", font="sans 10 bold",bg="#C6D9E3",fg="gray",relief="ridge")
        copyright_label.place(x=350,y=420)

        