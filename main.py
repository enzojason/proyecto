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
centrar(raiz,500,400)
raiz.iconbitmap("calendario.ico") #Cambiar el icono
raiz.resizable(0,0) #si la ventana es manipulable de x,y 0,0=NO redimencionar

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
    def __init__(self,titulo,fecha,hora,importancia,fecha_recordatorio,duracion=1,descripcion="",etiquetas=""):
        """Se crea el objeto evento"""
        self.titulo=titulo
        self.fecha=fecha
        self.hora=hora
        self.descripcion=descripcion
        self.importancia=importancia
        self.fecha_recordatorio=fecha_recordatorio
        self.etiquetas=etiquetas
    
    def guardar_evento(self):
        import json
        datos={"Titulo":self.titulo,"Fecha":self.fecha,"Hora":self.hora,"Importancia":self.importancia,"Fecha Recordatorio":self.fecha_recordatorio,"Descripcion":self.descripcion}
        with open("eventos.json",'w') as archivo:
            json.dump(datos,archivo)


#label.focus_set() #SET THE FOCUS 
#mostrar mensaje de evento agregado


#Abrir la ventana cuando el boton agregar es ejecutado.
def abrir_ventana():
    from centralizacion import centrar
    import tkinter as tk
    from tkinter import messagebox,ttk
    ventananueva = Toplevel(raiz)
    ventananueva.title("Agregar evento")
    ventananueva.geometry("270x420")
    centrar(ventananueva,270,420)
    #ventananueva.iconbitmap("calendario.ico")
    
    
    #CREACION DE HORAS,DIAS Y MESES EN LISTA
    dias=list()
    meses=list()
    horas=list()
    anios=[2020,2021,2022,2023,2024]
    for x in range(31):
        dias.append(x)
    for y in range(12):
        meses.append(calendar.month_name[y])
    for z in range(23):
        horas.append(z)   

    #Label titulo
    titulol=Label(ventananueva,text="Titulo:")
    titulol.place(x=50,y=8)
    
    #Entrada titulo
    tituloe=ttk.Entry(ventananueva)
    tituloe.config(width=18)
    tituloe.place(x=95,y=8)

    #Label Dia mes año duracion horas
    dial=Label(ventananueva,text="Dia:")
    dial.place(x=65,y=32)

    mesl=Label(ventananueva,text="Mes:")
    mesl.place(x=62,y=62)

    aniol=Label(ventananueva,text="Año:")
    aniol.place(x=62,y=92)

    duracionl=Label(ventananueva,text="Duración:")
    duracionl.place(x=40,y=122)
    
    horal=Label(ventananueva,text="Hora:")
    horal.place(x=134,y=32)

    #combo dias
    combo_dias = ttk.Combobox(
    ventananueva,
    state="readonly",
    values=dias,
    width="2",
    )
    combo_dias.pack()
    combo_dias.place(x=95,y=32)
    #combo_dias.set(9) # PONE EL TEXTO EN COMBOS DIAS COMO 
    
    #combo horas
    combo_horas=ttk.Combobox(
    ventananueva,
    state="readonly",
    values=horas,
    width=2,
    )
    combo_horas.pack
    combo_horas.place(x=172,y=32)

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

    #entrada duracion horas
    horaed =ttk.Entry(ventananueva)
    horaed.place(x=95,y=122)
    horaed.config(width="2")
    horaed.insert(0,1)

    #entrada minutos
    minutosed =ttk.Entry(ventananueva)
    minutosed.place(x=139,y=122)
    minutosed.config(width="3")
    minutosed.insert(0,"00")

    Label(ventananueva,text="hs").place(x=115,y=122)
    Label(ventananueva,text="min").place(x=160,y=122)

    radioValue = tk.IntVar()
    radioValue.set(1)
    #SELECCION BOTONES, NORMAL E IMPORTANTE
    Radiobutton(ventananueva,
            text="Normal",
            variable=radioValue,
            value=1,
            ).place(x=10,y=150)

    Radiobutton(ventananueva,
            text="Importante",
            variable=radioValue,
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
        import json
        import tkinter as tk
        from tkinter import messagebox,ttk
        messagebox.showinfo(message="Evento Agregado", title="Calendario")
        

        titulo=tituloe.get()
        
        diac=combo_dias.get()
        mesc=combo_meses.get()
        aniosc=combo_anios.get()

        fecha=diac+"/"+mesc+"/"+aniosc
    
        horac=combo_horas.get()
        
        hora=horaed.get()
        minuto=minutosed.get()
        duracion='{}:{}'.format(hora,minuto)
        
        hora_recor=horaer.get()
        dia_recor=diar.get()

        fecha_recordatorio=dia_recor+","+hora_recor

        descripcion=descripcion_texto.get("1.0","end")

        if radioValue==2:
            importancia="Importante"
        else:
            importancia="Normal"
    
        t=titulo
        t=Eventos(titulo,fecha,hora,importancia,fecha_recordatorio,duracion,descripcion)
        t.guardar_evento()
        t=0
        ventananueva.destroy()
    #BOTON AGREGAR LISTO
    boton_listo=ttk.Button(ventananueva,text="Agregar",command=agregado)
    boton_listo.pack()
    boton_listo.place(x=85,y=390)

    
  
#botonagregar
boton1=Button(raiz,text="Agregar\nEvento",command=abrir_ventana)
boton1.config(width=7,height=3)
boton1.place(x=210,y=320)

raiz.mainloop()
