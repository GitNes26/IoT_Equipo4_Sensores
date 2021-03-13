import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='sensores'
)
print("MySQL -> conectado a la BD: " + mydb.database)

cursor = mydb.cursor()

'''SETUP'''
v = True
cursor.execute("SHOW TABLES")
for x in cursor:
    v = False
if v:
    cursor.execute("CREATE TABLE sensors (reg int AUTO_INCREMENT PRIMARY KEY, id VARCHAR(20), sensor VARCHAR(50), com VARCHAR(20), description VARCHAR(255), created_at VARCHAR(100), updated_at VARCHAR (100))")
    cursor.execute("CREATE TABLE results (reg Int AUTO_INCREMENT PRIMARY KEY, sensor_id VARCHAR(20) , data_double DOUBLE, data_string VARCHAR(100), data_bool BOOLEAN, created_at VARCHAR(100), updated_at VARCHAR (100))")
    cursor.execute("SHOW TABLES")
else:
    pass
'''SETUP'''

'''MOSTRAR ID'''
def showID():
    return cursor.lastrowid


'''INSERTAR DATOS'''
def insert(table, id=None, sensor=None, sensor_id=None, com=None, description=None, data=None, created_at=None, updated_at=None):
    if table == 'sensors':
        sql = "INSERT INTO " + table + " (id, sensor, com, description, created_at, updated_at) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (id, sensor, com, description, created_at, updated_at)
    else:
        fieldData = filterData(data)
        sql = ("INSERT INTO " + table + " (sensor_id, " + fieldData + ", created_at, updated_at) VALUES (%s,%s,%s,%s)")
        val = (sensor_id, data, created_at, updated_at)
    cursor.execute(sql, val)
    mydb.commit()
    print("| Registro realizado")

'''FILTRAR TIPO DE DATO'''
def filterData(data):
    typee = type(data)
    if typee == str:
        fieldData = 'data_string'
    elif typee == float:
        fieldData = 'data_double'
    else:
        fieldData = 'data_bool'
    return fieldData

'''OBTENER EL COM DEL SENSOR'''
def getCom(sensor_id):
    sql = ("SELECT * FROM sensors WHERE id = '" + sensor_id + "'")
    cursor.execute(sql)
    comm = cursor.fetchone()
    com = comm[3]
    return com


'''MOSTRAR DATOS'''
def show(table):
    sql = ("SELECT * FROM " + table)
    cursor.execute(sql)
    myResult = cursor.fetchall()

    return myResult

'''ACTUALIZAR DATOS'''
def update(table, fieldSet, valueSet, updated_at, valueWhere):
    if table == 'sensors':
        fielWhere = 'id'
    else:
        fieldWhere = 'reg'

    sql = ("UPDATE " + table +
           " SET " + fieldSet + " = %s"
           " WHERE "+fielWhere+" = %s")
    val = (valueSet, valueWhere)
    cursor.execute(sql, val)
    mydb.commit()
    sql = ("UPDATE " + table +
           " SET updated_at = %s"
           " WHERE "+fielWhere+" = %s")
    val = (updated_at, valueWhere)
    cursor.execute(sql, val)
    mydb.commit()
    print("| " + cursor.rowcount, " fila(s) actualizada(s)")

'''ELIMINAR DATOS'''
def delete(table, valueID):
    if table == 'sensors':
        fielWhere = 'id'
    else:
        fieldWhere = 'reg'

    sql = ("DELETE FROM " + table + " WHERE "+fielWhere+" = %s")
    val = (valueID,)
    cursor.execute(sql, val)
    mydb.commit()
    print("| " + cursor.rowcount, " registro(s) eliminado(s)")