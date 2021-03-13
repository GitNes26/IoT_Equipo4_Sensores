import Scripts.DB.ConexionLocalJSON as json
import Scripts.DB.ConexionMySQL as mysql
import Scripts.DB.ConexionMongoDB as mongo


class Result:
    def __init__(self, reg=None, sensor_id=None, data=None, created_at=None, updated_at=None):
        self.reg = reg
        self.sensor_id = sensor_id
        self.data = data
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

    def insert(self, sensor_id, data, date, db):
        mydb = self.selectDB(db)
        newResult = Result(sensor_id=sensor_id, data=data, created_at=date, updated_at=date)
        mydb.insert('results', sensor_id=newResult.sensor_id, data=newResult.data, created_at=newResult.created_at, updated_at=newResult.updated_at)

    def show(self, db):
        mydb = self.selectDB(db)
        resultArray = mydb.show('results')
        return resultArray

    def update(self, fieldSet, valueSet, date, valueWhere, db):
        mydb = self.selectDB(db)
        mydb.update('results', fieldSet=fieldSet, valueSet=valueSet, updated_at=date, valueWhere=valueWhere)


    #def update(self, fieldSet, valueSet, fieldWhere, date, conditional, valueWhere, db):
    #    mydb = self.selectDB(db)
    #    mydb.update('results', fieldSet, valueSet, date, fieldWhere, conditional, valueWhere)

    def delete(self, valueID, db):
        mydb = self.selectDB(db)
        mydb.delete('results', valueID)
