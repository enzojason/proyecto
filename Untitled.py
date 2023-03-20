import json
with open("eventos.json",'r') as a:
    datos=json.load(a)
with open('eventos.json', 'w') as f:
    json.dump(datos, f, indent=4)

listatitulos=list()

datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
datas = json.loads(datajs)#objeto python

#mostrar y añadir a lista Titulos
for a in range(len(datas)):
    aa=(datas[a])
    for b in aa:
        print("b ",b)
        print(aa[b])
        c=aa[b]
        if b == "Titulo":
            listatitulos.append(c)
          
print("lista titulos")
print(listatitulos)

#elegir titulo a modificar
tituloelegido=int()
tituloelegido=1
#modifica el titulo
aa=(datas[tituloelegido])
for b in aa:
    print("b ",b)
    print(aa[b])
    c=aa[b]
    if b == "Titulo":
        print("ingrese nuevo titulo")
        a=str(input())
        #Aqui se pone en a el nuevo titulo a cambiar ejemplo puse un input
        aa[b]=a

#guardar la modificacion
with open("eventos.json",'w') as archivo:
    json.dump(datas,archivo, indent=4)
        
        
print(datas)
print(type(datas))
print(listatitulos)

