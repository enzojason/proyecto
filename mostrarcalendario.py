import calendar
import locale
locale.setlocale(locale.LC_ALL, '')

def mostrar_calendario():
	for x in calendar.monthcalendar(2023,3):
		print(x)


mostrar_calendario()