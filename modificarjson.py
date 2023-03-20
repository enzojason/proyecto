import json
with open("eventos.json",'r') as archivo:
    datos=json.load(archivo)

    datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
    datas = json.loads(datajs)#objeto python

print(datas)
listafeho=[]

for a in range(len(datas)):
    aa=(datas[a])
    for b in aa:
        print("b ",b)
        print(aa[b])
        c=aa[b]
        if b =="Fecha y hora":
            listafeho.append(c)

print(listafeho)
tituloelgido=1
fechayhoraelegido=listafeho[tituloelgido]
print(fechayhoraelegido)

f=fechayhoraelegido.split(sep=",")
for x in f:
    print("a")
    print(x)

import datetime
print(fechayhoraelegido)
datetime_str = fechayhoraelegido
datetime_object = datetime.datetime.strptime(datetime_str, '%d/%m/%Y,%H:%M:%S')
print(datetime_object)
print(datetime_object.strftime("%d"))
print(datetime_object.strftime("%H"))

"""
numero=1
    print(datas)
    print(type(datas))
    datas.pop(1)
with open("eventos.json",'w') as archivo:
    json.dump(datas,archivo)
"""


"""
#mostrar y añadir a lista Titulos
listatitulos=[]
listaitems=[]

for a in range(len(datas)):
    aa=(datas[a])
    for b in aa:
        listaitems.append(b)
        print("b ",b)
        print(aa[b])
        c=aa[b]
        if b == "Titulo":
            listatitulos.append(c)
          
print("lista titulos")
print(listatitulos)

print("lista items")
print(listaitems)
"""
