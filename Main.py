#import json
#import Scripts.ConexionMySQL as mysql
#import Scripts.ConexionMongoDB as mongo
from Classes.Sensor import Sensor as sensor
from Classes.Result import Result as result

S = sensor()
R = result()
#mydb = mysql
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
        #mydb = mysql
        print("|                BD -> MySQL                         |")
        dbTitle = "-MySQL-"
        dbs = 'mysql'
    elif mydb == '2':
        #mydb = mongo
        print("|                BD -> MongoDB                       |")
        dbTitle = "MongoDB"
        dbs = 'mongo'
    else:
        #mydb = json
        print("|                BD -> LocalJSON                     |")
        dbTitle = "-JSON--"
        dbs = 'json'
    print("|                                                    |")
    return (dbTitle, dbs)#,mydb)

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
        print("| ID ||   SENSOR\t|")
        for r in reg:
            if db[1] == 'mysql':
                print("| "+str(r[0])+"\t||"+r[1]+"\t|")
            elif db[1] == 'mongo':
                print("| "+str(r['id'])+"\t||"+r['sensor']+"\t|")
            else:
                print("en json")
    else:
        reg = R.show(db[1])
        print("| ID ||   SENSOR_ID\t||   DATA\t\t||   DATE\t\t|")
        for r in reg:
            if db[1] == 'mysql':
                print("| " + str(r[0]) + "\t||" + str(r[1]) + "\t||" + str(r[2]) + "\t||" + r[3] + "\t||")
            elif db[1] == 'mongo':
                print("| " + str(r['id']) + "\t||" + str(r['sensor_id']) + "\t||" + str(r['data']) + "\t||" + r['date'] + "\t||")
            else:
                print("en json")




db = selectDB()
#mydb = db[1]
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
            else:
                db = selectDB()
                #mydb = db[1]
                action = menu()
            action = SubMenu()
            if action == "1":
                print(
                    "|---------------------------------------------------------- MOSTRAR --------------------------------------------------------------|")
                show(table)
                print(
                    "|---------------------------------------------------------------------------------------------------------------------------------------|\n")
            elif action == "2":
                print("|------------------ REGISTRAR -------------------|")
                #InsertarDB(table)
                print("|------------------------------------------------|\n")
            elif action == "3":
                print("|------------------- MODIFICAR ------------------|")
                if table == 'prestamos':
                    print("|----------------- DEVOLUCIONES -----------------|")
                #ActualizarDB(table)
                print("|------------------------------------------------|\n")
            elif action == "4":
                print("|------------------- ELIMINAR -------------------|")
                #EliminarDB(table)
                print("|------------------------------------------------|\n")
            else:
                pass
        else:
            print("HAS SALIDO DEL MENU\n")
            menu = False

    else: print("Opcion Invalida|debe de ser un numero entero entre el 0-3\n")
else: print("Fin...")