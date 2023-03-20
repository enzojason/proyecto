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

cr=open("eventos.json",'w')
cr.close()

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

    listaeventos=[]
    
    def agregar_evento():
        import json
        Eventos.listaeventos
        with open ("eventos.json",'w') as archivo:
            json.dump(Eventos.listaeventos,archivo)
    



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
        import json
        import datetime
        import tkinter as tk
        from tkinter import messagebox,ttk
        messagebox.showinfo(message="Evento Agregado", title="Calendario")
        titulo=tituloe.get()
        #fecha y hora actuales
        fechayhora=(fechan+","+horaln)

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
        fecha_recordatorio=(diare+","+horar)

        descripcion=descripcion_texto.get("1.0","end")
        des=descripcion.rstrip()

        im=str(radio.get())
        if im=="1":
            importancia="Normal"
        elif im=="2":
            importancia="Importante"
       
        import json
        entry={"Descripcion":des,"Fecha Recordatorio":fecha_recordatorio,"Importancia":importancia,"Fecha y hora":fechayhora,"Titulo":titulo,"Duracion":duracion}
        Eventos.listaeventos.append(entry)
        Eventos.agregar_evento()
           
        def eliminar_evento():
            from centralizacion import centrar
            import tkinter as tk
            from tkinter import messagebox,ttk

            ventanam = Toplevel(raiz)
            ventanam.focus_set()
            ventanam.title("Eliminar evento")
            ventanam.geometry("200x200")
            centrar(ventanam,200,200)
                
            import json
            with open("eventos.json",'r') as archivo:
                datos=json.load(archivo)
                datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
                datas = json.loads(datajs)#objeto python
            
                listatitulos=[]
            for a in range(len(datas)):
                aa=(datas[a])
            for b in aa:
                c=aa[b]
                if b == "Titulo":
                    listatitulos.append(c) 

            def salirr():
                ventanam.quit()

            def eliminar():
                #eliminar un evento
                from tkinter import messagebox
                messagebox.showinfo(message="Se ha eliminado un evento", title="Eliminar Evento")
                with open("eventos.json",'r') as archivo:
                    datos=json.load(archivo)
                    datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
                    datas = json.loads(datajs)#objeto python
                    for i in range(len(listatitulos)):
                        if listatitulos[i] == combotitulo.get():
                                numero=i
                    datas.pop(numero)
                with open("eventos.json",'w') as archivo:
                    json.dump(datas,archivo)

            #boton salir
            bs=ttk.Button(ventanam,text="Salir",command=salirr)
            bs.pack()
            bs.place(x=10,y=140)

             #boton guardar
            bg=ttk.Button(ventanam,text="Elimnar",command=eliminar)
            bg.pack()
            bg.place(x=100,y=140)

            #Label 
            Label(ventanam,text="Seleccione el Evento \n a eliminar:").place(x=10,y=25)   
            combotitulo=ttk.Combobox(ventanam,values=listatitulos)
            combotitulo.place(x=50,y=80)
            combotitulo.config(width="12")
            

        def modificar_evento():
            from centralizacion import centrar
            import tkinter as tk
            from tkinter import messagebox,ttk

            ventanamod = Toplevel(raiz)
            ventanamod.focus_set()
            ventanamod.title("Modificar evento")
            ventanamod.geometry("200x200")
            centrar(ventanamod,200,200)
            #listas para combox de titulos y items para modificar
            import json
            with open("eventos.json",'r') as archivo:
                datos=json.load(archivo)
            datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
            datas = json.loads(datajs)#objeto python
            #mostrar y añadir a lista Titulos
            listatitulos=[]
            listaitems=[]
            for a in range(len(datas)):
                aa=(datas[a])
                for b in aa:
                    listaitems.append(b)
                    c=aa[b]
                    if b == "Titulo":
                        listatitulos.append(c)
               

            def selecciontitulo():
                f=Frame(ventanamod)
                f.pack()
                f.config(width="270",height="450")

                Label(f,text="Seleccione item a modificar").place(x=15,y=40)

                #combox modificar
                comboitem=ttk.Combobox(ventanamod,values=listaitems)
                comboitem.place(x=40,y=80)
                comboitem.config(width="14")

                #boton seleccionar item a modifica
                def mostrar_casillero():
                    fe = Toplevel(raiz)
                    fe.focus_set()
                    fe.title("Modificar evento")
                    fe.geometry("200x200")
                    centrar(fe,200,200)
                    a=comboitem.get()
                    Label(fe,text="Ingrese el nuevo valor de \n"+a).place(x=20,y=40)
                    nuevo=Entry(fe,width="25")
                    nuevo.pack()
                    nuevo.place(x=22,y=100)
                    nuevo.insert(0, "Nueva@ "+a)
                    nuevo.focus_set()

                    def salirc():
                        fe.quit()
                    
                    def guardarcambios():
                        from tkinter import messagebox
                        messagebox.showinfo(message="Cambios Guardados", title="Modificar Calendario")
                        import json
                        with open("eventos.json",'r') as archivo:
                            datos=json.load(archivo)
                            datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
                            datas = json.loads(datajs)#objeto python
                        
                        with open("eventos.json",'w') as archivo:
                            #elegir titulo a modificar
                            for i in range(len(listatitulos)):
                                if listatitulos[i] == combotitulo.get():
                                    tituloelegido=i

                            #modifica el titulo
                            aa=(datas[tituloelegido])
                            for b in aa:
                                if b == comboitem.get():
                                    #Aqui se pone en a el nuevo titulo a cambiar ejemplo puse un input
                                    aa[b]=nuevo.get()

                            #guardar la modificacion
                            json.dump(datas,archivo, indent=4)

                    #boton salir
                    bs=ttk.Button(fe,text="Salir",command=salirc)
                    bs.pack()
                    bs.place(x=10,y=140)

                    #boton guardar
                    bg=ttk.Button(fe,text="Guardar",command=guardarcambios)
                    bg.pack()
                    bg.place(x=100,y=140)

                ci=ttk.Button(ventanamod,text="Aceptar",command=mostrar_casillero)
                ci.place(x=50,y=140)

                
                
            #Label modifcar evento
            Label(ventanamod,text="Seleccione el Evento \n a modificar:").place(x=10,y=25)   
            combotitulo=ttk.Combobox(ventanamod,values=listatitulos)
            combotitulo.place(x=50,y=80)
            combotitulo.config(width="12")
            #boton seleccionar
            bc=ttk.Button(ventanamod,text="Seleccionar",command=selecciontitulo)
            bc.place(x=50,y=140)

        #boton modificar evento
        boton2=Button(raiz,text="Modificar\n Evento",command=modificar_evento)
        boton2.config(width=9,height=3)
        boton2.place(x=15,y=325)

        #boton eliminar evento
        boton3=Button(raiz,text="Eliminar\n Evento",command=eliminar_evento)
        boton3.config(width=9,height=3)
        boton3.place(x=455,y=325)

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