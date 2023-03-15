"""
BARRA VERTICAL ELECTIVA
from tkinter import *
  
root = Tk()  
root.geometry("400x300") 
v2 = IntVar()
  
def show2():
      
    sel = "Vertical Scale Value = " + str(v2.get()) 
    l2.config(text = sel, font =("Courier", 14))
  
s2 = Scale( root, variable = v2,
           from_ = 1, to = 31,
           orient = VERTICAL) 
  
l4 = Label(root, text = "Vertical Scaler")
  
b2 = Button(root, text ="Display Vertical",
            command = show2,
            bg = "purple", 
            fg = "white")
  
l2 = Label(root)
  
s2.pack(anchor = CENTER) 
l4.pack()
b2.pack()
l2.pack()
  
root.mainloop()
"""









import calendar
from tkinter import messagebox, ttk
import tkinter as tk
def show_selection():
    # Obtener la opción seleccionada.
    selection = combo.get()

    messagebox.showinfo(
        message=f"La opción seleccionada es: {selection}",
        title="Selección"
    )
dias=list()

for x in range(31):
    dias.append(x)

main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox(
    state="readonly",
    values=dias
)
combo.place(x=50, y=50)
button = ttk.Button(text="Mostrar selección", command=show_selection)
button.place(x=50, y=100)
main_window.mainloop()




