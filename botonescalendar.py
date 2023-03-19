


from tkinter import *
import calendar
import locale
import datetime
locale.setlocale(locale.LC_ALL, '')

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
    
    

root = Tk()
mi_Frame=Frame(root)
mi_Frame.pack(padx=10,pady=100)
mi_Frame.config(width="550",height="420")
mi_Frame.config(bg="black")

    

print("dia actual",CalendarioSemanal.dia_actual)


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
sigue=ttk.Button(root,text="Next",command=siguiente_semana)
sigue.pack()
sigue.place(x=5,y=5)

ante=ttk.Button(root,text="ant",command=anterior_semana)
ante.pack()
ante.place(x=85,y=5)


root.mainloop()