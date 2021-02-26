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
    cursor.execute("CREATE TABLE sensors (id int AUTO_INCREMENT PRIMARY KEY , sensor VARCHAR(50), create_at VARCHAR(100), update_at VARCHAR (100))")
    cursor.execute("CREATE TABLE results (id Int AUTO_INCREMENT PRIMARY KEY , sensor_id int , data int, create_at VARCHAR(100), update_at VARCHAR (100))")
    cursor.execute("SHOW TABLES")
else:
    pass
'''SETUP'''

'''MOSTRAR ID'''
def showID():
    return cursor.lastrowid


'''INSERTAR DATOS'''
def insert(table, sensor=None, sensor_id=None, data=None, create_at=None, update_at=None):
    if table == 'sensors':
        sql = "INSERT INTO " + table + " (sensor, create_at, update_at) VALUES (%s,%s,%s)"
        val = (sensor, create_at, update_at)
    else:
        sql = ("INSERT INTO " + table + " (sensor_id, data, create_at, update_at) VALUES (%s,%s,%s,%s)")
        val = (sensor_id, data, create_at, update_at)
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
#def update(table, fieldSet, valueSet, update_at, fieldWhere, coditional, valueWhere):
#    sql = ("UPDATE " + table +
#           " SET " + fieldSet + " = %s ,"
#           " SET update_at = %s "
#           "WHERE " + fieldWhere + " " + coditional + " %s")
#    val = (valueSet, update_at, valueWhere)
#    cursor.execute(sql, val)
#    mydb.commit()
#    print(cursor.rowcount, " fila(s) actualizada(s)")

def update(table, fieldSet, valueSet, update_at, valueWhere):
    sql = ("UPDATE " + table +
           " SET " + fieldSet + " = %s"
           " WHERE id = %s")
    val = (valueSet, valueWhere)
    cursor.execute(sql, val)
    mydb.commit()
    sql = ("UPDATE " + table +
           " SET update_at = %s"
           " WHERE id = %s")
    val = (update_at, valueWhere)
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