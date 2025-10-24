import tkinter as tk
from tkinter import messagebox

def saludar():
    print("Hola Franchi")
    messagebox.showinfo("Mensaje de información", "¡Hola Franchi! Este es un mensaje en un cuadro de texto.")

# Creamos la ventan ppal con tk
ventana = tk.Tk()
ventana.configure(background='black')
ventana.title('Mi primera ventana con Tkinter')
ventana.geometry("500x500")                     #ancho por alto en pixeles

#etiqueta = tk.Label(ventana,text="Hola Mundo", font=('arial',20))
boton=tk.Button(ventana,text="Apreta el Boton",font=('arial',20),command=saludar,bg='#00e8e8',fg='white')

#etiqueta.pack()
boton.pack(fill=tk.BOTH)

ventana.mainloop()