import calendar
import locale
import datetime
import tkinter as tk
from centralizacion import centrar
locale.setlocale(locale.LC_ALL, '')
from tkinter import *

#clase evento 
class Eventos():
    def __init__(self,titulo,fecha,importancia,fecha_recordatorio,duracion=1,descripcion="",etiquetas=""):
        """Se crea el objeto evento"""
        self.titulo=titulo
        self.fecha=fecha
        self.descripcion=descripcion
        self.importancia=importancia
        self.fecha_recordatorio=fecha_recordatorio
        self.etiquetas=etiquetas

    import json
    js=open("eventos.json",'w')
    js.close()

    def agregar_evento():
        #agrega eventos en archivo json
        import json
        with open("datos.json",'r+') as ar:
            data=json.load(ar)

        with open("eventos.json",'r')as arc:
            dataj=json.load(arc)
        dataj.append(data)
        with open("eventos.json",'w') as archivo:
            json.dump(dataj,archivo)
            
raiz=tk.Tk()
raiz.title("Calendario") #Cambiar el nombre de la ventana
raiz.geometry("500x400")
centrar(raiz,550,400)
raiz.iconbitmap("calendario.ico") #Cambiar el icono
raiz.resizable(0,0) #si la ventana es manipulable de x,y 0,0=NO redimencionar

#LABEL FECHA ACTUAL
x=datetime.datetime.now()
fecha=x.strftime("%A %d de %B %Y")
labelfecha=Label(raiz,text=fecha)
labelfecha.place(x=310,y=15)
labelfecha.config(fg="black",font=("Verdana",12))
#datos de la fecha actual
d=x.strftime("%d")
dia_actual=int(d)            
m=x.strftime("%m")
mes=int(m)
a=x.strftime("%Y")
anio=int(a)

#label encabezado fecha
encabezado=Label(raiz,text="Lunes     Martes     Miercoles  Jueves   Viernes     Sabado    Domingo")
encabezado.place(x=20,y=75)
encabezado.config(fg="black",bg="white",font=("Verdana",11))

from tkinter import ttk
#BOTON CAMBIAR EL CALENDARIO A MENSUAL
cambiar=ttk.Button(raiz,text="Calendario Mensual")
cambiar.place(x=5,y=10)

#funcion que muestra el calendario SEMANAL
def mostrar_calendario(anio,mes,numero_semana):
    mi_Frame=Frame()
    mi_Frame.pack(padx=10,pady=100)
    mi_Frame.config(width="550",height="420")
    mi_Frame.config(bg="black")

    cal=calendar.Calendar()
    meses= cal.monthdayscalendar(anio,mes)
    semana=meses[numero_semana]
    for x in semana:
        celda=Label(mi_Frame,height=9,width=6,text=x,bg="grey")
        celda.config(fg="black",bg="white",font=("Verdana",13))
        celda.grid(padx=1,pady=1,row=0,column=x)


#calcular numero de semana donde se encuentra el dia en la matriz que se va a crear Mes
def calcular_semana_actual(anio,mes):
    calendario=calendar.Calendar()
    meses = calendario.monthdayscalendar(anio,mes)
    for a in range(len(meses)):
            semana=meses[a]
            for dias in semana:
                if dias==dia_actual:
                    numero_de_semana=a
    return numero_de_semana

def abrir_ventana():
    from centralizacion import centrar
    import tkinter as tk
    from tkinter import messagebox,ttk
    ventananueva = Toplevel(raiz)
    ventananueva.focus_set()
    ventananueva.title("Agregar evento")
    ventananueva.geometry("270x450")
    centrar(ventananueva,270,450)
    ##ventananueva.iconbitmap("calendario.ico")
    ##radioValue = tk.IntVar()
    
    #CREACION DE HORAS,DIAS Y MESES EN LISTA
    x=datetime.datetime.now()
    d=x.strftime("%d")
    dia_actual=int(d)            
    m=x.strftime("%m")
    mes=int(m)
    a=x.strftime("%Y")
    anio=int(a)
    h=x.strftime("%H")
    hora_actual=int(h)

    meses=list()
    horas=list()
    minutos=list()
    
    for y in range(13):
        if y==0:
            pass
        else:
            meses.append(calendar.month_name[y])

    for z in range(24):
        if z==0:
            pass 
        else:
            horas.append(z)

    for r in range(60):
        if r==0:
            pass
        else:
            minutos.append(r)    

    #Label nuevo evento
    ne=Label(ventananueva,text="Nuevo Evento")
    ne.place(x=25,y=15)
    ne.config(font=("Verdana",17))
    
    #Label titulo
    titulol=Label(ventananueva,text="Titulo:")
    titulol.place(x=20,y=75)

    #Entrada titulo
    tituloe=ttk.Entry(ventananueva)
    tituloe.focus_set()
    tituloe.config(width=25)
    tituloe.place(x=65,y=75)

    #Label fecha
    fecha=Label(ventananueva,text="Fecha:")
    fecha.place(x=20,y=115)
    fechan=x.strftime("%x")
    Label(ventananueva,text=fechan).place(x=65,y=115)
    #Label hora
    horal=Label(ventananueva,text="Hora:")
    horal.place(x=20,y=140)
    horaln=x.strftime("%X")
    Label(ventananueva,text=horaln).place(x=65,y=140)

    #label duracion
    duracionl=Label(ventananueva,text="Duración --->")
    duracionl.place(x=20,y=180)
    #entrada duracion horas
    horaed =ttk.Combobox(ventananueva,values=horas)
    horaed.place(x=95,y=180)
    horaed.config(width="3")
    horaed.insert(0,1)
    #entrada minutos
    minutosed =ttk.Combobox(ventananueva,values=minutos)
    minutosed.place(x=147,y=180)
    minutosed.config(width="3")
    minutosed.insert(0,"00")
    Label(ventananueva,text="hs").place(x=130,y=180)
    Label(ventananueva,text="min").place(x=185,y=180)
    
    #BOTONES importante y normal
    radio = tk.IntVar()
    Radiobutton(ventananueva,
            text="Normal",
            variable=radio,
            value=1,
            ).place(x=10,y=215)

    Radiobutton(ventananueva,
            text="Importante",
            variable=radio,
            value=2,
            ).place(x=10,y=240)
    
    
    #LABEL RECORDATORIO
    Label(ventananueva,text="---------------Recordatorio---------------").place(x=10,y=270)
    dias=list()
    for a in range(dia_actual):
        dd=dia_actual-a
        dias.append(dd)

    #dias combox recordatorio
    diar= ttk.Combobox(
    ventananueva,
    state="readonly",
    values=dias,
    width="3",
    )
    diar.pack()
    diar.place(x=40,y=300)
    Label(ventananueva,text="Dia:").place(x=15,y=300)
    horasr=list()
    for x in range(24):
        if x==0:
            pass
        else:
            horasr.append(x)

    #entrada horas combobox
    horaer=ttk.Combobox(
    ventananueva,
    state="readonly",
    values=horasr,
    width=3,
    )
    horaer.pack
    horaer.place(x=120,y=300)
    Label(ventananueva,text="Hora:").place(x=90,y=300)

    #entrada minutos
    minutoser =ttk.Combobox(ventananueva,values=minutos)
    minutoser.place(x=190,y=300)
    minutoser.config(width="3")
    Label(ventananueva,text="Min:").place(x=165,y=300)

    #label descripcion
    descripcion=Label(ventananueva,text="Descripción:").place(x=4,y=327)
    #texto descripcion
    descripcion_texto = Text(ventananueva, height=3,width=32)
    descripcion_texto.pack()
    descripcion_texto.place(x=4,y=350)
    
    def agregado():
    #titulo,importancia,fecha_recordatorio,fecha_hora,descripcion):
        import json
        import tkinter as tk
        from tkinter import messagebox,ttk
        messagebox.showinfo(message="Evento Agregado", title="Calendario")
        
        titulo=tituloe.get()

        #fechayhora=[fechan]+[horaln]
        fecha=fechan

        hora=horaed.get()
        minuto=minutosed.get()
        duracion='{}:{}'.format(hora,minuto)
        
        hora_recor=horaer.get()
        dia_recor=diar.get()
        fecha_recordatorio=dia_recor+":"+hora_recor

        descripcion=descripcion_texto.get("1.0","end")
        des=descripcion.rstrip()

        im=str(radio.get())
        if im=="1":
            importancia="Normal"
        elif im=="2":
            importancia="Importante"


        #t=Eventos(titulo,fechayhora,importancia,fecha_recordatorio,duracion,des)
        datos=[{"Descripcion":descripcion,"Fecha Recordatorio":fecha_recordatorio,"Importancia":importancia,"Fecha":fecha,"Titulo":titulo}]
        def guardar_evento(datos):
            """Guarda datos en un archivo json cuando el boton de agregar es ejecutado"""
            import json
            with open("eventos.json",'w') as archivo:
                json.dump(datos,archivo)
            Eventos.agregar_evento()
        guardar_evento(datos)

        def modificar_evento():
            from centralizacion import centrar
            import tkinter as tk
            from tkinter import messagebox,ttk

            ventanamod = Toplevel(raiz)
            ventanamod.focus_set()
            ventanamod.title("Modificar evento")
            ventanamod.geometry("270x450")
            centrar(ventanamod,270,450)

            import json
            with open("eventos.json",'r') as archivo:
                data=json.load(archivo)
                print(data)
           
            #Label modifcar evento
            Label(ventanamod,text="Seleccione que evento desea modificar:").place(x=5,y=10)   
            c=ttk.Combobox(ventanamod,values=tituloseventos)
            minutoser.place(x=100,y=100)
            minutoser.config(width="3")


        #boton modificar evento
        boton2=Button(raiz,text="Modificar\n Evento",command=modificar_evento)
        boton2.config(width=9,height=3)
        boton2.place(x=15,y=320)

        #cierra la ventana de agregar
        ventananueva.destroy()
        
    def salir():
        ventananueva.quit()

    

    #BOTON AGREGAR LISTO
    boton_listo=ttk.Button(ventananueva,text="Agregar",command=agregado)
    boton_listo.pack()
    boton_listo.place(x=160,y=415)

    #BOTON SALIR
    boto_salir=ttk.Button(ventananueva,text="Salir",command=salir)
    boto_salir.pack()
    boto_salir.place(x=20,y=415)



#boton agregar evento
boton1=Button(raiz,text="Agregar\nEvento",command=abrir_ventana)
boton1.config(width=7,height=3)
boton1.place(x=210,y=320)




numerosemana=calcular_semana_actual(anio,mes)
mostrar_calendario(anio,mes,numerosemana)

raiz.mainloop()