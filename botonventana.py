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
#https://recursospython.com/guias-y-manuales/caja-de-texto-entry-tkinter/
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("300x300")
 
    # A Label widget to show in toplevel
    Label(newWindow,text ="Agregar evento").pack()

    entry = ttk.Entry(newWindow,width=5)
    entry.place(x=10, y=10)


boton1=ttk.Button(text="agregar",command=openNewWindow)
boton1.place(x=10,y=100)



root.mainloop()