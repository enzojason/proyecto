from tkinter import *
raiz = Tk()
mi_Frame = Frame(raiz)
mi_Frame.config(width=500, height=400)

mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Metodo grid")
mi_Label.grid(row=0, column=0)

raiz.mainloop()