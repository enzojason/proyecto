from tkinter import *
import calendar
import locale
locale.setlocale(locale.LC_ALL, '')

root = Tk()
calendario=calendar.monthcalendar(2023,3)
for r in range(len(calendario)):
    for c in range(0, 7):
        if calendario[r][c]==0:
            pass
        else:
            cell = Label(root, width=5,text=calendario[r][c])
            cell.grid(padx=5, pady=5, row=r, column=c)

for semana in calendar.monthcalendar(2023,3):
    print(semana)



root.mainloop()