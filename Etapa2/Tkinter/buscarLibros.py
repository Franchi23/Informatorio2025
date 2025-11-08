from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from tkcalendar import Calendar,DateEntry

class BuscarLibros(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()
    
    def widgets(self):

        frame1= tk.Frame(self,bg="#dddddd",highlightbackground="gray",highlightthickness=2)
        frame1.pack()
        frame1.place(x=0,y=0,width=1100, height=100)

        title =tk.Label(self,text="AUTORES",bg="#dddddd",font="sans 30 bold", anchor="center")
        title.pack()
        title.place(x=5,y=0,width=1080,height=90)

        frame2= tk.Frame(self, bg="#C6D9E3",highlightbackground="gray",highlightthickness=2)
        frame2.place(x=0,y=100, width=1100, height=550)

        lblframe = LabelFrame(frame2,text="Informacion de los Autores", bg="#C6D9E3",font="sans 16 bold")
        lblframe.place(x=10,y=10,width=500,height=520)

        label_nro_Socio = tk.Label(lblframe,text="Nro de Autor: ",bg="#C6D9E3",font="sans 12 bold")
        label_nro_Socio.place(x=10,y=5)
        self.nro_Socio = tk.StringVar()         # para almacenar el nro de autor
        self.entry_nro_Socio = tk.Entry(lblframe,textvariable=self.nro_Socio,state="readonly",font="sans 12 bold")
        self.entry_nro_Socio.place(x=130,y=5,width=100)

        #NOMBRE
        label_nombre =tk.Label(lblframe,text="Nombre : ",bg="#C6D9E3",font="sans 12 bold")
        label_nombre.place(x=10,y=35)
        self.entry_nombre = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_nombre.place(x=130,y=35,width=280)
        #NACIONALIDAD
        label_nacionalidad =tk.Label(lblframe,text="Nacionalidad: ",bg="#C6D9E3",font="sans 12 bold")
        label_nacionalidad.place(x=10,y=65)
        self.entry_nacionalidad = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_nacionalidad.place(x=130,y=65,width=280)
        #FECHA NACIMIENTO
        label_fecha_nac =tk.Label(lblframe,text="Fe Nacimiento: ",bg="#C6D9E3",font="sans 12 bold")
        label_fecha_nac.place(x=10,y=95)
        self.label_fecha_nac = DateEntry(lblframe,font="sans 12 bold",date_pattern='MM/dd/yyyy')
        self.label_fecha_nac.place(x=130,y=95,width=120)
        #PUBLICACIONES
        label_publicaciones =tk.Label(lblframe,text="Publicaciones: ",bg="#C6D9E3",font="sans 12 bold")
        label_publicaciones.place(x=10,y=125)
        self.entry_publicaciones = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_publicaciones.place(x=130,y=125,width=100)