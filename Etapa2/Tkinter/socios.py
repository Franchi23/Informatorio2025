from tkinter import *
import tkinter as tk
import os
from tkinter import ttk,messagebox
from tkcalendar import Calendar,DateEntry
from PIL import Image, ImageTk
from conexion import Conexion
from mysql.connector import Error

indexcbo =0
Nro =0 
class Socios(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)    
        self.widgets()
    
    def agregar_socios(self):                      # Funcion para pasar los text a la grilla
        #Nro = self.entry_nro_Socio.get()
        nrodoc= self.entry_documento.get()
        nombre =self.entry_nombre.get()
        domicilio=self.entry_domicilio.get()
        telefono=self.entry_telefono.get()
        mail=self.entry_mail.get()
        sexo=self.cbo_sexo.get()
        indexcbo = self.cbo_sexo.current()
        fecha=self.label_fecha_nac._calendar.get_date()
        #PASA LOS DATOS DE LAS CAJAS A LA GRILLA
        if (nombre == "") or (domicilio =="") or (telefono ==""):
            messagebox.showwarning("Hay datos necesarios en blanco", "No se puede agregar un socio sin nombre, domicilio o telefono")
            return
        else:
            self.tree.insert("",tk.END, values=("1",nombre,domicilio,telefono,mail,sexo,fecha))
            self.limpiar_text()
    
    #Funcion para vaicar los text y dejarlos limpios para volver a cargarlos
    def limpiar_text(self):
        #Para limpiar los text
        self.entry_nombre.delete(0,tk.END)
        self.entry_documento.delete(0,tk.END)
        self.entry_mail.delete(0,tk.END)
        self.entry_telefono.delete(0,tk.END)
        self.entry_domicilio.delete(0,tk.END)
        self.cbo_sexo.set("")
        self.entry_documento.focus()
        indexcbo =0
        #self.label_fecha_nac
    
    #Verifica que se ingresen datos necesarios
    def validacion(self,documento, nombre,domicilio,telefono, mail):
        pass
        if not (documento and nombre and domicilio and telefono and mail):
            return False
        else:
            return True

    #Funcion que efectua el ingreso de los datos en los text
    #a la tabla en la base de datos
    def insertar_socios(self):

        if self.validacion(self.entry_documento.get(),self.entry_nombre.get(),self.entry_domicilio.get(),self.entry_telefono.get(),self.entry_mail.get()):
            con = Conexion().conectar()            
            c =con.cursor()
            try:
                c.execute("Select MAX(idSocio) from socios")
                nro = c.fetchone()[0]
                if nro:
                    nro +=1
                else:
                    nro =1

                if self.consultar_documento() == 0:
                    sql="Insert into socios (idsocio,documento,nombre,domicilio,telefono,mail,sexo) values (%s,%s,%s,%s,%s,%s,%s)"
                    valores =(nro,self.entry_documento.get(),self.entry_nombre.get(),self.entry_domicilio.get(),self.entry_telefono.get(),self.entry_mail.get(),self.cbo_sexo.get())#,self.label_fecha_nac._calendar.get_date())
                    c.execute(sql,valores)
                    con.commit()
                    messagebox.showinfo("Informacion","Registro insertado correctamente")
                    self.limpiar_text()
                else:
                    messagebox.showerror("Por Favor Verifique","Ya existe un socio cargado con ese numero de documento. Por favor verifique")

            except Error as e:
                messagebox.showerror("Se produjo un Error al devolver los datos. Por favor verifique", str(e))
            finally:
                con.close()
        else:
            messagebox.showerror("Validar Datos","Se produjo un Error. Hay datos necesarios que no fueron ingresados. Por favor verifique")
    
    #Verifica que no exista un documento igual al que se ingresa
    #ya cargado en la base
    def consultar_documento(self):
        try:
            nro = 0
            con = Conexion().conectar()            
            c= con.cursor()
            valor =(self.entry_documento.get(),)
            sql="Select idsocio from socios where documento= %s"

            c.execute(sql, valor)
            nro = c.fetchone()
            
            if nro is not None:
            #if nro[0] > 0:
                return nro
            else:
                return 0
            
        except Error as e:
            messagebox.showerror("Se produjo un Error al buscar el documento. Por favor verifique", str(e))
        finally:
            con.close()

    def widgets(self):
#----------------------------------------------------------------------------------------------------
#           PRIMER FRAME - EL TITULO DE LA VENTANA

        frame1= tk.Frame(self,bg="#dddddd",highlightbackground="gray",highlightthickness=1)
        frame1.pack()
        frame1.place(x=0,y=0,width=1100, height=100)

        title =tk.Label(self,text="SOCIOS",bg="#dddddd",font="sans 30 bold", anchor="center")
        title.pack()
        title.place(x=5,y=0,width=1090,height=90)
#-----------------------------------------------------------------------------------------------------
#           EL CUERPO DE LA VENTANTA - EL OTRO CONTENEDOR Y LOS LABELS Y LAS CAJAS DE TEXTO        
        frame2= tk.Frame(self, bg="#C6D9E3",highlightbackground="gray",highlightthickness=2)
        frame2.place(x=0,y=100, width=1100, height=550)

        lblframe = LabelFrame(frame2,text="Informacion de los Socios", bg="#C6D9E3",font="sans 16 bold")
        lblframe.place(x=10,y=10,width=1070,height=520)

        label_nro_Socio = tk.Label(lblframe,text="Nro de Socio: ",bg="#C6D9E3",font="sans 12 bold")
        label_nro_Socio.place(x=10,y=5)
        self.nro_Socio = tk.StringVar()                     # para almacenar el nro de socio
        self.entry_nro_Socio = tk.Entry(lblframe,textvariable=self.nro_Socio,state="readonly",font="sans 12 bold")
        self.entry_nro_Socio.place(x=130,y=5,width=100)

        #NRO DOCUMENTO
        label_nrodoc =tk.Label(lblframe,text="Documento: ",bg="#C6D9E3",font="sans 12 bold")
        label_nrodoc.place(x=10,y=35)
        self.entry_documento = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_documento.place(x=130,y=35,width=100)
        self.entry_documento.focus_set()
        #NOMBRE
        label_nombre =tk.Label(lblframe,text="Nombre: ",bg="#C6D9E3",font="sans 12 bold")
        label_nombre.place(x=10,y=65)
        self.entry_nombre = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_nombre.place(x=130,y=65,width=280)
        self.entry_nombre.focus_set()
        #DOMICILIO
        label_domicilio =tk.Label(lblframe,text="Domicilio: ",bg="#C6D9E3",font="sans 12 bold")
        label_domicilio.place(x=10,y=95)
        self.entry_domicilio = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_domicilio.place(x=130,y=95,width=280)
        #FECHA NACIMIENTO
        label_fecha_nac =tk.Label(lblframe,text="Fe Nacimiento: ",bg="#C6D9E3",font="sans 12 bold")
        label_fecha_nac.place(x=10,y=125)
        #self.label_fecha_nac = tk.Entry(lblframe,font="sans 12 bold")
        self.label_fecha_nac = DateEntry(lblframe,font="sans 12 bold",date_pattern='dd/mm/yyyy') #Que muestre dia/mes/año
        self.label_fecha_nac.place(x=130,y=125,width=120)
        #SEXO
        label_sexo =tk.Label(lblframe,text="Sexo: ",bg="#C6D9E3",font="sans 12 bold")
        label_sexo.place(x=10,y=155)
        self.opcionesCBO =["M","F"]
        #self.cbo_sexo = ttk.Combobox(lblframe,font="sans 12 bold",values=["M", "F"])
        self.cbo_sexo = ttk.Combobox(lblframe,font="sans 12 bold",values=self.opcionesCBO)
        self.cbo_sexo.place(x=130,y=155,width=70)
        #MAIL
        label_mail =tk.Label(lblframe,text="E-Mail: ",bg="#C6D9E3",font="sans 12 bold")
        label_mail.place(x=10,y=185)
        self.entry_mail = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_mail.place(x=130,y=185,width=280)
        #TELEFONO
        label_telefono =tk.Label(lblframe,text="Telefono:  ",bg="#C6D9E3",font="sans 12 bold")
        label_telefono.place(x=10,y=215)
        self.entry_telefono = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_telefono.place(x=130,y=215,width=280)


        #Buscar
        lbl1 =tk.Label(lblframe,text="Buscar : ",bg="#C6D9E3",font="sans 12 bold")
        lbl1.place(x=550,y=215)

        self.cbo_buscar = ttk.Combobox(lblframe,font="sans 11 bold",values=["ID","Documento", "Nombre"])
        self.cbo_buscar.place(x=620,y=215,width=110)
        self.cbo_buscar.bind("<Return>",  self.funcion_foco)
        self.cbo_buscar.bind("<<ComboboxSelected>>", self.funcion_foco)

        self.entry_buscar = tk.Entry(lblframe,font="sans 12 bold")
        self.entry_buscar.place(x=740,y=215,width=270)   
        self.entry_buscar.bind("<Return>",  self.verificar_y_llamar)


        #FRAME DE LA GRILLA
        treeframe = tk.Frame(frame2,bg="#C6D9E3")
        treeframe.place(x=30,y=290,width=1030,height=150)

        scrol_y= ttk.Scrollbar(treeframe,orient=VERTICAL)
        scrol_y.pack(side=RIGHT,fill=Y)

        scrol_x= ttk.Scrollbar(treeframe,orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM,fill=X)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#           GRILLA 
        self.tree = ttk.Treeview(treeframe,columns=("Socio","Documento","Nombre","Domicilio","Telefono","Mail","Sexo","Fecha"), show="headings",height=10,yscrollcommand=scrol_y.set,xscrollcommand=scrol_x.set)
        scrol_y.config(command=self.tree.yview)
        scrol_x.config(command=self.tree.xview)

        #Encabezados de la GRILLA
        self.tree.heading("#1",text="Socio")
        self.tree.heading("#2",text="Documento")
        self.tree.heading("#3",text="Nombre")
        self.tree.heading("#4",text="Domicilio")
        self.tree.heading("#5",text="Telefono")
        self.tree.heading("#6",text="Mail")
        self.tree.heading("#7",text="Sexo")
        self.tree.heading("#8",text="Fecha")

        #Columnas
        self.tree.column("Socio", anchor="center")
        self.tree.column("Documento", anchor="center")
        self.tree.column("Nombre", anchor="center")
        self.tree.column("Domicilio", anchor="center")
        self.tree.column("Telefono", anchor="center")
        self.tree.column("Mail", anchor="center")
        self.tree.column("Sexo", anchor="center")
        self.tree.column("Fecha", anchor="center")

        self.tree.pack(expand=True,fill="both")     #Arma la grilla y la muestra con el metodo pack
        self.tree.bind("<Double-1>", self.DobleClickTree)

        #Barra de opciones abajo
        lblframe1 = LabelFrame(frame2,text="Opciones", bg="#C6D9E3",font="sans 12 bold")
        lblframe1.place(x=30,y=450,width=1030,height=70)

        #BOTONES
        btn_agregar = tk.Button(lblframe1,text="Agregar ",bg="lightgrey",font="sans 12 bold",command=self.insertar_socios)
        btn_agregar.place(x=10,y=5, width=150,height=30)

        btn_baja = tk.Button(lblframe1,text="Baja ",bg="lightgrey",font="sans 12 bold")
        btn_baja.place(x=170,y=5, width=150,height=30)

        btn_modificar = tk.Button(lblframe1,text="Modificar ",bg="lightgrey",font="sans 12 bold",command=self.editar_socios)
        btn_modificar.place(x=335,y=5, width=150,height=30)

        btn_buscar = tk.Button(lblframe1,text="Buscar ",bg="lightgrey",font="sans 12 bold")
        btn_buscar.place(x=500,y=5, width=150,height=30)

        btn_cerrar = tk.Button(lblframe1,text="Cerrar ",bg="lightgrey",font="sans 12 bold",command=self.master.destroy)
        btn_cerrar.place(x=835,y=5, width=150,height=30)
        
        #IMAGEN DE LOS SOCIOS
        dir= os.path.dirname(os.path.abspath(__file__))
        ruta_imagen = os.path.join(dir,'imagenes','socios1.png')
        self.logo_image = Image.open(ruta_imagen)
        self.logo_image = self.logo_image.resize((270,200))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame2, image=self.logo_image, bg="#C6D9E3") 
        self.logo_label.place(x=750,y=40)

        self.entry_documento.focus_set()
        self.cargar_socios(self.tree,"1=1")

    #PARA PASAR DE LA GRILLA A LOS TEXT
    def editar_socios(self):            #VER ESTO
        self.limpiar_text()         #Funcion para borrar el contenido de los textbox
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Editar Socios","No se selecciono ningun socio de la grilla para editar")
            return
        
        item_id= self.tree.item(seleccion)["text"]
        item_values =self.tree.item(seleccion)["values"]
        self.entry_nro_Socio.insert(0, item_values[0])
        self.entry_documento.insert(0, item_values[1])
        self.entry_nombre.insert(0,item_values[2])
        self.entry_domicilio.insert(0,item_values[3])
        self.entry_telefono.insert(0,item_values[4])
        self.entry_mail.insert(0,item_values[5])
        self.label_fecha_nac.set_date(0,item_values[7])
        self.cbo_sexo.current(indexcbo)

        ventana_buscar = Toplevel(self)
        ventana_buscar.title("Buscar Socios")
        ventana_buscar.geometry ("800x500")
        ventana_buscar.config(bg="#C6D9E3")
        ventana_buscar.resizable(False,False)

        frame1= tk.Frame(ventana_buscar,bg="#dddddd",highlightbackground="gray",highlightthickness=1)
        frame1.pack()
        frame1.place(x=0,y=0,width=800, height=70)

        title =tk.Label(ventana_buscar,text="Buscar Socios",bg="#dddddd",font="sans 36 bold", anchor="center")
        title.pack()
        title.place(x=5,y=0,width=800,height=60)

        treeFrame = tk.Frame(ventana_buscar,bg="#C6D9E3")
        treeFrame.place(x=10,y=110,width=780,height=380)

        scrol_y= ttk.Scrollbar(treeFrame,orient=VERTICAL)
        scrol_y.pack(side=RIGHT,fill=Y)

        scrol_x= ttk.Scrollbar(treeFrame,orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM,fill=X)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#           GRILLA 
        treeSocios = ttk.Treeview(treeFrame,columns=("Socio","Documento","Nombre","Domicilio","Telefono","Mail"), show="headings",height=10,yscrollcommand=scrol_y.set,xscrollcommand=scrol_x.set)
        scrol_y.config(command=treeSocios.yview)
        scrol_x.config(command=treeSocios.xview)

        #Encabezados de la GRILLA
        treeSocios.heading("#1",text="Socio")
        treeSocios.heading("#2",text="Documento")
        treeSocios.heading("#3",text="Nombre")
        treeSocios.heading("#4",text="Domicilio")
        treeSocios.heading("#5",text="Telefono")
        treeSocios.heading("#6",text="E-Mail")

        #Columnas
        treeSocios.column("Socio", width=30, anchor="center")
        treeSocios.column("Documento", width=80, anchor="center")
        treeSocios.column("Nombre", width=200, anchor="center")
        treeSocios.column("Domicilio",width= 200, anchor="center")
        treeSocios.column("Telefono", width=80, anchor="center")
        treeSocios.column("Mail", width=90, anchor="center")

        lbl1 =tk.Label(ventana_buscar,text="Nombre : ",bg="#C6D9E3",font="sans 12 bold")
        lbl1.place(x=10,y=80)
        entry_nombre = tk.Entry(ventana_buscar,font="sans 12 bold")
        entry_nombre.place(x=90,y=80,width=280)
        entry_nombre.focus_set()

        btn_buscar_socio = tk.Button(ventana_buscar,text="Buscar ",bg="lightgrey",font="sans 12 bold", command="")
        btn_buscar_socio.place(x=380,y=80, width=100,height=25)

        treeSocios.pack(expand=True,fill="both")     #Arma la grilla y la muestra con el metodo pack
        treeSocios.bind("<Double-1>", self.DobleClickTree)

        self.cargar_socios(self.tree,"1=1")

    #Muestra todos los socios al abrir la ventana de busqueda
    def cargar_socios(self,tree,sql):
            try:
                con = Conexion().conectar()            
                c= cursor=con.cursor()
                #c.execute("select idsocio,documento,nombre,domicilio, telefono,mail from socios where 1=1")
                c.execute("select idsocio,documento,nombre,domicilio, telefono,mail from socios where %s", ( str(sql),))
        
                socios_db= cursor.fetchall()
                for socio in socios_db:
                    tree.insert("",'end',values = socio)
                con.close()
            except Error as e:
                messagebox.showerror("Cargar Socios","Se produjo un Error al devolver los datos. Por favor verifique", str(e))
            finally:
                con.close()

    

    
    
    
    
    
    
    #Doble click en la grilla para que se cierre la ventana y los datos
    #pasen al formulario para ser editados
    def DobleClickTree(self, event):
        self.editar_socios()

    #La caja de texto buscar recibe el foco
    def funcion_foco(self,event):
        self.entry_buscar.focus()
    
    #Si el textbox buscar es distinto de "" arma la consulta y la ejecuta
    def verificar_y_llamar(self,event):
        contenido = self.entry_buscar.get()
        select = self.cbo_buscar.current()
        if contenido and select >=0:
            if select == 0:  #IdSocio
                self.cargar_socios(self.tree,"idsocio =  ", ( str(self.entry_buscar.get()),))
            elif select ==1:    #Documento
                valor =("documento = ?", (self.entry_buscar.get(),))
                self.cargar_socios(self.tree,valor)
            else:               #Nombre
                self.cargar_socios(self.tree,"nombre like ", ('%' + str(self.entry_buscar.get() + '%',)))
                
            
            #sql="Select idsocio from socios where documento= %s"