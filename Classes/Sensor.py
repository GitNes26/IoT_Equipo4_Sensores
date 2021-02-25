import json
import Scripts.ConexionMySQL as mysql
import Scripts.ConexionMongoDB as mongo


class Sensor:
    def __init__(self, id=None, sensor=None):
        self.id = id
        self.sensor = sensor

    def selectDB(self, db):
        if db == 'mysql':
            db = mysql
        elif db == 'mongo':
            db = mongo
        else:
            db = json

        return db

    def insert(self, sensor, db):
        mydb = self.selectDB(db)
        newSensor = Sensor(sensor=sensor)
        mydb.insert('sensors', newSensor.sensor)

    def show(self, db):
        mydb = self.selectDB(db)
        sensorArray = mydb.show('sensors')
        return sensorArray

    def update(self, fieldSet, valueSet, fieldWhere, conditional, valueWhere, db):
        mydb = self.selectDB(db)
        mydb.update('sensors', fieldSet, valueSet, fieldWhere, conditional, valueWhere)

    def delete(self, valueID, db):
        mydb = self.selectDB(db)
        mydb.delete('sensors', valueID)