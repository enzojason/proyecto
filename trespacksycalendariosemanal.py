import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Pack Demo')
root.geometry("500x400")
root.config(bg="white")



# place widgets top down
frame1 = tk.Frame(root, bg="red")
frame1.pack(ipadx= 50,ipady=50, fill=tk.X)

frame2 = tk.Frame(root,bg="white")
frame2.pack(ipadx= 50,ipady=1, fill=tk.X,padx=25)

frame3 = tk.Frame(root,bg="blue")
frame3.pack(ipadx= 50,ipady=130, fill=tk.X)


def mostrar(numero_semana,mes):
    from tkinter import ttk
    semana=mes[numero_semana]
    y=0
    for x in semana:
        if x==0:
            celda=tk.Label(frame2,height=2,width=5,text="-",bg="grey",)

        else:
            celda=tk.Label(frame2,height=2,width=5,text=x,bg="grey")
        y=y+1
        celda.config(fg="black",bg="white",font=("Verdana",13))
        celda.grid(padx=1,pady=1,row=0,column=y)

import calendar
calendario=calendar.Calendar()
mes = calendario.monthdayscalendar(2023,3)
mostrar(3,mes)

root.mainloop()