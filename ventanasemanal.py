import calendar
import locale
import datetime
import tkinter as tk
from centralizacion import centrar
locale.setlocale(locale.LC_ALL, '')
from tkinter import *

raiz=tk.Tk()
raiz.title("Calendario") #Cambiar el nombre de la ventana
raiz.geometry("500x400")
centrar(raiz,550,400)
raiz.iconbitmap("calendario.ico") #Cambiar el icono
raiz.resizable(0,0) #si la ventana es manipulable de x,y 0,0=NO redimencionar

x=datetime.datetime.now()
fecha=x.strftime("%A %d/%m/%Y")
labelfecha=Label(raiz,text=fecha)
labelfecha.place(x=310,y=5)
labelfecha.config(fg="black",font=("Verdana",12))

from tkinter import *
mi_Frame=Frame()
mi_Frame.pack(padx=10,pady=100)
mi_Frame.config(width="550",height="420")
mi_Frame.config(bg="grey")

#label encabezado fecha
encabezado=Label(raiz,text="Lunes     Martes     Miercoles  Jueves   Viernes     Sabado    Domingo")
encabezado.place(x=20,y=75)
encabezado.config(fg="black",bg="white",font=("Verdana",11))


def cambiar_mensual():
    from main import raiz as r
    r.mainloop()
    raiz.destroy()
    
from tkinter import ttk
#CAMBIAR EL CALENDARIO A MENSUAL
cambiar=ttk.Button(raiz,text="Calendario Mensual",command=cambiar_mensual)
cambiar.place(x=5,y=10)

#funcion que muestra el calendario SEMANAL
def mostrar_calendario(anio,mes):
    cal=calendar.Calendar()
    mes = cal.monthdayscalendar(anio,mes)
    print(mes)
    semana=mes[0]
    for x in range(len(semana)):
        if x==0:
            celda=Label(mi_Frame,height=9,width=6,text="-",bg="grey")
        else:
            celda=Label(mi_Frame,height=9,width=6,text=x,bg="grey")
        celda.config(fg="black",bg="white",font=("Verdana",13))
        celda.grid(padx=1,pady=1,row=0,column=x)


x=datetime.datetime.now()               
m=x.strftime("%m")
mes=int(m)
a=x.strftime("%Y")
anio=int(a)
mostrar_calendario(anio,mes)
raiz.mainloop()