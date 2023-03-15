import tkinter as tk
from tkinter import messagebox,ttk

root=tk.Tk()
root.config(width=300,height=200)

#saluda con una ventana nueva y muestra el mensaje
def saludar():
    messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")


boton=ttk.Button(text="hola",command=saludar)
boton.place(x=50,y=50)


#BOTON AGREGARR 
from tkinter import *
from tkinter.ttk import *

#Abrir la ventana cuando el boton agregar es ejecutado.
def abrir_ventana():
     
    # Toplevel object which will
    # be treated as a new window
    ventananueva = Toplevel(root)
    ventananueva.iconbitmap("calendario.ico")
    # sets the title of the
    # Toplevel widget
    ventananueva.title("Agregar evento")
 
    # sets the geometry of toplevel
    ventananueva.geometry("250x200")
    
    #Label Dia,
    dial=Label(ventananueva,text="Dia:")
    dial.place(x=65,y=32)
    celda=Entry(ventananueva,width=10)
    celda.place(x=95,y=32)

    mesl=Label(ventananueva,text="Mes:")
    mesl.place(x=65,y=62)
    celd=Entry(ventananueva,width=10)
    celd.place(x=95,y=62)

boton1=ttk.Button(text="agregar",command=abrir_ventana)
boton1.place(x=10,y=100)


root.mainloop()