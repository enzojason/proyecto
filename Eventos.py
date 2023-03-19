class Eventos():
    def __init__(self,titulo,fecha,hora,importancia,fecha_recordatorio,duracion=1,descripcion="",etiquetas=""):
        """Se crea el objeto evento"""
        self.titulo=titulo
        self.fecha=fecha
        self.hora=hora
        self.descripcion=descripcion
        self.importancia=importancia
        self.fecha_recordatorio=fecha_recordatorio
        self.etiquetas=etiquetas
    
    def guardar_evento(self):
        import json
        datos={"Titulo":self.titulo,"Fecha":self.fecha,"Hora":self.hora,"Importancia":self.importancia,"Fecha Recordatorio":self.fecha_recordatorio,"Descripcion":self.descripcion}
        with open("eventos.json",'w') as archivo:
            json.dump(datos,archivo)