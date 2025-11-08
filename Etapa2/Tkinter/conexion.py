import mysql.connector
from mysql.connector import Error
from tkinter import ttk,messagebox

class Conexion:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host = 'localhost',
                user ='root',
                password ='fuser',
                database = 'biblioteca'
            )
        except Error as e:
            messagebox.showerror("Error", str(e))
    
    def conectar(self):
        return self.con

    