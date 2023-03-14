# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:31:08 2023

@author: Enzo
"""
import datetime
import tkinter as tk
from tkinter import ttk


print("calendario")
class Eventos():
    def __init__(self,titulo,importancia,fecha_recordatorio,fecha_hora=datetime.datetime.now(),duracion=1,descripcion="",etiquetas=""):
        """Se crea el objeto evento"""
        self.titulo=titulo
        self.fecha_hora=fecha_hora
        self.descripcion=descripcion
        self.importancia=importancia
        self.fecha_recordatorio=fecha_recordatorio
        self.etiquetas=etiquetas
        
  
evento1=Eventos("primera fecha","importante","21")
#tkinder
ventana = tk.Tk()
ventana.title("Calendario-Main")
ventana.config(width=500, height=400)
ventana.mainloop()

