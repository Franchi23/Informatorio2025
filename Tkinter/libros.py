from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox

class Libros(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()
    
    def widgets(self):

        frame1= tk.Frame(self,bg="#dddddd",highlightbackground="gray",highlightthickness=2)
        frame1.pack()
        frame1.place(x=0,y=0,width=1100, height=100)

        title =tk.Label(self,text="LIBROS",bg="#dddddd",font="sans 30 bold", anchor="center")
        title.pack()
        title.place(x=5,y=0,width=1090,height=90)

        frame2= tk.Frame(self, bg="#C6D9E3",highlightbackground="gray",highlightthickness=2)
        frame2.place(x=0,y=100, width=1100, height=550)

        lblframe = LabelFrame(frame2,text="Informacion de Libros", bg="#C6D9E3",font="sans 16 bold")
        lblframe.place(x=10,y=10,width=600,height=520)

        label_nro_libro = tk.Label(lblframe,text="Nro de Libro: ",bg="#C6D9E3",font="sans 12 bold")
        label_nro_libro.place(x=10,y=5)
        self.nro_libro = tk.StringVar()         # para almacenar el nro de libro
        self.entry_nro_libro = tk.Entry(lblframe,textvariable=self.nro_libro,state="readonly",font="sans 12 bold")
        self.entry_nro_libro.place(x=130,y=5,width=100)

        #TITULO
        label_titulo =tk.Label(lblframe,text="Titulo : ",bg="#C6D9E3",font="sans 12 bold")
        label_titulo.place(x=10,y=35)
        self.entry_titulo = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_titulo.place(x=130,y=35,width=280)
        #AUTOR
        label_autor =tk.Label(lblframe,text="Autor: ",bg="#C6D9E3",font="sans 12 bold")
        label_autor.place(x=10,y=65)
        self.autor = tk.Entry(lblframe,font="sans 12 bold")
        self.autor.place(x=130,y=65,width=280)
        #ISBN
        label_isbn =tk.Label(lblframe,text="ISBN: ",bg="#C6D9E3",font="sans 12 bold")
        label_isbn.place(x=10,y=95)
        self.label_isbn = tk.Entry(lblframe,font="sans 12 bold")
        self.label_isbn.place(x=130,y=95,width=120)
        #GENERO
        label_genero =tk.Label(lblframe,text="Genero: ",bg="#C6D9E3",font="sans 12 bold")
        label_genero.place(x=10,y=125)
        self.label_genero = ttk.Combobox(lblframe,font="sans 12 bold",values=["M", "F"])
        self.label_genero.place(x=130,y=125,width=70)
        #EDITORIAL
        label_editorial =tk.Label(lblframe,text="Editorial: ",bg="#C6D9E3",font="sans 12 bold")
        label_editorial.place(x=10,y=155)
        self.entry_editorial = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_editorial.place(x=130,y=155,width=280)
        #EDIDICION
        label_edicion =tk.Label(lblframe,text="Edicion:  ",bg="#C6D9E3",font="sans 12 bold")
        label_edicion.place(x=10,y=185)
        self.entry_edicion = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_edicion.place(x=130,y=185,width=100)
        #AÑO PUBLICACION
        label_anio_pub =tk.Label(lblframe,text="Año Pub:  ",bg="#C6D9E3",font="sans 12 bold")
        label_anio_pub.place(x=10,y=215)
        self.entry_anio_pub = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_anio_pub.place(x=130,y=215,width=100)
        #UNIDADES
        label_unidades =tk.Label(lblframe,text="Unidades:  ",bg="#C6D9E3",font="sans 12 bold")
        label_unidades.place(x=10,y=245)
        self.entry_unidades = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_unidades.place(x=130,y=245,width=100)