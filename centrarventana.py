import tkinter as tk
from tkinter import ttk
#ventana = tk.Tk()
#ventana.title("Conversor de temperatura")
#ventana.config(width=400, height=300)
root=tk.Tk()
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
wventana = 500
hventana = 400
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
root.mainloop()