import tkinter as tk
from tkinter import messagebox,ttk
import calendar
import locale
locale.setlocale(locale.LC_ALL, '')

root=tk.Tk()
root.config(width=300,height=200)

#saluda con una ventana nueva y muestra el mensaje
def saludar():
    messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")

#label.focus_set() #SET THE FOCUS 


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
    ventananueva.geometry("250x250")
    #CREACION DE DIAS Y MESES EN LISTA
    dias=list()
    meses=list()
    anios=[2020,2021,2022,2023,2024]
    for x in range(31):
        dias.append(x)
    for y in range(12):
        meses.append(calendar.month_name[y])
       
        
    
    #Label Dia,
    dial=Label(ventananueva,text="Dia:")
    dial.place(x=65,y=32)

    mesl=Label(ventananueva,text="Mes:")
    mesl.place(x=65,y=62)

    aniol=Label(ventananueva,text="Año:")
    aniol.place(x=65,y=92)

    horal=Label(ventananueva,text="Duración:")
    horal.place(x=40,y=122)
    Label(ventananueva,text="hs").place(x=115,y=122)
    Label(ventananueva,text="min").place(x=160,y=122)

    #combo dias
    combodias = ttk.Combobox(
    ventananueva,
    state="readonly",
    values=dias,
    width="3",
    )
    combodias.pack()
    combodias.place(x=95,y=32)
    #combodias.set(9) # PONE EL TEXTO EN COMBOS DIAS COMO OPCION

    #combo meses
    combo_meses = ttk.Combobox(
    ventananueva,
    state="readonly",
    values=meses,
    width="10",
    )
    combo_meses.pack()
    combo_meses.place(x=95,y=62)

    #combo años
    combo_anios = ttk.Combobox(
    ventananueva,
    state="readonly",
    values=anios,
    width="7",
    )
    combo_anios.pack()
    combo_anios.place(x=95,y=92)
    combo_anios.set(2023)

    #entrada hora
    horae =ttk.Entry(ventananueva)
    horae.place(x=95,y=122)
    horae.config(width="2")
    horae.insert(0,1)

    #entrada minutos
    minutose =ttk.Entry(ventananueva)
    minutose.place(x=139,y=122)
    minutose.config(width="3")
    minutose.insert(0,"00")

    Radiobutton(ventananueva,
            text="Normal",
            value=1,
            ).place(x=10,y=150)

    Radiobutton(ventananueva,
            text="Importante",
            value=2,
            ).place(x=10,y=175)

    
#botonagregar
boton1=ttk.Button(text="agregar",command=abrir_ventana)
boton1.place(x=10,y=100)


root.mainloop()
