import Scripts.ConexionLocalJSON as json
import Scripts.ConexionMySQL as mysql
import Scripts.ConexionMongoDB as mongo


class Result:
    def __init__(self, id=None, sensor_id=None, data=None, create_at=None, update_at=None):
        self.id = id
        self.sensor_id = sensor_id
        self.data = data
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

    def insert(self, sensor_id, data, date, db):
        mydb = self.selectDB(db)
        newResult = Result(sensor_id=sensor_id, data=data, create_at=date, update_at=date)
        mydb.insert('results', sensor_id=newResult.sensor_id, data=newResult.data, create_at=newResult.create_at, update_at=newResult.update_at)

    def show(self, db):
        mydb = self.selectDB(db)
        resultArray = mydb.show('results')
        return resultArray

    def update(self, fieldSet, valueSet, date, valueWhere, db):
        mydb = self.selectDB(db)
        mydb.update('results', fieldSet, valueSet, date, valueWhere)


    #def update(self, fieldSet, valueSet, fieldWhere, date, conditional, valueWhere, db):
    #    mydb = self.selectDB(db)
    #    mydb.update('results', fieldSet, valueSet, date, fieldWhere, conditional, valueWhere)

    def delete(self, valueID, db):
        mydb = self.selectDB(db)
        mydb.delete('results', valueID)
