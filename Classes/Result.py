import json
import Scripts.ConexionMySQL as mysql
import Scripts.ConexionMongoDB as mongo


class Result:
    def __init__(self, id=None, sensor_id=None, data=None, date=None):
        self.id = id
        self.sensor_id = sensor_id
        self.data = data
        self.date = date

    def selectDB(self, db):
        if db == 'mysql':
            db = mysql
        elif db == 'mongo':
            db = mongo
        else:
            db = json

        return db

    def insert(self, sensor_id, data, date, db):
        mydb = self.selectDB(db)
        newResult = Result(sensor_id=sensor_id, data=data, date=date)
        mydb.insert('results', newResult.sensor_id, newResult.data, newResult.date)

    def show(self, db):
        mydb = self.selectDB(db)
        resultArray = mydb.show('results')
        return resultArray

    def update(self, fieldSet, valueSet, fieldWhere, conditional, valueWhere, db):
        mydb = self.selectDB(db)
        mydb.update('results', fieldSet, valueSet, fieldWhere, conditional, valueWhere)

    def delete(self, valueID, db):
        mydb = self.selectDB(db)
        mydb.delete('results', valueID)
