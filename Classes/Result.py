import json
import Scripts.ConexionMySQL as mysql
import Scripts.ConexionMongoDB as mongo

mydb = mysql
class Result:
    def __init__(self, id=None, sensor=None):
        self.id = id
        self.sensor = sensor

    def selectDB(self,db):
        if db == 'mysql':
            db = mysql
        elif db == 'mongo':
            db = mongo
        #else:
        #   db = json

        return db

    def insert(self, sensor, db):
        #mydb = self.selectDB(db)
        mydb
        newMiembro = Sensor(sensor=sensor)
