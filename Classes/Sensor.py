import Scripts.ConexionLocalJSON as json
import Scripts.ConexionMySQL as mysql
import Scripts.ConexionMongoDB as mongo


class Sensor:
    def __init__(self, reg=None, id=None, sensor=None, com=None, description=None, created_at=None, updated_at=None):
        self.reg = reg
        self.id = id
        self.sensor = sensor
        self.com = com
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def selectDB(self, db):
        if db == 'mysql':
            db = mysql
        elif db == 'mongo':
            db = mongo
        else:
            db = json
        return db

    def insert(self, id, sensor, com, description, date, db):
        mydb = self.selectDB(db)
        newSensor = Sensor(id=id, sensor=sensor, com=com, description=description, created_at=date, updated_at=date)
        mydb.insert('sensors', id=newSensor.id, sensor=newSensor.sensor, com=newSensor.com, description=newSensor.description, created_at=newSensor.created_at, updated_at=newSensor.updated_at)

    def show(self, db):
        mydb = self.selectDB(db)
        sensorArray = mydb.show('sensors')
        return sensorArray

    def update(self, fieldSet, valueSet, date, valueWhere, db):
        mydb = self.selectDB(db)
        mydb.update('sensors', fieldSet=fieldSet, valueSet=valueSet, updated_at=date, valueWhere=valueWhere)

    #def update(self, fieldSet, valueSet, date, fieldWhere, conditional, valueWhere, db):
    #    mydb = self.selectDB(db)
    #    mydb.update('sensors', fieldSet, valueSet, date, fieldWhere, conditional, valueWhere)

    def delete(self, valueID, db):
        mydb = self.selectDB(db)
        mydb.delete('sensors', valueID)