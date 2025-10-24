import tkinter as tk
from tkinter import messagebox

def suma(num1, *args):
    total = num1
    for num in args:
        total += num
    return total

def resta(num1,*args):
    total= num1
    for num in args:
        total -=num
    return total

def mostrar():
    messagebox.showinfo("El Resultado es: ", suma(5,3))

ventana = tk.Tk()
ventana.configure(background="lightgrey")
ventana.resizable(0,0)
ventana.title("Calculadora Franchi")
ventana.geometry("300x400")

boton=tk.Button(ventana,text="Apreta el Boton",font=('arial',20),command=mostrar,bg='#00e8e8',fg='white')

#etiqueta.pack()
boton.pack(fill=tk.BOTH)

ventana.mainloop()