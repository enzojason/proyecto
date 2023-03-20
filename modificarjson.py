import json
with open("eventos.json",'r') as archivo:
    datos=json.load(archivo)

    datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
    datas = json.loads(datajs)#objeto python
    numero=1
    print(datas)
    print(type(datas))
    datas.pop(1)

with open("eventos.json",'w') as archivo:
    json.dump(datas,archivo)



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

#elegir titulo a modificar

#modifica el titulo
#

#guardar la modificacion
#with open("eventos.json",'w') as archivo:json.dump(datas,archivo, indent=4)
        
        

