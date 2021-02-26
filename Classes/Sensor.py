import Scripts.ConexionLocalJSON as json
import Scripts.ConexionMySQL as mysql
import Scripts.ConexionMongoDB as mongo


class Sensor:
    def __init__(self, id=None, sensor=None, create_at=None, update_at=None):
        self.id = id
        self.sensor = sensor
        self.create_at = create_at
        self.update_at = update_at

    def selectDB(self, db):
        if db == 'mysql':
            db = mysql
        elif db == 'mongo':
            db = mongo
        else:
            db = json
        return db

    def insert(self, sensor, date, db):
        mydb = self.selectDB(db)
        newSensor = Sensor(sensor=sensor, create_at=date, update_at=date)
        mydb.insert('sensors', sensor=newSensor.sensor, create_at=newSensor.create_at, update_at=newSensor.update_at)

    def show(self, db):
        mydb = self.selectDB(db)
        sensorArray = mydb.show('sensors')
        return sensorArray

    def update(self, fieldSet, valueSet, date, valueWhere, db):
        mydb = self.selectDB(db)
        mydb.update('sensors', fieldSet=fieldSet, valueSet=valueSet, update_at=date, valueWhere=valueWhere)

    #def update(self, fieldSet, valueSet, date, fieldWhere, conditional, valueWhere, db):
    #    mydb = self.selectDB(db)
    #    mydb.update('sensors', fieldSet, valueSet, date, fieldWhere, conditional, valueWhere)

    def delete(self, valueID, db):
        mydb = self.selectDB(db)
        mydb.delete('sensors', valueID)