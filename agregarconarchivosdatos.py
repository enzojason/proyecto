
#from tkinter import * 
#raiz = Tk()
import calendar
import locale
import datetime
import tkinter as tk

raiz=tk.Tk()

raiz.title("Calendario") #Cambiar el nombre de la ventana
raiz.geometry("500x400")
#raiz.iconbitmap("calendario.ico") #Cambiar el icono
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

#funcion que muestra el calendario grande
def mostrar_calendario(anio,mes):
    calendario=calendar.monthcalendar(anio,mes)
    for f in range(len(calendario)):
        for c in range(0, 7):
            if calendario[f][c]==0:
                pass
            else:
                celda = Label(mi_Frame,height=2,width=8,text=calendario[f][c])
                celda.grid(padx=2, pady=2, row=f, column=c)

#funcion mostrar_calendario ejecutada, y datos de año y mes actualizados a tiempo real
m=x.strftime("%m")
mes=int(m)
a=x.strftime("%Y")
anio=int(a)
mostrar_calendario(anio,mes)

#clase evento 
class Eventos():
    def __init__(self,titulo,importancia,fecha_recordatorio,fecha_hora,duracion=1,descripcion="",etiquetas=""):
        """Se crea el objeto evento"""
        self.titulo=titulo
        self.fecha_hora=fecha_hora
        self.descripcion=descripcion
        self.importancia=importancia
        self.fecha_recordatorio=fecha_recordatorio
        self.etiquetas=etiquetas
    
    def guardar_evento(self):
        #eventos=dict()
        #evento["Titulo"]:self.titulo
        with open("eventos.json",'w') as archivo:
            archivo.write(self.titulo)


#label.focus_set() #SET THE FOCUS 
#mostrar mensaje de evento agregado


#Abrir la ventana cuando el boton agregar es ejecutado.
def abrir_ventana():

    ventananueva = Toplevel(raiz)
    import tkinter as tk
    from tkinter import messagebox,ttk
    #ventananueva.iconbitmap("calendario.ico")
    ventananueva.title("Agregar evento")
    ventananueva.geometry("270x420")

    #CREACION DE DIAS Y MESES EN LISTA
    dias=list()
    meses=list()
    anios=[2020,2021,2022,2023,2024]
    for x in range(31):
        dias.append(x)
    for y in range(12):
        meses.append(calendar.month_name[y])
       
    #Label titulo
    titulol=Label(ventananueva,text="Titulo:")
    titulol.place(x=50,y=8)
    
    tituloe=ttk.Entry(ventananueva)
    tituloe.config(width=14)
    tituloe.place(x=95,y=8)

    #Label Dia,
    dial=Label(ventananueva,text="Dia:")
    dial.place(x=65,y=32)

    mesl=Label(ventananueva,text="Mes:")
    mesl.place(x=62,y=62)

    aniol=Label(ventananueva,text="Año:")
    aniol.place(x=62,y=92)

    horal=Label(ventananueva,text="Duración:")
    horal.place(x=40,y=122)
    
    #combo dias
    combo_dias = ttk.Combobox(
    ventananueva,
    state="readonly",
    values=dias,
    width="3",
    )
    combo_dias.pack()
    combo_dias.place(x=95,y=32)
    #combo_dias.set(9) # PONE EL TEXTO EN COMBOS DIAS COMO OPCION

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

    Label(ventananueva,text="hs").place(x=115,y=122)
    Label(ventananueva,text="min").place(x=160,y=122)


    #SELECCION BOTONES, NORMAL E IMPORTANTE
    Radiobutton(ventananueva,
            text="Normal",
            value=1,
            ).place(x=10,y=150)

    Radiobutton(ventananueva,
            text="Importante",
            value=2,
            ).place(x=10,y=175)


    #LABEL RECORDATORIO
    Label(ventananueva,text="---------------Recordatorio---------------").place(x=10,y=220)
    #entrada hora
    diar =ttk.Entry(ventananueva)
    diar.place(x=95,y=250)
    diar.config(width="2")
    diar.insert(0,1)

    #entrada minutos
    horaer =ttk.Entry(ventananueva)
    horaer.place(x=160,y=250)
    horaer.config(width="3")
    horaer.insert(0,"00")

    Label(ventananueva,text="Dia:").place(x=65,y=250)
    Label(ventananueva,text="Hora:").place(x=120,y=250)

    

    descripcion=Label(ventananueva,text="Descripción:").place(x=5,y=280)

    #descripcion_entrada=ScrolledText.ScrolledText(ventananueva)
    #descripcion_entrada.place(x=5,y=290)

    #AREA DE TEXTO , DESCRIPCION
    descripcion_texto = Text(ventananueva, height=5,width=32)
    descripcion_texto.pack()
    descripcion_texto.place(x=4,y=300)

    
    
    #fecha_hora=combo_dias.get()+ combo_meses.get()+combo_anios.get()
    #descripcion=descripcion_texto.get()
    #importancia= IntVar()
    #fecha_recordatorio=diar.get()+horaer()

    def agregado():
    #titulo,importancia,fecha_recordatorio,fecha_hora,descripcion):
        import tkinter as tk
        from tkinter import messagebox,ttk
        messagebox.showinfo(message="Evento Agregado", title="Calendario")
        titulo=tituloe.get()
        x=open("hoja.txt",'w')
        x.write(titulo)
        x.close()
    
    #nuevoevento=Eventos(titulo,importancia,fecha_recordatorio,fecha_hora,descripcion)
    #nuevoevento.guardar_evento()
    #BOTON AGREGAR LISTO
    boton_listo=ttk.Button(ventananueva,text="Agregar",command=agregado)
    boton_listo.pack()
    boton_listo.place(x=85,y=390)

  
#botonagregar
boton1=Button(raiz,text="Agregar\nEvento",command=abrir_ventana)
boton1.config(width=7,height=3)
boton1.place(x=210,y=320)

raiz.mainloop()
