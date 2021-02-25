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
    cursor.execute("CREATE TABLE sensors (id int AUTO_INCREMENT PRIMARY KEY , sensor VARCHAR(50))")
    cursor.execute("CREATE TABLE results (id Int AUTO_INCREMENT PRIMARY KEY , sesonr int , data_int VARCHAR(), date VARCHAR(100))")
    cursor.execute("SHOW TABLES")
else:
    pass
'''SETUP'''

'''MOSTRAR ID'''
def showID():
    return cursor.lastrowid


'''INSERTAR DATOS'''
def insert(table, sensor=None, sensor_id=None, data=None, date=None):
    if table == 'sensors':
        sql = "INSERT INTO " + table + " (sensor) VALUES (%s)"
        val = (sensor,)
    else:
        sql = ("INSERT INTO " + table + " (sensor_id, data, date) VALUES (%s,%s,%s)")
        val = (sensor_id, data, date)
    cursor.execute(sql, val)
    mydb.commit()
    print("Registro realizado")


'''MOSTRAR DATOS'''
def show(table):
    sql = ("SELECT * FROM " + table)
    cursor.execute(sql)
    myResult = cursor.fetchall()

    return myResult

'''ACTUALIZAR DATOS'''
def update(table, fieldSet, valueSet, fieldWhere, coditional, valueWhere):
    sql = ("UPDATE " + table +
           " SET " + fieldSet + " = %s " +
           "WHERE " + fieldWhere + " " + coditional + " %s")
    val = (valueSet, valueWhere)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, " fila(s) actualizada(s)")


'''ELIMINAR DATOS'''
def delete(table, valueID):
    sql = ("DELETE FROM " + table + " WHERE id = %s")
    val = (valueID,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, " registro(s) eliminado(s)")