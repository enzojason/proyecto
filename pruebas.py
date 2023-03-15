
#from tkinter import * 
#raiz = Tk()
import calendar
import locale
import datetime
import tkinter as tk
raiz=tk.Tk()

raiz.title("Calendario") #Cambiar el nombre de la ventana
raiz.geometry("500x400")
raiz.iconbitmap("calendario.ico") #Cambiar el icono
raiz.resizable(0,0) #si la ventana es manipulable de x,y 0,0=NO redimencionar

#label fecha actual
locale.setlocale(locale.LC_ALL, '')
from tkinter import *
x=datetime.datetime.now()
fecha=x.strftime("%A %d/%m/%Y")
labelfecha=Label(raiz,text=fecha)
labelfecha.place(x=310,y=5)
labelfecha.config(fg="black",font=("Verdana",12))

#label encabezado fecha
encabezado=Label(raiz,text="Lunes     Martes     Miercoles  Jueves   Viernes    Sabado   Domingo")
encabezado.place(x=20,y=75)
encabezado.config(fg="black",bg="white",font=("Verdana",10))


#FRAME
from tkinter import *
mi_Frame=Frame()
mi_Frame.pack(padx=10,pady=100)
mi_Frame.config(width="550",height="720")
mi_Frame.config(bg="grey")

#mi_frame.config(cursor=),se edita el cursor


#dias de la semana labels
from tkinter import *

calendario=calendar.monthcalendar(2023,3)
for r in range(len(calendario)):
    for c in range(0, 7):
        if calendario[r][c]==0:
            pass
        else:
            cell = Label(mi_Frame,height=2,width=8,text=calendario[r][c])
            cell.grid(padx=2, pady=2, row=r, column=c,sticky=S)


raiz.mainloop()
