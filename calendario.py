print("calendar")
import calendar
import locale
locale.setlocale(locale.LC_ALL, '')
#meses
#imprime los meses y las abreviaturas
for i in range(1,13):
    print(calendar.month_abbr[i],calendar.month_name[i])

#dias
for i in range(0,7):
    print(calendar.day_abbr[i],calendar.day_name[i])

print(calendar.monthrange(2023,3))
print(calendar.monthcalendar(2023,3))
print(calendar.weekheader(10))

for semana in calendar.monthcalendar(2023,3):
    print(semana)