import calendar
import locale
import datetime
import tkinter as tk
from centralizacion import centrar
locale.setlocale(locale.LC_ALL, '')
from tkinter import *

#ventana principal
raiz=tk.Tk()
raiz.title("Calendario") #Cambiar el nombre de la ventana
raiz.geometry("500x400")
centrar(raiz,550,400)
raiz.iconbitmap("calendario.ico") #Cambiar el icono
raiz.resizable(0,0) #si la ventana es manipulable de x,y 0,0=NO redimencionar

#frame
mi_Frame=Frame(raiz)
mi_Frame.pack(padx=10,pady=100)
mi_Frame.config(width="550",height="420")
mi_Frame.config(bg="black")

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
#clase evento 

class Eventos():
    def __init__(self,titulo,fechayhora,importancia,fecha_recordatorio,duracion,descripcion="",etiquetas=""):
        """Se crea el objeto evento"""
        self.titulo=titulo
        self.fechayhora=fechayhora
        self.descripcion=descripcion
        self.importancia=importancia
        self.duracion=duracion
        self.fecha_recordatorio=fecha_recordatorio
        self.etiquetas=etiquetas
        
    
    def agregar_evento():
        #agrega eventos en archivo json
        import json
        with open("datos.json",'r') as ar:
            data=json.load(ar)
        with open("eventos.json",'a') as archivo:
            json.dump(data,archivo)

class CalendarioSemanal():
    def __init__(self,numero): 
        self.numero=numero
    x=datetime.datetime.now()
    diax=x.strftime("%d")
    dia_actual=int(diax)
    m=x.strftime("%m")
    mes_actual=int(m)
    a=x.strftime("%Y")
    anio=int(a)

    calendario=calendar.Calendar()
    mes = calendario.monthdayscalendar(anio,mes_actual)
    for a in range(len(mes)):
        semana=mes[a]
        for dias in semana:
            if dias==dia_actual:
                numero_de_semana=a

from tkinter import ttk
#BOTON CAMBIAR EL CALENDARIO A MENSUAL
cambiar=ttk.Button(raiz,text="Calendario Mensual")
cambiar.place(x=5,y=10)

#funcion que muestra el calendario SEMANAL
def mostrar_calendario(mes,numero_semana):
    semana=mes[numero_semana]
    CalendarioSemanal.numero_de_semana=numero_semana
    y=0
    for x in semana:
        if x==0:
            celda=Label(mi_Frame,height=9,width=6,text="-",bg="grey")
        else:
            celda=Label(mi_Frame,height=9,width=6,text=x,bg="grey")
        y=y+1
        celda.config(fg="black",bg="white",font=("Verdana",13))
        celda.grid(padx=1,pady=1,row=0,column=y)


mostrar_calendario(CalendarioSemanal.mes,CalendarioSemanal.numero_de_semana)
def siguiente_semana():
    s=CalendarioSemanal.numero_de_semana + 1
    mostrar_calendario(CalendarioSemanal.mes,s)

def anterior_semana():
    s=CalendarioSemanal.numero_de_semana - 1
    mostrar_calendario(CalendarioSemanal.mes,s)

from tkinter import ttk
#boton siguiente semana
sigue=ttk.Button(raiz,text="Semana Siguiente",command=siguiente_semana)
sigue.pack()
sigue.place(x=430,y=295)

#boton anterior semana
ante=ttk.Button(raiz,text="Semana Anterior",command=anterior_semana)
ante.pack()
ante.place(x=15,y=295)

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
    radio = tk.IntVar()
    radio.set(1)
    #CREACION DE HORAS,DIAS Y MESES EN LISTA
    x=datetime.datetime.now()
    d=x.strftime("%d")
    dia_actual=int(d)            
    m=x.strftime("%m")
    a=x.strftime("%Y")
    h=x.strftime("%H")

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
    Label(ventananueva,text="Descripción:").place(x=4,y=327)
    #texto descripcion
    descripcion_texto = Text(ventananueva, height=3,width=32)
    descripcion_texto.pack()
    descripcion_texto.place(x=4,y=350)
    
    def agregado():
    #titulo,importancia,fecha_recordatorio,fecha_hora,descripcion):
        import json
        import datetime
        import tkinter as tk
        from tkinter import messagebox,ttk
        messagebox.showinfo(message="Evento Agregado", title="Calendario")
        titulo=tituloe.get()
        #fecha y hora actuales
        fechayhora=[fechan+","+horaln]

        #duracion
        horaf=horaed.get()
        minutof=minutosed.get()
        duracion='{}:{}'.format(horaf,minutof)

        #dia hora min recordatorio
        hora_recor=horaer.get()
        dia_recor=diar.get()
        mier=minutoser.get()

        diare=dia_recor+"/"+"3"+"/"+"2023"
        horar = hora_recor+":"+mier
        fecha_recordatorio=[diare+","+horar]

        descripcion=descripcion_texto.get("1.0","end")
        des=descripcion.rstrip()

        im=str(radio.get())
        if im=="1":
            importancia="Normal"
        elif im=="2":
            importancia="Importante"

        datos=[{"Descripcion":des,"Fecha Recordatorio":fecha_recordatorio,"Importancia":importancia,"Fecha y hora":fechayhora,"Titulo":titulo,"Duracion":duracion}]
        def guardar_evento(datos):
            """Guarda datos en un archivo json cuando el boton de agregar es ejecutado"""
            import json
            with open("datos.json",'w') as archivo:
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
            ventanamod.geometry("270x350")
            centrar(ventanamod,270,350)
            
            
            #configuracion
            import json
            with open("eventos.json",'r') as a:
                datoss=json.load(a)
            with open('eventos.json', 'w') as f:
                json.dump(datoss, f, indent=4)

            listatitulos=list()

            datajs = json.dumps(datoss, indent=4, sort_keys=True)#list json
            datas = json.loads(datajs)#objeto python
            #mostrar y añadir a lista Titulos
            for a in range(len(datas)):
                aa=(datas[a])
                for b in aa:
                    c=aa[b]
                    if b == "Titulo":
                        listatitulos.append(c)

            def selecciontitulo():
                f=Frame(ventanamod)
                f.pack()
                f.config(width="270",height="350")
                Label(f,text="Modificar: ").place(x=20,y=100)
                
                Label(f,text="Titulo:").place(x=20,y=140)
                titutlom=Entry(f)
                titutlom.place(x=70,y=140)
                titutlom.insert(0, "Nuevo Titulo")

                Label(f,text="Fecha:").place(x=20,y=170)
                fecham=Entry(f)
                fecham.place(x=70,y=170)
                fecham.insert(0,"dd/mm/aa")


                Label(f,text="Hora:").place(x=20,y=200)
                horam=Entry(f)
                horam.place(x=20,y=200)
                horam.insert(0,"Hora")


                


            #Label modifcar evento
            Label(ventanamod,text="Seleccione que evento desea modificar:").place(x=5,y=5)   
            c=ttk.Combobox(ventanamod,values=listatitulos)
            c.place(x=50,y=50)
            c.config(width="6")
            #boton seleccionar
            bc=ttk.Button(ventanamod,text="Seleccionar",command=selecciontitulo)
            bc.place(x=120,y=50)

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
from tkinter import ttk
boton1=ttk.Button(raiz,text="Agregar Evento",command=abrir_ventana)
boton1.pack()
boton1.place(x=220,y=330)

raiz.mainloop()