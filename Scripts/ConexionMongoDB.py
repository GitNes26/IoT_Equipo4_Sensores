import pymongo


myCluster = pymongo.MongoClient("mongodb+srv://npuentes:npuentes@sandbox.pvuoz.mongodb.net/sensores?retryWrites=true&w=majority")
'''CREANDO COLECCIONES'''
mydb = myCluster['sensores']
colS = mydb['sensors']
colR = mydb['results']

print("MongoDB -> conectado")

'''SEEDERS'''
#data = {"id": 0, "sensor": "sensor", "create_at": "00-00-00 00:00", "update_at": "00-00-00 00:00"}
#s = colS.insert_one(data)
#print(s.inserted_id)

#data = {"id": 0, "sensor_id": 0, "data": 0.0, "create_at": "00-00-00 00:00", "update_at": "00-00-00 00:00"}
#r = colR.insert_one(data)
#print(r.inserted_id)


'''MOSTRAR ID'''
def showID():
    x = colS
    print(x.inserted_id)

def selectCollection(collection):
    if collection == 'sensors':
        col = mydb["sensors"]
    else:
        col = mydb["results"]

    return col

'''INSERTAR DOCUMENTO'''
def insert(collection, sensor=None, sensor_id=None, data=None, create_at=None, update_at=None):
    if collection == 'sensors':
        col = mydb["sensors"]
    else:
        col = mydb["results"]

    c = col.find({}, {"_id": 0, "id": 1}).sort("id", -1).limit(1)
    for i in c:
        d = int(i['id'])

    if collection == 'sensors':
        data = {
            "id": d + 1,
            "sensor": sensor,
            "create_at": create_at,
            "update_at": update_at
        }
        x = colS.insert_one(data)

    else:
        data = {
            "id": d + 1,
            "sensor_id": sensor_id,
            "data": data,
            "create_at": create_at,
            "update_at": update_at
        }
        x = colR.insert_one(data)
    print("Documento agregado")


'''MOSTRAR DOCUMENTO'''
def show(collection):
    col = mydb[collection]
    x = col.find({}, {"_id": 0})

    return x


'''ACTUALIZAR DOCUMENTO'''
def update(collection, fieldSet, valueSet, update_at, fieldWhere=None, valueWhere=None):
    col = mydb[collection]

    fieldWhere = 'sensor'
    conditional = '$set'
    query = {fieldWhere: valueWhere, 'update_at':update_at}
    val = {conditional: {fieldSet: valueSet}}

    x = col.update_one(query, val)
    print(x.modified_count, " documento(s) modificado(s)")


'''ELIMINAR DOCUMENTO'''
def delete(collection, valueID):
    col = mydb[collection]

    query = {'id': valueID}
    x = col.delete_one(query)
    print(x.deleted_count, " documento(s) eliminado(s)")
