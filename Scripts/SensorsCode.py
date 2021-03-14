import serial
import csv
from datetime import datetime
import simplejson
from Mysql import BaseDatos as DB
from Mongodb import DbMongo as Mng
from Documentos import documentos as Doc
import time

Id = 0
value = ""
id_sensor = 0
nombre = ""
descripcion = ""
doc = Doc(Id, id_sensor, value, nombre, descripcion)
db = DB()
Mdb = Mng()
fecha = datetime.now()
fecha = fecha.strftime("%Y-%m-%d %H:%M:%S")


class sensores(object):
    def _init_(self, idi, nombre):
        self.idi = idi
        self.nombre = nombre

    def LeerSensor(self, idi):
        serialArduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
        time.sleep(1)
        valor = 0
        datos = "Hay movimiento"
        while True:
            cad = serialArduino.readline().decode('ascii').strip()
            if cad:
                pos = cad.index(":")
                label = cad[:pos]
                value = cad[pos + 1:]
                if idi == 3:
                    if label == 'dis':
                        if valor != value:
                            print("Es val de la distancia es: {} Cm\n ******".format(value))
                            doc.crearSensorUltrasonic(1, value, fecha)
                            db.InsertarDatos(idi, value, fecha)
                            Mdb.InsertarSensor(idi, value, fecha)
                            valor = value
                if idi == 4:
                    if label == 'Humedad':
                        if valor != value:
                            print("Es valor de la humedad es: {} %\n ******".format(value))
                            doc.crearSensorHumedad(1, value, fecha)
                            db.InsertarDatos(idi, value, fecha)
                            Mdb.InsertarSensor(idi, value, fecha)
                            valor = value
                if idi == 2:
                    if label == 'Temperatura':
                        if valor != value:
                            print("Es valor de la Temperatura es: {} C\n ******".format(value))
                            doc.crearSensorTemperatura(1, value, fecha)
                            db.InsertarDatos(idi, value, fecha)
                            Mdb.InsertarSensor(idi, value, fecha)
                            valor = value
                if idi == 1:
                    if label == 'Hay Movimiento':
                        print("Hay movimiento")
                        doc.crearSensorPir(1, datos, fecha)
                        db.InsertarDatos(idi, datos, fecha)
                        Mdb.InsertarSensor(idi, datos, fecha)

    def MostrarDatoss(self, idi):
        print("Mysql")
        db.MostrarDatos(idi)
        print("Mongo")
        Mdb.MostrarDatos(idi)
        print("Archivos")
        Doc.verSensor(idi)