import pymongo


myCluster = pymongo.MongoClient("mongodb+srv://npuentes:npuentes@sandbox.pvuoz.mongodb.net/sensores?retryWrites=true&w=majority")
'''CREANDO COLECCIONES'''
mydb = myCluster['sensores']
colS = mydb['sensors']
colR = mydb['results']

print("MongoDB -> conectado")

'''SEEDERS'''
#data = {"reg": 0, "id": "0-A", "sensor": "Nombre del Sensor", "com": "puerto de conexion", "description": "descripcion", "created_at": "00-00-00 00:00", "updated_at": "00-00-00 00:00"}
#s = colS.insert_one(data)
#print(s.inserted_id)

#data = {"reg": 0, "sensor_id": 0, "data": 0.0, "created_at": "00-00-00 00:00", "updated_at": "00-00-00 00:00"}
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
def insert(collection, id=None, sensor=None, sensor_id=None, com=None, description=None, data=None, created_at=None, updated_at=None):
    col = selectCollection(collection)

    c = col.find({}, {"_id": 0, "reg":1, "id": 1}).sort("id", -1).limit(1)
    for i in c:
        r = int(i['reg'])

    if collection == 'sensors':
        data = {
            "reg": r + 1,
            "id": id,
            "sensor": sensor,
            "com": com,
            "description": description,
            "created_at": created_at,
            "updated_at": updated_at
        }
        colS.insert_one(data)

    else:
        data = {
            "reg": r + 1,
            "sensor_id": sensor_id,
            "data": data,
            "created_at": created_at,
            "updated_at": updated_at
        }
        colR.insert_one(data)
    print("| Documento agregado")


'''MOSTRAR DOCUMENTO'''
def show(collection):
    col = selectCollection(collection)

    x = col.find({}, {"_id": 0})

    return x


'''ACTUALIZAR DOCUMENTO'''
def update(collection, fieldSet, valueSet, updated_at, valueWhere):
    col = selectCollection(collection)

    if collection == 'sensors':
        fieldWhere = 'id'
    else:
        fieldWhere = 'reg'

    query = {fieldWhere: valueWhere}
    val = {"$set": {fieldSet: valueSet}}

    col.update_one(query, val)
    updateAt(collection, updated_at, valueWhere, fieldWhere)
def updateAt(collection, updated_at, id, fieldWhere):
    col = selectCollection(collection)
    query = {fieldWhere: id}
    val = {"$set": {"updated_at": updated_at}}

    x = col.update_one(query, val)
    print(x.modified_count, "| fecha actualizada")


'''ELIMINAR DOCUMENTO'''
def delete(collection, valueID):
    col = selectCollection(collection)

    if collection == 'sensors':
        fieldWhere = 'id'
    else:
        fieldWhere = 'reg'

    query = {fieldWhere: valueID}
    x = col.delete_one(query)
    print(x.deleted_count, "| documento(s) eliminado(s)")
