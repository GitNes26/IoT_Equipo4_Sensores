import json
from P2_Sensores.Classes.Sensor import Sensor
from P2_Sensores.Classes.Result import Result

listSensors = []
listResults = []
myData = {}


def listsJSON(list):
    if list == 'sensors':
        myData['sensorList'] = []
        dataJSON = 'dataSensors.json'
        nameList = 'sensorList'
    else:
        myData['resultList'] = []
        dataJSON = 'dataResults.json'
        nameList = 'resultList'
    return (myData, dataJSON, nameList)


def getReg(list):
    dataList = listsJSON(list)
    with open('..DataJSON/'+dataList[1]) as f:
        listJSON = json.load(f)
        for i in listJSON[dataList[2]]:
            reg = i['reg']
        reg += 1
    return reg

def insert(list, id=None, sensor=None, sensor_id=None, com=None, description=None, data=None, created_at=None, updated_at=None):
    dataList = listsJSON(list)
    reg = getReg(list)
    if list == 'sensors':
        newObject = Sensor(reg=reg, id=id, sensor=sensor, com=com, description=description, created_at=created_at, updated_at=updated_at)
    else:
        newObject = Result(reg=reg, sensor_id=sensor_id, data=data, created_at=updated_at, updated_at=updated_at)
    myData[dataList[2]].append(encoderObject(list, newObject))
    with open('DataJSON/' + dataList[1], 'w') as f:
        json.dump(myData, f, indent=4)
    print('| Sensor guardado')

def show(list):
    if list == 'sensors':
        return listSensors
    else:
        return listResults

def encoderObject(list, object):
    if list == 'sensors':
        return {
            'reg': object.reg,
            'id': object.id,
            'sensor': object.sensor,
            'com': object.com,
            'description': object.description,
            'created_at': object.created_at,
            'updated_at': object.updated_at
        }
    else:
        return {
            'reg': object.reg,
            'sensor_id': object.sensor_id,
            'data': object.data,
            'created_at': object.created_at,
            'updated_at': object.updated_at
        }

def update(list, fieldSet, valueSet, date, valueWhere):
    pass

def delete(list, valueID):
    pass

