from tkinter import Tk, Frame,messagebox,simpledialog
from contenedor import Contenedor
import tkinter as tk


class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Biblioteca FRANCHI V 1.0")
        self.resizable(False,False)
        self.configure(bg="#C6D9E3")
        self.geometry("800x450+120+20")

        # #BARRA DE MENU ---------------------------------------------------
        # exitImagen = tk.PhotoImage(file='d:/DATOS/Desktop/Informatorio/Etapa 2/Ejemplo Sistema Ventas/imagenes/Salir1.png')
        # barra_menu = tk.Menu(self)
        # self.config(menu=barra_menu)
        # menu_archivo =tk.Menu(barra_menu,tearoff=0,font="Tahoma")
        # barra_menu.add_cascade(label='Archivo', menu=menu_archivo)
        # menu_archivo.add_command(label='Libros')
        # menu_archivo.add_command(label='Socios')
        # menu_archivo.add_command(label='Autores')
        # menu_archivo.add_separator()
        # #menu_archivo.add_command(label='Salir', command=self.destroy)
        # menu_archivo.add_command(label='Salir', image=exitImagen,compound='left', command=Salir)
        # #-------------------------------------------------------------------
        self.contenedor = Frame(self,bg="#C6D9E3")
        self.contenedor.pack(fill="both",expand=True)

        self.frames={
            Contenedor: None
        }
        
        self.cargar_frames()
        self.mostrar_frame(Contenedor)

    def cargar_frames(self):
        for frameClass in self.frames.keys():
            frame = frameClass(self.contenedor,self)
            self.frames[frameClass] = frame

    def mostrar_frame(self, frame_Class):
        frame = self.frames[frame_Class]
        frame.tkraise()
    
def main():
    app = Manager()
    app.mainloop()

def Salir():
    resp = messagebox.askquestion("SALIR","¿Desea Cerrar la Aplicación?")
    if resp == "yes":
        quit()

if __name__ == '__main__':
    main()