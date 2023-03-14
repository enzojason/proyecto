
#from tkinter import * 
#raiz = Tk()

import tkinter as tk
raiz=tk.Tk()

raiz.title("Calendario") #Cambiar el nombre de la ventana
raiz.geometry("500x400")
raiz.iconbitmap("calendario.ico") #Cambiar el icono
#raiz.config(bg="blue") #Cambiar color de fondo
raiz.resizable(0,0) #si la ventana es manipulable de x,y 0,0=NO redimencionar

#FRAME
from tkinter import *
mi_Frame=Frame()
mi_Frame.pack(side="bottom",padx=10)
mi_Frame.config(bg="grey")
mi_Frame.config(width="550",height="320")
#mi_frame.config(cursor=),se edita el cursor

#label
lunes=Label(mi_Frame,text="Lunes Martes Miercoles Jueves Viernes Sabado Domingo")
lunes.place(x=5,y=15)
lunes.config(fg="black",bg="white",font=("Verdana",12))



raiz.mainloop()
