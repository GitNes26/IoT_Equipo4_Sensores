import datetime
from Classes.Sensor import Sensor
from Classes.Result import Result
#import GPIO

S = Sensor()
R = Result()
dbTitle = ''
dbs = ''
menu = True

#METODOS DE OPCION

#METODO PARA CONEXION A DB
def selectDB():
    print("|------------------- Base de Datos ------------------|")
    print("|     1.- MySQL     2.- MongoDB     3.- LocalJSON    |")
    mydb = input("| Elige que base de datos desea utilizar: ")
    if mydb == '1':
        print("|                BD -> MySQL                         |")
        dbTitle = "-MySQL-"
        dbs = 'mysql'
    elif mydb == '2':
        print("|                BD -> MongoDB                       |")
        dbTitle = "MongoDB"
        dbs = 'mongo'
    else:
        print("|                BD -> LocalJSON                     |")
        dbTitle = "-JSON--"
        dbs = 'json'
    print("|                                                    |")
    return (dbTitle, dbs)

def menu():
    print("|----------------------- MENU -------------" + db[0] + "---|")
    print("|   1.- Sensores                 2.- Resultados      |")
    print("|               3.- Seleccionar DB                   |")
    print("|                                                    |")
    print("|                  0.- Salir                         |")
    print("|                                                    |")
    action = input("|                Ingresar a => ");
    print("|                                                    |")
    return action

def SubMenu():
    print("|   1.- Mostrar                      2.- Registrar   |")
    print("|   3.- Modificar                    4.- Eliminar    |")
    print("|                                                    |")
    print("|                     0.- MENU                       |")
    print("|----------------------------------------------------|")
    action = input("                Accion a Realizar => "); print()
    return action

#METODOS CON LOS OBJETOS
def show(table):
    if table == 'sensors':
        reg = S.show(db[1])
        print("|REG|| ID \t||   SENSOR\t\t\t|| COM ||\t\t DESCRIPTION\t\t\t\t||\t   CREATED_AT\t\t\t||\t   UPDATED_AT\t\t\t|")
        for r in reg:
            if db[1] == 'mysql':
                print("| "+str(r[0])+"\t|| "+str(r[1])+"\t||"+str(r[2])+"\t\t||"+str(r[3])+"\t||"+str(r[4])+"\t||"+str(r[5])+"\t||"+str(r[6])+"\t|")
            elif db[1] == 'mongo':
                print("| "+str(r['reg'])+"\t|| "+str(r['id'])+"\t||"+str(r['sensor'])+"\t|| "+str(r['com'])+"\t|| "+str(r['description'])+"\t||" + str(r['created_at']) + "\t||" + str(r['updated_at']) + "\t|")
            else:
                print("en json")
    else:
        reg = R.show(db[1])
        print("|REG|| SENSOR_ID ||   DATA\t||\t   CREATED_AT\t\t\t||\t   UPDATED_AT\t\t\t|")
        for r in reg:
            if db[1] == 'mysql':
                print("| " + str(r[0]) + "\t||" + str(r[1]) + "\t||" + str(r[2]) + "\t||" + str(r[5]) + "\t||" + str(r[6]) + "\t|")
            elif db[1] == 'mongo':
                print("| " + str(r['reg']) + "\t||" + str(r['sensor_id']) + "\t||" + str(r['data']) + "\t||" + str(r['created_at']) + "\t||" + str(r['updated_at']) + "\t|")
            else:
                print("en json")

def insert(table):
    if table == 'sensors':
        id = input("| Clave del sensor: ")
        sensor = input("| Nombre del sensor: ")
        com = input("| Puerto del sensor: ")
        description = input("| Descripcion del sensor: ")
        date = str(datetime.datetime.now())
        S.insert(id, sensor, com, description, date, db[1])
        print("| Sensor registrado")
    else:
        sensor_id = input("| Id del sensor: ")
        com = R.getCom(sensor_id)
        if com in ('3','5','7','8','10','11','12','13','15'): #Tipo FLOAT/DOUBLE/INT/DECIMAL
            data = input("| Dato de lectura: ")
        elif com in ('16','18','19','21','22','23','24','26','29'): #Tipo STRING
            data = float(input("| Dato de lectura: "))
        elif com in ('31','32','33','35','36','37','38','40'): #Tipo BOOLEAN
            data = bool(input("| Dato de lectura: "))
        date = str(datetime.datetime.now())
        R.insert(sensor_id, data, date, db[1])
        print("| Registro agregado")

def update(table):
    fieldSet = input("Cambiar el campo: ")
    valueSet = input("Con el valor: ")
    date = str(datetime.datetime.now())
    #fieldWhere = input("Donde el campo: ")
    #conditional = input("Sea...(=,<,>,...): ")
    #valueWhere = input("Al valor: ")
    valueWhere = (input("Al que tenga el ID: "))
    if table == 'sensors':
        #S.update(fieldSet, valueSet, date, fieldWhere, conditional, valueWhere)
        S.update(fieldSet, valueSet, date, valueWhere, db[1])
        print("| Sensor Actualizado")
    else:
        #R.update(fieldSet, valueSet, date, fieldWhere, conditional, valueWhere)
        R.update(fieldSet, valueSet, date, valueWhere, db[1])
        print("| Registro Actualizado")

def delete(table):
    if table == 'sensors':
        valueID = input("ID del sensor: ")
        S.delete(valueID, db[1])
        print("| Sensor Eliminado")
    else:
        valueID = input("No. del registro: ")
        R.delete(valueID, db[1])
        print("| Registro eliminado")


db = selectDB()
while menu != True:
    action = menu()
    if action in ("1", "2", "3", "0"):
        if action in ("1", "2", "3"):
            if action == "1":
                print("|---------------------- SENSORES --------------------|")
                table = 'sensors'
            elif action == "2":
                print("|--------------------- RESULTADOS -------------------|")
                table = 'results'
            elif action == "3":
                db = selectDB()
                action = menu()
            elif action == "0":
                print("HAS SALIDO DEL MENU\n")
                menu = False
                break

            action = SubMenu()
            if action == "1":
                print(
                    "|------------------------------------------ MOSTRAR --------------------------------------------|")
                show(table)
                print(
                    "|-----------------------------------------------------------------------------------------------|\n")
            elif action == "2":
                print("|------------------ REGISTRAR -------------------|")
                insert(table)
                print("|------------------------------------------------|\n")
            elif action == "3":
                print("|------------------- MODIFICAR ------------------|")
                if table == 'prestamos':
                    print("|----------------- DEVOLUCIONES -----------------|")
                update(table)
                print("|------------------------------------------------|\n")
            elif action == "4":
                print("|------------------- ELIMINAR -------------------|")
                delete(table)
                print("|------------------------------------------------|\n")
            else:
                pass

    else: print("Opcion Invalida|debe de ser un numero entero entre el 0-3\n")
else: print("Fin...")